import streamlit as st
from rules import rules_text
import openai
st.title("부경대 도서관 챗봇")
st.session_state.api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.get("api_key", ""))
question = st.text_input("도서관에 대해 궁금한 점을 물어보세요")
if st.button("질문") and question:
    openai.api_key = st.session_state.api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"다음 도서관 규정을 기반으로만 답하세요:\n{rules_text}"},
            {"role": "user", "content": question}
        ]
    )
    st.write(response.choices[0].message.content)
