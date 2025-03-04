from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig


from langchain import hub
from langchain_community.document_loaders import WebBaseLoader, TextLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage, SystemMessage

import chainlit as cl
from time import *
from CodeClient import *
from MachineClient import *
from make_code_runnable import *
from plot_log import *
 

import bs4
import os
import re
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv()) 


# Preparation of documents for RAG-------------------------
# Vectorstore, for retrieval
embedding_model=OpenAIEmbeddings(model="text-embedding-3-large")   #text-embedding-3-large   #text-embedding-ada-002    #text-embedding-3-small

# If pdf vectorstore exists
vectorstore_path = "Vectorstore/chromadb-MCCoder"
if os.path.exists(vectorstore_path):
    vectorstore = Chroma(
                    embedding_function=embedding_model,
                    persist_directory=vectorstore_path,
                    ) 
    print("load from disk: " + vectorstore_path)
else:
        # Load from chunks and save to disk
    # vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model, persist_directory=vectorstore_path) 
    print("load from chunks")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# Txt loader of sample codes, for BM25 search
loader = TextLoader("./docs/WMX3API_MCEval_Samplecodes.txt")
docs = loader.load()

#Sample code chunk with dedicated separators
separators = ['``']  # Adjust based on actual document structure, `` is the end of each code snippet.
text_splitter = RecursiveCharacterTextSplitter(separators=separators, keep_separator=True, chunk_size=1000, chunk_overlap=200, add_start_index=True)
splits = text_splitter.split_documents(docs)



# Global variable to store the name of the LLM
llm_name = None
llm = ChatOpenAI(name="MCCoder and QA", model_name="gpt-4o", streaming=True)

@cl.on_chat_start
async def on_chat_start():
    
    
    

    global llm_name
    # Store the name of the LLM in the global variable
    llm_name = llm.model_name

    # Prompt for code generation
    prompt_template = """Write a python code based on the following Question and Context. You need to choose the correct codes from the Context to answer the Question.
    1. Review the question carefully and find all the 'Axis number', IO Inputs and Outputs, and add them to the first lines of the generated code in the following format: 
    # Axes = [Axis number 1, Axis number 2, ...]
    # Inputs = [byte.bit 1, byte.bit 2, ...]
    # Outputs = [byte.bit 1, byte.bit 2, ...]
    For instance, if the question is '...Axis 9..., ...Axis 12..., ...Axis 2..., Input 0.3 and 1.2, ...Output 3.4 and 6.1', then 
    # Axes = [9, 12, 2]
    # Inputs = [0.3, 1.2, ...]
    # Outputs = [3.4, 6.1, ...]
    2. Include all the generated codes within one paragraph between ```python and ``` tags. 
    3. Don't import any library.
    4. Don't create any functions or example usage.
    5. You need to wait until the axis reaches the target position and stops, unless otherwise specified.
    ----------------------------------------------

    Question: 
    {question}

    Context: 
    {context}

        """

    prompt_code = ChatPromptTemplate.from_template(prompt_template)

    runnable = (
        # {"context": retriever | format_docs}
         prompt_code
        | llm
        | StrOutputParser()
    )

    cl.user_session.set("runnable", runnable)


@cl.step
async def self_correct(err_codes):
   # remember to write "python" code in the prompt later
    template = """Correct the following codes based on the error infomation. 

        {err_codes}

        """

    custom_rag_prompt = PromptTemplate.from_template(template)
    
    rag_chain = (
            {"err_codes": RunnablePassthrough()}
            | custom_rag_prompt
            | llm
            | StrOutputParser()
        )

    code_corrected=rag_chain.invoke(err_codes)
 
    return(code_corrected)




# Joins the page content of each document with double newline
def format_docs(docs):
   return "\n\n".join(doc.page_content for doc in docs)

 
# Extracts code snippets written in Python from the given text
def extract_code(text):
    # Define the regular expression pattern to find text between ```python and ```
    pattern = r"```python(.*?)```"

    # Use re.findall to find all occurrences
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the matches, join them if there are multiple matches
    return "\n\n---\n\n".join(matches)


@cl.step
# Extracts and formats code instructions from a user question based on specific starting phrases.
async def coder_router(user_question):
    """
    Extracts numbered sections of a user question based on specific starting phrases.
    
    If the question starts with 'Write a python code', 'Python code', or 'write python' (case insensitive),
    it splits the question into paragraphs that start with numbers (e.g., 1., 2., 3.) and adds 
    'Write python code to ' after the numbers. If the question does not start 
    with the specified phrases or does not contain numbered lists, the entire question is saved into a single 
    element array. If the question does not start with the specified phrases, NoCoder is set to 1.
    
    Args:
        user_question (str): The user's question.
    
    Returns:
        tuple: NoCoder (int), an array of strings with each element containing a code instruction or the entire question.
    """
    result = []
    NoCoder = 0
    # Check if the input starts with the specified prefixes
    if re.match(r'(?i)^(Write a python code|Python code|write python)', user_question):
        result.append(user_question)
    else:
        # Save the entire question to the array and set NoCoder to 1
        result.append(user_question)
        NoCoder = 1
    
    return NoCoder, result


@cl.step
# This function retrieves and concatenates documents for each element in the input string array.
async def coder_retrieval(coder_router_result):
    """
    This function takes an array of strings as input. For each element in the array,
    it performs a retrieval using format_docs(retriever.invoke(element))
    and concatenates the element with the retrieval result into one long string, 
    with a newline character between them. Each concatenated result is separated by a specified separator.
    
    Args:
        coder_router_result (list): An array of strings.

    Returns:
        str: A single long string formed by concatenating each element with its retrieval result,
             separated by a newline character, and each concatenated result separated by a specified separator.
    """
    separator = "\n----------\n"
    long_string = ""
    for element in coder_router_result:

        # Fusion retrieval or hybrid search
        from langchain.retrievers import BM25Retriever, EnsembleRetriever

        # initialize the bm25 retriever and faiss retriever
        bm25_retriever = BM25Retriever.from_documents(splits)
        bm25_retriever.k = 5

        # initialize the ensemble retriever
        ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, retriever], weights=[0.5, 0.5])

        ensemble_docs = ensemble_retriever.get_relevant_documents(element)

        retrieval_result = format_docs(ensemble_docs)
        long_string += element + "\n" + retrieval_result + separator
    
    return long_string

RunnableCodeinMachine = ''

@cl.on_message
async def on_message(message: cl.Message):
    

    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    # Input text
    user_question = message.content
    
    # Call coder_router function
    NoCoder, coder_router_result = await coder_router(user_question)
    
    # Route the result based on NoCoder value
    if NoCoder == 0:
        coder_return = await coder_retrieval(coder_router_result)
        context_msg = coder_return
    else:
        context_msg = format_docs(retriever.invoke(coder_router_result[0]))

    # questionMsg=message.content


    async for chunk in runnable.astream(
        # {"question": questionMsg},
        {"context": context_msg, "question": user_question},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
        # print(chunk)

    # TaskId file path
    file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/TaskId.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
            task_info = file.read().strip()   

    # Only for making CanonicalCode.
    llm_name = 'CanonicalCode_test'

    # Get python code from the output of LLM
    msgCode = extract_code(msg.content)
    RunnableCode = make_code_runnable(msgCode, llm_name, task_info)

    # Old and new paths
    old_path = f'path_0.dirPath = r"\\\\Mac\\\\Home\\\\Documents\\\\GitHub\\\\MCCodeLog\\\\{llm_name}"'

    new_path = r'path_0.dirPath = r"C:\\"'

    # Replace the old path with the new one
    global RunnableCodeinMachine
    RunnableCodeinMachine = RunnableCode.replace(old_path, new_path)
    RunnableCodeinMachine = re.sub(r'# <logon[\s\S]*?# logon>', '', RunnableCodeinMachine)
    RunnableCodeinMachine = re.sub(r'# <logoff[\s\S]*?# logoff>', '', RunnableCodeinMachine)


    print(RunnableCodeinMachine)

    # Run Code in WMX3
    codereturn = SendCode(RunnableCode)
    # if 'error' in codereturn:
    #     err_codes_0 = codereturn + '\n # ------------------------------- \n' + RunnableCode
    #     code_corrected = await self_correct(err_codes_0)

    

    # lines = msgCode.splitlines()
    # api_start_index = None
    
    # # 查找 '# WMX3 API ' 行的索引
    # for i, line in enumerate(lines):
    #     if line.strip() == '### WMX3 API':
    #         api_start_index = i
    #         break

    # # 如果找到了 '## WMX3 API ' 行，将其和其后的所有行赋值给 API_list
    # if api_start_index is not None:
    #     API_list = lines[api_start_index:]
    
    # text_content = '\n'.join(API_list)
    # # Display API related documents
    # apitext = [
    #     cl.Text(name="simple_text", content=text_content, display="inline", size='small')
    # ]

    # await cl.Message(
    #     content="API reference:",
    #     elements=apitext,
    # ).send()

    folder_path = f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}'
    os.makedirs(folder_path, exist_ok=True)

    # Define plot files name
    plot_filenames = [
        f"{task_info}_{llm_name}_log_plot.png",
        f"{task_info}_{llm_name}_log_2d_plot.png",
        f"{task_info}_{llm_name}_log_3d_plot.png"
    ]

    # Check if the plot files exist in folder_path and delete them if they do
    for filename in plot_filenames:
        file_path = os.path.join(folder_path, filename)
        # if os.path.exists(file_path):
        #     os.remove(file_path)

    log_file_path = os.path.join(folder_path, f"{task_info}_{llm_name}_log.txt")
    # Plot with the log file
    plot_log(log_file_path)
    
    sleep(0.3)

    for filename in plot_filenames:
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            image = cl.Image(path=file_path, name=filename, display="inline", size='large')
            # Attach the image to the message
            await cl.Message(
                content=f"Plot name: {filename}",
                elements=[image],
            ).send()




    await msg.send()    

    print("end")




    #  Sending an action button within a chatbot message
    actions = [
        cl.Action(name="action_button", value="example_value", description="Run!")
    ]

    await cl.Message(content="Run the code in the real machine!", actions=actions).send()




@cl.action_callback("action_button")
async def on_action(action: cl.Action):
    print("Send to real machine for running!")

    codereturn = SendCodetoMachine(RunnableCodeinMachine)
    print(codereturn)

    return "Send to real machine for running!"