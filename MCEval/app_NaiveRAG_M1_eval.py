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
from langchain_deepseek import ChatDeepSeek
from langchain_community.chat_models import ChatHunyuan

from time import *
from CodeClient import *
from MachineClient import *
from make_code_runnable import *
from plot_log import *

from userlib.user_logger import log_message

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

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# Txt loader of sample codes, for BM25 search
loader = TextLoader("./docs/WMX3API_MCEval_Samplecodes.txt")
docs = loader.load()

#Sample code chunk with dedicated separators
separators = ['``']  # Adjust based on actual document structure, `` is the end of each code snippet.
text_splitter = RecursiveCharacterTextSplitter(separators=separators, keep_separator=True, chunk_size=1000, chunk_overlap=200, add_start_index=True)
splits = text_splitter.split_documents(docs)



# llm = ChatOpenAI(name="MCCoder-M1-o3-mini-M1", model_name="o3-mini")   #
# llm_name = 'o3-mini-M1'

# llm = ChatDeepSeek(name="MCCoder-DeepSeek-R1-M1", model_name="deepseek-reasoner", temperature=0.0)  # 
# llm_name = 'DeepSeek-R1-M1'


# llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",model="deepseek-r1",temperature=0)  # o3-mini gpt-4o, ,temperature=0.2
 
# codegene_runnable = None
# llm_name = 'DeepSeek-R1-M1'  #CanonicalCode, gpt-4o-M3


llm = ChatOpenAI(openai_api_key="CTYUN_API_KEY",openai_api_base="https://wishub-x1.ctyun.cn/v1",model_name="7ba7726dad4c4ea4ab7f39c7741aea68",temperature=0)  # o3-mini gpt-4o, ,temperature=0.2
llm_name = 'DeepSeek-R1-M1'  #CanonicalCode, gpt-4o-M3


# Prompt for code generation
prompt_template = """Generate a Python script based on the given Question and Context, ensuring that the code structure and formatting align with the Context.

Instructions:
1.	Extract Key Information:
•	Identify all Axis numbers, IO Inputs, and IO Outputs mentioned in the Question, list numbers from small to big.
•	Add this information at the beginning of the generated code in the following format:

# Axes = [Axis_number_1, Axis_number_2, ...]
# IOInputs = [byte.bit_1, byte.bit_2, ...]
# IOOutputs = [byte.bit_1, byte.bit_2, ...]


•	Example:
If the Question states:
“Move Axis 9, Axis 12, and Axis 2 based on Input 0.3 and 1.2, then activate Output 3.4 and 6.1”,
the script should start with:

# Axes = [2, 9, 12]
# IOInputs = [0.3, 1.2]
# IOOutputs = [3.4, 6.1]


2.	Code Formatting:
•	Enclose the entire generated script within triple backticks (```python and ```) to ensure proper formatting.

3.	Do not import any motion libraries.

4. Wait for axes stop moving after every single motion, but don't wait in the middle of continuous motion.
----------------------------------------------

Question: 
{question}

Context: 
{context}

    """

prompt_code = ChatPromptTemplate.from_template(prompt_template)

codegene_runnable = (
    # {"context": retriever | format_docs}
        prompt_code
    | llm
    | StrOutputParser()
)



# Joins the page content of each document with double newline
def format_docs(docs):
   return "\n\n".join(doc.page_content for doc in docs)

def extract_code(text):
    """Extracts the first Python code snippet from the given text."""
    
    # Define the regular expression pattern to find text between ```python and ```
    pattern = r"```python(.*?)```"

    # Use re.search to find the first occurrence
    match = re.search(pattern, text, re.DOTALL)
    
    # Return the first match if found, otherwise return an empty string
    return match.group(1) if match else ""




# This function retrieves and concatenates documents for each element in the input string array.
def coder_retrieval(question):

    separator = "\n----------\n"
    long_string = ""


    # initialize the bm25 retriever and faiss retriever
    bm25_retriever = BM25Retriever.from_documents(splits)
    bm25_retriever.k = 6

    # initialize the ensemble retriever
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, retriever], weights=[0.5, 0.5])

    ensemble_docs = ensemble_retriever.invoke(question)
    ensemble_docs = ensemble_docs[:5] 

    retrieval_result = format_docs(ensemble_docs)
    long_string +=  "\n" + retrieval_result + separator
    
    return long_string

RunnableCodeinMachine = ''

def on_message(task_id, message):
    """Handle incoming message, generate executable code with post-processing."""
    
    llm_start_time = time()
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

    response = codegene_runnable.invoke(
    {"context": context_msg, "question": user_question})

    llm_end_time = time()
    llm_execution_time = llm_end_time - llm_start_time
    print(f"llm execution time: {llm_execution_time}")

    # # Define TaskId file path
    # file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/TaskId.txt'
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     # Read task info from file
    #     task_info = file.read().strip()   
    task_info = task_id


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

    log_message(f"{codereturn}")

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

    os.system("say --voice=\"Mei-Jia\" o")

    print("end")

    # Return the final codereturn
    return codereturn + f"\nllm_time: {llm_execution_time}s"