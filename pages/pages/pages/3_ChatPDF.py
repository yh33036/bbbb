import streamlit as st
import openai
from PyPDF2 import PdfReader
st.title("PDF 챗봇")
api_key = st.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")
if uploaded_file and "api_key" in st.session_state:
    reader = PdfReader(uploaded_file)
    text = "".join(page.extract_text() for page in reader.pages)
    question = st.text_input("질문을 입력하세요")
    if question:
        prompt = f"다음은 PDF 내용입니다:\n{text[:3000]}\n\n질문: {question}"
        client = openai.OpenAI(api_key=st.session_state["api_key"])
        response = client.chat.completions.create(
            model="gpt-4.0-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message.content)
if st.button("Clear"):
    st.experimental_rerun()
