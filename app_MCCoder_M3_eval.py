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
embedding_model=OpenAIEmbeddings(model="text-embedding-3-large")   

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
codegene_llm = ChatOpenAI(name="MCCoder", model_name="gpt-4o", streaming=True, temperature=0.2)
taskdecom_llm = codegene_llm
codegene_runnable = None
 
 
# Store the name of the LLM in the global variable
llm_name = codegene_llm.model_name

# Code generation llm >>>>>>>>>>>>>
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

codegene_runnable = (
    prompt_code
    | codegene_llm
    | StrOutputParser()
)

# Task decomposition llm >>>>>>>>>>>>>
# Prompt for task decomposition
taskdecom_prompt_template = """
You are a task decomposer that breaks down a user question into multiple sub-tasks, listing them as separate lines. For example, the user question '1. Write Python code to move Axis 6 to 20 with a velocity of 900 using a trapezoid profile ; 2. set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0; 3. Move Axis 7 to 30; ' should be decomposed into three tasks, adding 'Write Python code to' to each:

1. Write Python code to move Axis 6 to 20 with a velocity of 900 using a trapezoid profile ; 
2. Write Python code to set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0; 
3. Write Python code to Move Axis 7 to 30; 

If the user question contains only a single task, output the original question as is, adding 'Write Python code to' at the beginning if it’s not already present.

User question:
{question}

Output:

    """

taskdecom_prompt_code = ChatPromptTemplate.from_template(taskdecom_prompt_template)

taskdecom_runnable = (
    taskdecom_prompt_code
    | taskdecom_llm
    | StrOutputParser()
)

def task_decomposition(user_question):
    """Decomposes a user question into a list of non-empty task lines."""
    task_str=taskdecom_runnable.invoke({"question": user_question})
    lines = task_str.splitlines()
    lines = [line for line in lines if line.strip()] # To remove empty lines from the list of lines
    return lines

def task_rag(tasks):
    """Performs retrieval for each task and formats results with task-reference pairs."""
    separator = "\n----------\n"
    result_list = []
    
    # Perform retrieval for each task
    for task in tasks:
        # Retrieve relevant reference content using retriever
        retrieved_docs = retriever.invoke(task)
        
        # Format the documents into a string using the existing format_docs function
        references = format_docs(retrieved_docs)
        
        # Build the output format for a single task
        task_output = f"Task: {task}\nReference:\n{references}"
        result_list.append(task_output)
    
    # Join all task outputs with the separator
    context_output = separator.join(result_list)
    
    return context_output
    

def self_correct(original_code, err_info):
    """Correct the code based on original code and error information using LLM."""
    
    # Retrieve relevant documents based on error information
    retrieved_docs = retriever.invoke(err_info)
    
    # Format retrieved documents into a single string
    references = format_docs(retrieved_docs)
    
    # Combine original error info with retrieved references into a richer context
    err_context = f"{err_info}\n\nReferences:\n{references}"
    
    # Define the prompt template with original code and error context
    template = """Correct the following code based on the error information and context provided.

    Original Code:
    ```
    {original_code}
    ```

    Error Context:
    ```
    {err_context}
    ```

    Please provide the corrected code only, without additional explanations.
    """

    # Create a prompt template from the defined string
    custom_rag_prompt = PromptTemplate.from_template(template)
    
    # Build the processing chain: prompt -> LLM -> output parser
    self_correct_chain = (
        custom_rag_prompt
        | codegene_llm
        | StrOutputParser()
    )

    # Execute the chain with the input variables
    code_corrected = self_correct_chain.invoke({
        "original_code": original_code,
        "err_context": err_context
    })
    
    # Return the corrected code
    return code_corrected




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
    bm25_retriever.k = 5

    # initialize the ensemble retriever
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, retriever], weights=[0.5, 0.5])

    ensemble_docs = ensemble_retriever.invoke(question)

    retrieval_result = format_docs(ensemble_docs)
    long_string +=  "\n" + retrieval_result + separator
    
    return long_string

RunnableCodeinMachine = ''

def on_message(message):
    """Handle incoming message, generate executable code, and manage self-correction with post-processing."""
    
    # Extract user question from the message
    user_question = message

    # Decompose the user question into tasks
    tasks = task_decomposition(user_question)
    
    # Retrieve context for tasks using RAG
    context_msg = task_rag(tasks)
 
    # Generate response using codegen runnable with context and question
    response = codegene_runnable.invoke(
        {"context": context_msg, "question": user_question}
    )

    # Define TaskId file path
    file_path = r'/Users/yin/Documents/GitHub/MCCodeLog/TaskId.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read task info from file
        task_info = file.read().strip()   

    # Specify LLM name for making CanonicalCode
    llm_name = 'CanonicalCode_test'

    # Extract Python code from LLM output
    msgCode = extract_code(response)
    
    # Convert extracted code into runnable format
    RunnableCode = make_code_runnable(msgCode, llm_name, task_info)

    # # Old and new paths (commented out but retained)
    # old_path = f'path_0.dirPath = r"\\\\Mac\\\\Home\\\\Documents\\\\GitHub\\\\MCCodeLog\\\\{llm_name}"'
    # new_path = r'path_0.dirPath = r"C:\\"'
    # # Replace the old path with the new one
    # global RunnableCodeinMachine
    # RunnableCodeinMachine = RunnableCode.replace(old_path, new_path)
    # RunnableCodeinMachine = re.sub(r'# <logon[\s\S]*?# logon>', '', RunnableCodeinMachine)
    # RunnableCodeinMachine = re.sub(r'# <logoff[\s\S]*?# logoff>', '', RunnableCodeinMachine)

    # Run Code in WMX3
    codereturn = SendCode(RunnableCode)

    # Set maximum correction attempts
    max_attempts = 3
    attempt_count = 0

    # Check for errors in codereturn and attempt self-correction
    while "err" in codereturn and attempt_count < max_attempts:
        # Call self_correct with original code and error info
        corrected_code = self_correct(msgCode, codereturn)
        
        # Convert corrected code back to runnable format
        RunnableCode = make_code_runnable(corrected_code, llm_name, task_info)
        
        # Run the corrected code in WMX3
        codereturn = SendCode(RunnableCode)
        
        # Increment attempt counter
        attempt_count += 1
        
    # Check final state of codereturn
    if "err" not in codereturn:
        # Execute post-processing if no error is present
        folder_path = f'/Users/yin/Documents/GitHub/MCCodeLog/{llm_name}'
        os.makedirs(folder_path, exist_ok=True)

        # Define plot file names
        plot_filenames = [
            f"{task_info}_{llm_name}_log_plot.png",
            f"{task_info}_{llm_name}_log_2d_plot.png",
            f"{task_info}_{llm_name}_log_3d_plot.png"
        ]

        # Check and delete existing plot files in folder_path
        for filename in plot_filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)

        # Define log file path and plot with it
        log_file_path = os.path.join(folder_path, f"{task_info}_{llm_name}_log.txt")
        plot_log(log_file_path)
        
        # Brief pause to ensure file operations complete
        sleep(0.1)

        # Indicate successful completion
        print("end")
    elif attempt_count >= max_attempts:
        # Output error code if maximum attempts exceeded
        print(f"Error after {max_attempts} attempts: {codereturn}")

    # Return the final codereturn
    return codereturn

