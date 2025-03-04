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



@cl.on_chat_start
async def on_chat_start():
    
    llm = ChatOpenAI(name="MC QA", model_name="gpt-4o", temperature=0.2, streaming=True)

    # Prompt for code generation
    prompt_template = """Answer the question based on the following question and context.  

    Question: {question}

    Context: {context}

        """

    prompt_code = ChatPromptTemplate.from_template(prompt_template)

    runnable = (
        # {"context": retriever | format_docs}
         prompt_code
        | llm
        | StrOutputParser()
    )

    cl.user_session.set("runnable", runnable)


def format_docs(docs):
   return "\n\n".join(doc.page_content for doc in docs)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    questionMsg=message.content

    async for chunk in runnable.astream(
        # {"question": questionMsg},
        {"context": format_docs(retriever.invoke(questionMsg)) , "question": questionMsg},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)
        # print(chunk)

    await msg.send()    

    print("end")


 