import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.llms import Ollama
# import os
from langchain_groq import ChatGroq

# from dotenv import load_dotenv
# load_dotenv()

## Langsmith Tracking
LANGSMITH_API_KEY= st.secrets['LANGSMITH_API_KEY']
LANGCHAIN_TRACING = "true"
LANGCHAIN_PROJECT = "Simple Q&A Chatbot With Ollama"
# os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
# os.environ["LANGCHAIN_TRACING"]="true"
# os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

####### LANGSMITH EMAIL USED -> knfuejmiservlimcvv@nesopf.com

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=ChatGroq(model="llama3-70b-8192", groq_api_key=st.secrets['GROQ_API_KEY'])
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Q&A Chatbot with Llama3 - BhaskarGPT 😎")
st.write("Made with \u2764\ufe0f by Bhaskar Shivaji Kumbhar 😎")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["llama3.1"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")
