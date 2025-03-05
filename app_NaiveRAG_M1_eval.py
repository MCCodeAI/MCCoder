from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig


from langchain import hub
from langchain_community.document_loaders import WebBaseLoader, TextLoader, PyPDFLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

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

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Txt loader of sample codes, for BM25 search
loader = TextLoader("./docs/WMX3API_MCEval_Samplecodes.txt")
docs = loader.load()

#Sample code chunk with dedicated separators
separators = ['``']  # Adjust based on actual document structure, `` is the end of each code snippet.
text_splitter = RecursiveCharacterTextSplitter(separators=separators, keep_separator=True, chunk_size=1000, chunk_overlap=200, add_start_index=True)
splits = text_splitter.split_documents(docs)



# Global variable to store the name of the LLM
llm_name = None
llm = ChatOpenAI(name="MCCoder", model_name="gpt-4o", streaming=True)
runnable = None
 
 
def on_chat_start():
    
    global llm_name
    # Store the name of the LLM in the global variable
    llm_name = llm.model_name

    # Prompt for code generation
    prompt_template = """Generate a Python script based on the given Question and Context, ensuring that the code structure and formatting align with the Context.

Instructions:
	1.	Extract Key Information:
	•	Identify all Axis numbers, IO Inputs, and IO Outputs mentioned in the Question.
	•	Add this information at the beginning of the generated code in the following format:

# Axes = [Axis_number_1, Axis_number_2, ...]
# Inputs = [byte.bit_1, byte.bit_2, ...]
# Outputs = [byte.bit_1, byte.bit_2, ...]


	•	Example:
If the Question states:
“Move Axis 9, Axis 12, and Axis 2 based on Input 0.3 and 1.2, then activate Output 3.4 and 6.1”,
the script should start with:

# Axes = [9, 12, 2]
# Inputs = [0.3, 1.2]
# Outputs = [3.4, 6.1]


	2.	Code Formatting:
	•	Enclose the entire generated script within triple backticks (```python and ```) to ensure proper formatting.

	3.	Do not import any motion libraries.


    ----------------------------------------------
    
    Question: 
    {question}

    Context: 
    {context}

        """

    prompt_code = ChatPromptTemplate.from_template(prompt_template)

    global runnable
    runnable = (
        # {"context": retriever | format_docs}
         prompt_code
        | llm
        | StrOutputParser()
    )



def self_correct(err_codes):
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




# This function retrieves and concatenates documents for each element in the input string array.
def coder_retrieval(question):

    separator = "\n----------\n"
    long_string = ""


    # initialize the bm25 retriever and faiss retriever
    bm25_retriever = BM25Retriever.from_documents(splits)
    bm25_retriever.k = 5

    # initialize the ensemble retriever
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, retriever], weights=[0.5, 0.5])

    ensemble_docs = ensemble_retriever.invoke(question)

    retrieval_result = format_docs(ensemble_docs)
    long_string +=  "\n" + retrieval_result + separator
    
    return long_string

RunnableCodeinMachine = ''

def on_message(message):
    
    # Input text
    user_question = message
    
    context_msg = coder_retrieval(user_question)
 
    # questionMsg=message.content

    # async for chunk in runnable.astream(
    #     # {"question": questionMsg},
    #     {"context": context_msg, "question": user_question},
    #     config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    # ):
    #     await msg.stream_token(chunk)
        # print(chunk)

    response = runnable.invoke(
    {"context": context_msg, "question": user_question})


    # TaskId file path
    file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/TaskId.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
            task_info = file.read().strip()   

    # Only for making CanonicalCode.
    llm_name = 'CanonicalCode_test'

    # Get python code from the output of LLM
    msgCode = extract_code(response)
    RunnableCode = make_code_runnable(msgCode, llm_name, task_info)

    # Old and new paths
    old_path = f'path_0.dirPath = r"\\\\Mac\\\\Home\\\\Documents\\\\GitHub\\\\MCCodeLog\\\\{llm_name}"'

    new_path = r'path_0.dirPath = r"C:\\"'

    # Replace the old path with the new one
    global RunnableCodeinMachine
    RunnableCodeinMachine = RunnableCode.replace(old_path, new_path)
    RunnableCodeinMachine = re.sub(r'# <logon[\s\S]*?# logon>', '', RunnableCodeinMachine)
    RunnableCodeinMachine = re.sub(r'# <logoff[\s\S]*?# logoff>', '', RunnableCodeinMachine)


    # Run Code in WMX3
    codereturn = SendCode(RunnableCode)

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
        if os.path.exists(file_path):
            os.remove(file_path)

    log_file_path = os.path.join(folder_path, f"{task_info}_{llm_name}_log.txt")
    # Plot with the log file
    plot_log(log_file_path)
    
    sleep(0.1)

    print("end")

