import streamlit as st
import random

st.set_page_config(page_title="영어 단어 암기", page_icon="📚", layout="centered")

st.title("📚 영어 단어 암기 테스트")

# 세션 상태 초기화
if "words" not in st.session_state:
    st.session_state.words = {}
if "quiz_list" not in st.session_state:
    st.session_state.quiz_list = []
if "score" not in st.session_state:
    st.session_state.score = {"correct": 0, "wrong": 0}
if "current_word" not in st.session_state:
    st.session_state.current_word = None

# 단어 입력
st.subheader("✏️ 단어 입력")
word = st.text_input("영어 단어 입력")
meaning = st.text_input("뜻 입력")

if st.button("추가"):
    if word and meaning:
        st.session_state.words[word] = meaning
        st.success(f"{word} - {meaning} 추가됨!")

# 퀴즈 시작 버튼
if st.button("퀴즈 시작"):
    st.session_state.quiz_list = list(st.session_state.words.items())
    st.session_state.score = {"correct": 0, "wrong": 0}
    st.session_state.current_word = None

# 문제 출제
if st.session_state.quiz_list:
    if not st.session_state.current_word:
        st.session_state.current_word = random.choice(st.session_state.quiz_list)

    word, meaning = st.session_state.current_word
    st.subheader(f"❓ 단어: {word}")
    answer = st.text_input("뜻을 입력하세요", key="answer_box")

    if st.button("제출"):
        if answer.strip() == meaning:
            st.success("✅ 정답! 🎉")
            st.session_state.score["correct"] += 1
        else:
            st.error(f"❌ 오답! (정답: {meaning})")
            st.session_state.score["wrong"] += 1

        # 출제한 문제 제거
        st.session_state.quiz_list.remove(st.session_state.current_word)
        st.session_state.current_word = None

# 모든 문제가 끝난 후 결과 카드
if not st.session_state.quiz_list and st.session_state.score["correct"] + st.session_state.score["wrong"] > 0:
    correct = st.session_state.score["correct"]
    wrong = st.session_state.score["wrong"]
    total = correct + wrong
    percent = round(correct / total * 100, 1)

    card_html = f"""
    <div style="
        background: linear-gradient(135deg, #ffb6c1, #ff69b4);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        color: white;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        width: 400px;
        margin: auto;
    ">
        <h2 style="margin-bottom: 15px;">🎀 결과 카드 🎀</h2>
        <p style="font-size:20px; margin:10px 0;">✅ 정답: <b>{correct}</b></p>
        <p style="font-size:20px; margin:10px 0;">❌ 오답: <b>{wrong}</b></p>
        <p style="font-size:22px; margin-top:20px;">정답률: <b>{percent}%</b></p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
