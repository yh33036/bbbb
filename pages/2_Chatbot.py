import streamlit as st

st.title("📚 부경대학교 도서관 챗봇")

if "api_key" not in st.session_state:
    st.warning("Home에서 API Key를 먼저 입력하세요.")
    st.stop()

openai.api_key = st.session_state["api_key"]

with open("pknu_library_rules.txt", "r", encoding="utf-8") as f:
    rules_text = f.read()

question = st.text_input("도서관 관련 질문을 입력하세요:")

if question:
    system_prompt = "다음은 국립부경대학교 도서관 규정입니다:\n" + rules_text
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    st.write(response.choices[0].message.content)
