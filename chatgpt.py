#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: chatgpt.py
#Author: 韩伟
#Mail: hanwei2008123@163.com
#Created Time: 2023-05-07 22:18:04
############################

import openai
import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv
openai.api_key = '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'
def generate_response(prompt):
    completion=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
    )
    message=completion.choices[0].text
    return message

st.title("ChatGPT-like Web App")
#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input("You:",key='input')
if user_input:
    output=generate_response(user_input)
    #store the output
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
