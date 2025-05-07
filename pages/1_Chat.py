import streamlit as st
st.title("Chat with GPT")
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
st.session_state.api_key = st.text_input("Enter OpenAI API Key", type="password", value=st.session_state.api_key)
@st.cache_data(show_spinner=False)
def ask_gpt(prompt):
    openai.api_key = st.session_state.api_key
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
prompt = st.text_area("질문을 입력하세요")
if st.button("질문하기") and prompt:
    with st.spinner("답변 생성 중..."):
        st.write(ask_gpt(prompt))
