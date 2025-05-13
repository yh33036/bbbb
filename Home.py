import streamlit as st

st.title("GPT 기반 웹앱")
st.subheader("🔑 OpenAI API Key 입력")

api_key = st.text_input("API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key
    st.success("API Key 저장됨.")

if "api_key" not in st.session_state:
    st.warning("API Key를 입력하세요.")
