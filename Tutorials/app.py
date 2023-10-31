# Bring in deps:
'''
Yo! import Protocol from typing_extensions, this is very important
because, you might get the ModuleNotFound Error while using
from langchain.llms import OpenAI
make sure your typing_extensions is upgraded, if it's not use
the code below in the terminal:
pip install --upgrade typing_extensions
'''
from typing_extensions import Protocol

import os
import openai
from apikey import api_key
os.environ["OPENAI_API_KEY"] = api_key

# dotenv:
from dotenv import main
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())
main.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

# App Framework:
st.title("YouTube GPT Creator")
prompt = st.text_input('Plug in your prompt here!')


# Prompt templates:
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'Write me a youtube video script based on this title: {title}'
)

# LLMS:
llm = OpenAI(temperature=0.0)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)

if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)