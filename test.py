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

# 퀴즈 시작
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
        if a
