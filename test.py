import streamlit as st
import random

st.set_page_config(page_title="영어 단어 암기", page_icon="📚", layout="centered")

st.title("📚 영어 단어 암기 테스트")

# 세션 상태 초기화
if "words" not in st.session_state:
    st.session_state.words = {}
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

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
    if st.session_state.words:
        st.session_state.quiz_started = True
        st.session_state.user_answers = {}
    else:
        st.warning("먼저 단어를 추가하세요!")

# 문제 출제 (모두 한 번에)
if st.session_state.quiz_started:
    st.subheader("📝 퀴즈")
    for i, (w, m) in enumerate(st.session_state.words.items()):
        st.session_state.user_answers[w] = st.text_input(
            f"{i+1}. {w} 의 뜻은?", key=f"answer_{i}"
        )

    if st.button("채점하기"):
        correct = 0
        wrong = 0
        wrong_list = []

        for w, m in st.session_state.words.items():
            user_ans = st.session_state.user_answers.get(w, "").strip()
            if user_ans == m:
                correct += 1
            else:
                wrong += 1
                wrong_list.append((w, m, user_ans))

        total = correct + wrong
        percent = round(correct / total * 100, 1)

        # 🎀 결과 카드
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

        # ❌ 틀린 문제 리스트 출력
        if wrong_list:
            st.subheader("❌ 틀린 문제 복습")
            for w, m, ans in wrong_list:
                st.write(f"- **{w}** → 정답: {m}, 입력: {ans if ans else '미입력'}")
