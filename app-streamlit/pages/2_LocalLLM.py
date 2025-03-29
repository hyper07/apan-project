from pathlib import Path
import os

from langchain_community.llms import Ollama
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import UnstructuredExcelLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain.embeddings import OllamaEmbeddings
from streamlit_tags import st_tags, st_tags_sidebar

import streamlit as st
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import pandas as pd

import ollama


file_path = os.getcwd()
llm = Ollama(model="deepseek-r1:1.5b", base_url="http://host.docker.internal:37869", verbose=True)

sample_file_path = ''
columns = []

def sendPrompt(prompt):
    global llm
    response = llm.invoke(prompt)
    return response


CSS = """
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) {
    display: flex;
    flex-direction: row-reverse;
    align-itmes: end;
}

[data-testid="stChatMessageAvatarUser"] + [data-testid="stChatMessageContent"] {
    text-align: right;
}
"""
st.html(f"<style>{CSS}</style>")
st.title("Download LLM Models")
st.write("Check the LLM models from the following links:")
st.write("[OPEN SOURCE LLMs](https://ollama.com/library)")

st.image(file_path+"/images/select_llm.png", width=700)
st.write("Run 'docker exec -ti apan-ollama ollama pull llama3.2:1b' on the command to download the model")
st.image(file_path+"/images/download_llm.png", width=700)


st.title("Sample Chat UI")

if "messages" not in st.session_state.keys(): 
        st.session_state.messages = [
            {"role": "assistant", "content": "What can I help you with?"}
        ]

if prompt := st.chat_input("Your prompt"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
with st.chat_message("assistant"):
    # Placeholder for the assistant's message


    # Retrieve the last user prompt from session state
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        message_placeholder = st.empty()
        response = ""
        prompt = st.session_state.messages[-1]["content"]

        # Use the local LLM defined earlier
        response_stream = llm.stream(prompt)  # Stream the response
        for chunk in response_stream:
            # Remove <think> tags from the chunk
            chunk = chunk.replace("<think>", "").replace("</think>", "")
            response += chunk
            message_placeholder.write(response)  # Update the assistant's message progressively

        st.session_state.messages.append({"role": "assistant", "content": response})
