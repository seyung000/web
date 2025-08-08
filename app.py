import streamlit as st

st.title("ChatBot")

# 세션 상태에 메시지 기록이 없다면 초기화
if "message_history" not in st.session_state:
    st.session_state.message_history = []

# 사용자 입력 받기
prompt = st.chat_input("무엇이든지 물어보세요~!")

# 입력값이 있으면 message_history에 추가
if prompt and prompt.strip():
    st.session_state.message_history.append({
        "role": "user",
        "content": prompt
    })
    # (선택) 응답도 추가하는 예시
    st.session_state.message_history.append({
        "role": "assistant",
        "content": f"'{prompt}'에 대한 답변입니다."
    })

# 대화 메시지 출력
for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#