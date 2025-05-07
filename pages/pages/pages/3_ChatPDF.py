import streamlit as st
import openai
import PyPDF2
st.title("ChatPDF - PDF로 대화하기")
st.session_state.api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.get("api_key", ""))
file = st.file_uploader("PDF 파일 업로드", type="pdf")
@st.cache_data(show_spinner=False)
def ask_pdf_bot(query, pdf_text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"다음 PDF 내용을 기반으로 답하세요:\n{pdf_text}"},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content
if file:
    reader = PyPDF2.PdfReader(file)
    pdf_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    query = st.text_area("PDF 내용 기반으로 질문하세요")
    if st.button("질문") and query:
        with st.spinner("답변 생성 중..."):
            st.write(ask_pdf_bot(query, pdf_text, st.session_state.api_key))
if st.button("Clear"):
    st.experimental_rerun()
