from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import streamlit as st
import time

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


st.header("🤖  Srijibot 👨‍💻", divider="rainbow")
st.markdown("###### A chatbot powered by: GPT-4o-mini")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_active=True

if st.session_state.chat_active:
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    if prompt := st.chat_input("Your Query [Press 'e' to exit]"):
        if prompt == 'e':
            st.session_state.chat_active = False
            st.error("👋 Chat ended!") 
            time.sleep(2.5)
            st.rerun()
        st.session_state.chat_history.append({"role":"human","content":prompt})
        with st.chat_message("human"):
            st.write(prompt)
        response= model.invoke(st.session_state.chat_history)
        st.session_state.chat_history.append({"role":"assistant","content":response.content})
        with st.chat_message("assistant"):
            st.write(response.content)
else:
    if st.button("Restart Chat", type="primary"):
        st.session_state.chat_history = []
        st.session_state.chat_active=True
        st.rerun()


    