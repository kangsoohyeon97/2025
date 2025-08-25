import streamlit as st

st.set_page_config(page_title="🧠 심리 테스트", layout="centered")
ㅁimport streamlit as st

st.set_page_config(page_title="🌟 심리 테스트", layout="centered")

# CSS 스타일: 모던하고 화려한 느낌
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

body {
    background: linear-gradient(135deg, #6B5B95, #B8A9C9);
    font-family: 'Poppins', sans-serif;
    color: #fff;
}

.title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    margin-top: 30px;
    margin-bottom: 5px;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    letter-spacing: 2px;
    background: linear-gradient(90deg, #FF6A88, #FF99AC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s infinite linear;
}

@keyframes shine {
    0% {
        background-position: 0% 50%;
    }
    100% {
        background-position: 200% 50%;
    }
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 40px;
    color: #eee;
    letter-spacing: 1px;
    font-weight: 600;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
}

.question-card {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 25px 30px;
    margin-bottom: 25px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    transition: transform 0.3s ease;
}

.question-card:hover {
    transform: scale(1.03);
    box-shadow: 0 15px 30px rgba(255, 105, 180, 0.6);
}

.question-text {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 18px;
    color: #fff;
}

.stRadio > div {
    font-size: 16px;
    margin-left: 12px;
    color: #FDEFF9;
}

button[kind="primary"] {
    background: #FF5E7E;
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: 700;
    font-size: 18px;
    border: none;
    box-shadow: 0 8px 15px rgba(255, 94, 126, 0.6);
    transition: background 0.3s ease;
}

button[kind="primary"]:hover {
    background: #FF3A5E;
    box-shadow: 0 12px 25px rgba(255, 58, 94, 0.8);
    cursor: pointer;
}

.result-box {
    background: rgba(255, 255, 255, 0.25);
    border-radius: 25px;
    padding: 30px 40px;
    margin-top: 40px;
    box-shadow: 0 10px 30px rgba(255, 105, 180, 0.6);
    text-align: center;
    color: #fff;
}

.result-title {
    font-size: 38px;
    font-weight: 900;
    margin-bottom: 12px;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
}

.result-desc {
    font-size: 20px;
    margin-bottom: 25px;
    font-weight: 600;
    line-height: 1.3;
}

.recommend {
    font-size: 18px;
    margin: 8px 0;
    font-weight: 700;
    color: #FFD1DC;
}

textarea {
    background: rgba(255, 255, 255, 0.2) !important;
    color: #fff !important;
    border-radius: 15px !important;
    padding: 15px !important;
    font-size: 16px !important;
    font-family: 'Poppins', sans-serif !important;
    border: 1px solid rgba(255, 255, 255, 0.35) !important;
    box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4) !important;
    resize: none !important;
}

.reset-btn {
    background: #FF3A5E !important;
    border-radius: 15px !important;
    padding: 12px 30px !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    border: none !important;
    box-shadow: 0 10px 25px rgba(255, 58, 94, 0.9) !important;
    margin-top: 35px !important;
    transition: background 0.3s ease !important;
}

.reset-btn:hover {
    background: #FF1A3C !important;
    cursor: pointer !important;
}

.footer {
    margin-top: 60px;
    font-size: 14px;
    text-align: center;
    color: #EEE;
    font-style: italic;
    letter-spacing: 1.1px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌟 심리 테스트</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">솔직하게 답변하고 내 마음 스타일을 알아보세요!</div>', unsafe_allow_html=True)

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = [None]*5

scores = {
    "분석형": 0,
    "감정형": 0,
    "혼란형": 0,
    "행동형": 0,
}

questions = [
    {
        "question": "1. 누군가 고민을 이야기하면 나는?",
        "options": {
            "해결 방법을 제시한다.": "분석형",
            "감정에 공감하고 위로한다.": "감정형",
            "괜히 불안해져서 같이 걱정한다.": "혼란형",
            "이야기를 빨리 넘기고 다른 걸 한다.": "행동형",
        },
    },
    {
        "question": "2. 갑작스러운 일정 변경이 생기면?",
        "options": {
            "계획을 다시 정리한다.": "분석형",
            "상대방의 입장을 생각한다.": "감정형",
            "스트레스를 크게 받는다.": "혼란형",
            "그냥 적응한다. 문제없다.": "행동형",
        },
    },
    {
        "question": "3. 낯선 사람들과의 모임에서는?",
        "options": {
            "대화를 관찰하며 분석한다.": "분석형",
            "감정을 나누려 노력한다.": "감정형",
            "긴장되고 불편하다.": "혼란형",
            "즐기며 주도적으로 나선다.": "행동형",
        },
    },
    {
        "question": "4. 스트레스를 받았을 때 나는?",
        "options": {
            "조용히 정리하고 생각한다.": "분석형",
            "누군가에게 털어놓는다.": "감정형",
            "예민해지고 걱정이 많아진다.": "혼란형",
            "운동하거나 뭔가를 해버린다.": "행동형",
        },
    },
    {
        "question": "5. 결정을 내려야 할 때 나는?",
        "options": {
            "이유와 근거를 따진다.": "분석형",
            "기분과 감정에 따른다.": "감정형",
            "망설이고 걱정이 앞선다.": "혼란형",
            "그냥 느낌대로 행동한다.": "행동형",
        },
    },
]

for i, q in enumerate(questions):
    st.markdown(f'<div class="question-card"><div class="question-text">{q["question"]}</div></div>', unsafe_allow_html=True)
    options_list = list(q["options"].keys())
    default_index = 0
    if st.session_state.answers[i] in options_list:
        default_index = options_list.index(st.session_state.answers[i])

    ans = st.radio("", options_list, index=default_index, key=f"q{i}")
    st.session_state.answers[i] = ans

if st.button("🔍 결과 보기", key="submit_button") and not st.session_state.submitted:
    st.session_state.submitted = True
    for i, q in enumerate(questions):
        category = q["options"][st.session_state.answers[i]]
        scores[category] += 1

    result = max(scores, key=scores.get)

    descriptions = {
        "분석형": ("🎯 분석형", "논리적이고 계획적인 타입이에요.", "『논리의 기술』", "《인셉션》"),
        "감정형": ("💖 감정형", "감정을 잘 이해하고 공감하는 스타일입니다.", "『감정 수업』", "《이터널 선샤인》"),
        "혼란형": ("🌀 혼란형", "걱정이 많고 내면이 깊어요.", "『나는 생각이 너무 많아』", "《인사이드 아웃》"),
        "행동형": ("🔥 행동형", "즉흥적이고 에너지 넘치는 스타일입니다.", "『기억 전달자』", "《포레스트 검프》"),
    }

    title, desc, book, movie = descriptions[result]

    st.markdown(f'''
        <div class="result-box">
            <div class="result-title">{title}</div>
            <div class="result-desc">{desc}</div>
            <div class="recommend">📚 추천 책: {book}</div>
            <div class="recommend">🎬 추천 영화: {movie}</div>
        </div>
    ''', unsafe_allow_html=True)

    share_text = f"나의 심리 유형은 [{result}]!\n\n{desc}\n\n📚 {book}\n🎬 {movie}"
    st.text_area("📤 결과 공유 (복사해서 사용하세요)", share_text, height=150)

if st.button("🔄 다시 시작하기", key="reset_button"):
    st.session_state.submitted = False
    st.session_state.answers = [None] * len(questions)
    st.experimental_rerun()

st.markdown('<div class="footer">© 2025 심리 테스트 앱 - 재미로만 즐겨주세요!</div>', unsafe_allow_html=True)

# 스타일 꾸미기 (간단한 CSS)
st.markdown("""
    <style>
    .title {
        font-size: 38px;
        font-weight: 700;
        color: #4B0082;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        color: #6A5ACD;
        text-align: center;
        margin-bottom: 30px;
    }
    .question {
        font-size: 20px;
        font-weight: 600;
        color: #483D8B;
        margin-top: 20px;
    }
    .result {
        background: #E6E6FA;
        border-radius: 15px;
        padding: 20px;
        margin-top: 30px;
        font-size: 18px;
        color: #2F4F4F;
        box-shadow: 3px 3px 8px #B0C4DE;
    }
    .recommend {
        margin-top: 15px;
        font-weight: 600;
        color: #4B0082;
    }
    .footer {
        margin-top: 50px;
        font-size: 12px;
        color: #999999;
        text-align: center;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# 제목 & 부제목
st.markdown('<div class="title">🧠 나만의 심리 유형 테스트</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">아래 질문에 답하고 내 심리 스타일을 알아봐요!</div>', unsafe_allow_html=True)

# 세션 상태 초기화
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = [None]*5

scores = {
    "분석형": 0,
    "감정형": 0,
    "혼란형": 0,
    "행동형": 0
}

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

# 질문 출력 및 답변 저장
for i, q in enumerate(questions):
    st.markdown(f'<div class="question">{q["question"]}</div>', unsafe_allow_html=True)
    ans = st.radio("", list(q["options"].keys()), index=questions[i]["options"].keys().index(st.session_state.answers[i]) if st.session_state.answers[i] else 0, key=f"q{i}")
    st.session_state.answers[i] = ans

# 결과 버튼 및 처리
if st.button("🔍 결과 보기") and not st.session_state.submitted:
    st.session_state.submitted = True

    for i, q in enumerate(questions):
        category = q["options"][st.session_state.answers[i]]
        scores[category] += 1

    result = max(scores, key=scores.get)

    # 결과별 설명과 추천
    descriptions = {
        "분석형": ("🎯 분석형", "논리적이고 계획적인 성향이에요.", "『논리의 기술』", "《인셉션》"),
        "감정형": ("💖 감정형", "감정을 잘 이해하고 공감하는 타입입니다.", "『감정 수업』", "《이터널 선샤인》"),
        "혼란형": ("🌀 혼란형", "걱정이 많고 내면이 깊어요.", "『나는 생각이 너무 많아』", "《인사이드 아웃》"),
        "행동형": ("🔥 행동형", "즉흥적이고 에너지가 넘치는 스타일입니다.", "『기억 전달자』", "《포레스트 검프》"),
    }

    title, desc, book, movie = descriptions[result]

    st.markdown(f'<div class="result"><h2>{title}</h2><p>{desc}</p>'
                f'<p class="recommend">📚 추천 책: {book}</p>'
                f'<p class="recommend">🎬 추천 영화: {movie}</p></div>', unsafe_allow_html=True)

    share_text = f"나의 심리 유형은 [{result}]!\n\n{desc}\n📚 {book}\n🎬 {movie}"
    st.text_area("📤 결과 공유 (복사해서 사용하세요)", share_text, height=150)

# 다시하기 버튼 (항상 보이도록)
if st.button("🔄 다시 테스트하기"):
    st.session_state.submitted = False
    st.session_state.answers = [None]*len(questions)
    st.experimental_rerun()

st.markdown('<div class="footer">※ 이 테스트는 재미로 하는 심리 테스트입니다.</div>', unsafe_allow_html=True)
