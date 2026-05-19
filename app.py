import streamlit as st
import random

st.set_page_config(
    page_title="랜덤 점수 게임",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 랜덤 점수 게임")

st.write("버튼을 눌러 점수를 획득하세요!")

# 점수 저장
if "score" not in st.session_state:
    st.session_state.score = 0

if "message" not in st.session_state:
    st.session_state.message = "게임 시작!"

# 현재 점수 출력
st.subheader(f"현재 점수: {st.session_state.score}")

# 플레이 버튼
if st.button("플레이!"):

    random_number = random.randint(1, 10)

    st.session_state.score += random_number

    st.session_state.message = f"+{random_number} 점 획득!"

    # 승리 체크
    if st.session_state.score >= 50:
        st.session_state.message = "🏆 승리!"

# 메시지 출력
st.write(st.session_state.message)

# RESET 버튼
if st.button("RESET"):

    st.session_state.score = 0

    st.session_state.message = "게임이 초기화되었습니다."

# 추가 정보
st.divider()

st.markdown(
    """
    ### 게임 설명
    - 플레이 버튼을 누르면 랜덤 점수를 얻습니다.
    - 50점 이상이면 승리합니다.
    - RESET 버튼으로 초기화할 수 있습니다.
    """
)
