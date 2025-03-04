from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import bs4
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
import time
from CodeClient import *

import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv()) 



#SendCode('')




# Vectorstore 
embedding_model=OpenAIEmbeddings(model="text-embedding-3-large")   #text-embedding-3-large   #text-embedding-ada-002    #text-embedding-3-small

# If pdf vectorstore exists
vectorstore_path = "Vectorstore/chromadb-pdf-chunk1000"
if os.path.exists(vectorstore_path):
    vectorstore = Chroma(
                    embedding_function=embedding_model,
                    persist_directory=vectorstore_path,
                    ) 
    print("load from disk")
else:
        # Load from chunks and save to disk
    # vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model, persist_directory=vectorstore_path) 
    print("load from chunks")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})



@cl.on_chat_start
async def on_chat_start():
    
    llm = ChatOpenAI(name="MC Code", model_name="gpt-3.5-turbo", temperature=0, streaming=True)

    # Prompt for code coordination
    prompt_template = """As a motion control specialist skilled in utilizing WMX3, a sophisticated software controller, your task is to amalgamate the provided code fragments into a cohesive, accurate, and executable program. Ensure that all steps are incorporated systematically and without omission. After the codes, provide a detailed explanation of the entire code in a comment.
 
        Question: {question}

        Answer:
        """

    # Prompt for code generation
    # prompt_template = """You are an expert in motion control in WMX3 which is a software controller. You can answer the question and generate the code based on the following context. Give complete definitions and comments. 
# 
        # Context: {context}
#  
        # Question: {question}
# 
        # Answer:"""

    prompt_code = ChatPromptTemplate.from_template(prompt_template)

    runnable = (
        # {"context": retriever | format_docs}
         prompt_code
        | llm
        | StrOutputParser()
    )

    cl.user_session.set("runnable", runnable)


@cl.step
async def agentTaskPlanner(inputMsg):
   
    llmTask = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    template = """You are recognized for your exceptional skill in task decomposition. Your objective is to break down the presented question (task) into precise and clear sub-tasks, each numbered sequentially, without adding explanations.

        For queries framed as a singular, straightforward sentence, your responses should naturally incorporate the initiation and closing of WMX as part of the process. An illustration of this approach is as follows:

        Question: "Write a code to move Axis 1 to position 1000."
        Sub-tasks:

        1. Initialize WMX
        2. Move Axis 1 to position 1000
        3. Close WMX

        In situations where the query encompasses multiple directives within a few sentences, decompose the question into separate, ordered sub-tasks. A sample for this scenario is given below:

        Question: "Write a code to initialize WMX, move Axis 1 to position 1000, sleep for 2 seconds, set output 3.4 to 1, and subsequently close WMX."
        Sub-tasks:

        1. Initialize WMX
        2. Move Axis 1 to position 1000
        3. Sleep for 2 seconds
        4. Set output 3.4 to 1
        5. Close WMX

        Question: {question}

        Sub-tasks:
        """

    custom_rag_prompt = PromptTemplate.from_template(template)
    
    rag_chain = (
            {"question": RunnablePassthrough()}
            | custom_rag_prompt
            | llmTask
            | StrOutputParser()
        )

    MTask=rag_chain.invoke(inputMsg)

    return(MTask)


llmsubTask = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


@cl.step
async def agentSubTaskCode(subTask):
   # remember to write "python" code in the prompt later
    template = """You are an expert in motion control in WMX3 which is a software controller. You can answer the question based on the context, and give a concise code to invoke WMX3 apis, with code comments. 

        {context}

        Question: "write a python code: " + {question}

        Answer:
        """

    custom_rag_prompt = PromptTemplate.from_template(template)
    
    rag_chain = (
            {"context": retriever | format_docs, "question": 
        RunnablePassthrough()}
            | custom_rag_prompt
            | llmsubTask
            | StrOutputParser()
        )

    subTaskCode=rag_chain.invoke(subTask)
 
    return(subTaskCode)

def format_docs(docs):
   return "\n\n".join(doc.page_content for doc in docs)

@cl.step
async def llm_pipeline(inputMsg):

    MTask = await agentTaskPlanner(inputMsg)
    
    completeTaskCode = ""
    subTasks = MTask.split('\n')
    subTaskCount = 0
    for subTask in subTasks:
        if subTask == "": continue
        subTaskCount += 1
        # if subTaskCount == 2: continue
        
        subTaskCode = await agentSubTaskCode(subTask)
    
        completeTaskCode += "\n" + str(subTaskCount) + ".\n" +subTaskCode

    return(completeTaskCode)
 
import re
def extract_code(text):
    # Define the regular expression pattern to find text between ```python and ```
    pattern = r"```python(.*?)```"

    # Use re.findall to find all occurrences
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the matches, join them if there are multiple matches
    return "\n\n---\n\n".join(matches)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable


    msg = cl.Message(content="")
    
    # Task planning and retrieval pipeline.
    completeTaskCode=await llm_pipeline(message.content)
    questionMsg=completeTaskCode

    # questionMsg=message.content

    async for chunk in runnable.astream(
        {"question": questionMsg},
        # {"context": format_docs(retriever.invoke(questionMsg)) , "question": questionMsg},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
        # print(chunk)

    msgCode = extract_code(msg.content)
    print(msgCode)
    SendCode(msgCode)
    await msg.send()    

    print("end")




#     #  Sending an action button within a chatbot message
#     actions = [
#         cl.Action(name="Run Code", value="example_value", description="Run!")
#     ]

#     await cl.Message(content="Run the code in Simulation and real machine!", actions=actions).send()

# @cl.action_callback("action_button")
# async def on_action(action: cl.Action):
#     print("The user clicked on the action button!")

#     return "Thank you for clicking on the action button!"

