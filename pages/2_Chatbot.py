import streamlit as st
import openai
from rules import LIBRARY_RULES
st.title("📚 부경대 도서관 챗봇")
api_key = st.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key
question = st.text_input("도서관에 대해 질문하세요")
if question:
    prompt = f"다음은 도서관 규정입니다:\n{LIBRARY_RULES}\n\n사용자 질문: {question}"
    client = openai.OpenAI(api_key=st.session_state["api_key"])
    response = client.chat.completions.create(
        model="gpt-4.0-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(response.choices[0].message.content)
