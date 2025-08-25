# app.py

import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="심리 테스트", layout="centered")

# 세션 초기화
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = []

# 점수 초기화
scores = {
    "분석형": 0,
    "감정형": 0,
    "혼란형": 0,
    "행동형": 0
}

# 질문 리스트
questions = [
    {
        "question": "1. 누군가 고민을 이야기하면 나는?",
        "options": {
            "해결 방법을 제시한다.": "분석형",
            "감정에 공감하고 위로한다.": "감정형",
            "괜히 불안해져서 같이 걱정한다.": "혼란형",
            "이야기를 빨리 넘기고 다른 걸 한다.": "행동형"
        }
    },
    {
        "question": "2. 갑작스러운 일정 변경이 생기면?",
        "options": {
            "계획을 다시 정리한다.": "분석형",
            "상대방의 입장을 생각한다.": "감정형",
            "스트레스를 크게 받는다.": "혼란형",
            "그냥 적응한다. 문제없다.": "행동형"
        }
    },
    {
        "question": "3. 낯선 사람들과의 모임에서는?",
        "options": {
            "대화를 관찰하며 분석한다.": "분석형",
            "감정을 나누려 노력한다.": "감정형",
            "긴장되고 불편하다.": "혼란형",
            "즐기며 주도적으로 나선다.": "행동형"
        }
    },
    {
        "question": "4. 스트레스를 받았을 때 나는?",
        "options": {
            "조용히 정리하고 생각한다.": "분석형",
            "누군가에게 털어놓는다.": "감정형",
            "예민해지고 걱정이 많아진다.": "혼란형",
            "운동하거나 뭔가를 해버린다.": "행동형"
        }
    },
    {
        "question": "5. 결정을 내려야 할 때 나는?",
        "options": {
            "이유와 근거를 따진다.": "분석형",
            "기분과 감정에 따른다.": "감정형",
            "망설이고 걱정이 앞선다.": "혼란형",
            "그냥 느낌대로 행동한다.": "행동형"
        }
    },
]

st.title("🧠 당신의 심리 유형 테스트")

# 질문 출력
for i, q in enumerate(questions):
    answer = st.radio(q["question"], list(q["options"].keys()), key=f"q{i}")
    st.session_state.answers.append(answer)

# 제출 버튼
if st.button("🔍 결과 보기") and not st.session_state.submitted:
    st.session_state.submitted = True

    # 점수 계산
    for i, q in enumerate(questions):
        user_answer = st.session_state.answers[i]
        category = q["options"][user_answer]
        scores[category] += 1

    result = max(scores, key=scores.get)

    st.subheader(f"🧾 당신의 심리 유형: **{result}**")

    # 결과별 설명 + 추천
    if result == "분석형":
        desc = "🎯 분석형 - 논리적, 계획적이며 문제해결을 중시합니다."
        book = "『논리의 기술』"
        movie = "《인셉션》"
    elif result == "감정형":
        desc = "💖 감정형 - 공감과 감성 중심, 타인의 감정을 잘 이해합니다."
        book = "『감정 수업』"
        movie = "《이터널 선샤인》"
    elif result == "혼란형":
        desc = "🌀 혼란형 - 걱정이 많고 불안정하지만 내면이 깊습니다."
        book = "『나는 생각이 너무 많아』"
        movie = "《인사이드 아웃》"
    else:
        desc = "🔥 행동형 - 즉흥적이고 도전적인 스타일, 에너지 넘칩니다."
        book = "『기억 전달자』"
        movie = "《포레스트 검프》"

    # 결과 출력
    st.write(desc)
    st.markdown(f"**📚 추천 책:** {book}")
    st.markdown(f"**🎬 추천 영화:** {movie}")

    # 공유용 텍스트
    st.text_area("📤 결과 공유 (복사해서 사용하세요)", f"🧠 나의 심리 유형은 [{result}]!\n\n{desc}\n\n📚 {book}\n🎬 {movie}", height=150)

    # 새로 시작 버튼
    if st.button("🔄 다시 테스트하기"):
        for i in range(len(questions)):
            st.session_state[f"q{i}"] = None
        st.session_state.submitted = False
        st.session_state.answers = []
        st.experimental_rerun()
