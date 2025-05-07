import streamlit as st
import openai
st.title("GPT Chat")
api_key = st.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key
if "messages" not in st.session_state:
    st.session_state.messages = []
user_input = st.text_input("메시지를 입력하세요")
if user_input and "api_key" in st.session_state:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages,
        api_key=st.session_state["api_key"]
    )
    st.session_state.messages.append(response["choices"][0]["message"])
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role']}**: {msg['content']}")
if st.button("Clear"):
    st.session_state.messages = []
