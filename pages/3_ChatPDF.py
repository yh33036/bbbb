import streamlit as st
import PyPDF2

st.title("📄 PDF 기반 챗봇")

if "api_key" not in st.session_state:
    st.warning("Home에서 API Key를 먼저 입력하세요.")
    st.stop()

openai.api_key = st.session_state["api_key"]

uploaded_file = st.file_uploader("PDF 업로드", type="pdf")

@st.cache_data
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    user_q = st.text_input("PDF 내용에 대해 질문하세요:")

    if user_q:
        system_prompt = f"다음은 업로드한 PDF 내용입니다:\n{pdf_text[:3000]}"
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_q}
            ]
        )
        st.write(response.choices[0].message.content)

    if st.button("Clear"):
        uploaded_file = None
        st.experimental_rerun()
