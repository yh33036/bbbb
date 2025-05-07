import streamlit as st
st.title("부경대 도서관 챗봇")
st.session_state.api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.get("api_key", ""))
@st.cache_data(show_spinner=False)
def ask_library_bot(question, rules, api_key):
    openai.api_key = api_key
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"다음 도서관 규정을 기반으로만 답하세요:\n{rules}"},
            {"role": "user", "content": question}
        ]
    )
    return res.choices[0].message.content
question = st.text_input("도서관에 대해 궁금한 점을 물어보세요")
if st.button("질문") and question:
    with st.spinner("답변 생성 중..."):
        st.write(ask_library_bot(question, rules_text, st.session_state.api_key))
