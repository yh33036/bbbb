import streamlit as st

st.title("💬 Chat")

if "api_key" not in st.session_state:
    st.warning("Home에서 API Key를 먼저 입력하세요.")
    st.stop()

openai.api_key = st.session_state["api_key"]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("질문을 입력하세요:")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=st.session_state.chat_history
    )
    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.write(reply)

if st.button("Clear"):
    st.session_state.chat_history = []
