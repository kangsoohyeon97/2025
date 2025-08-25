import streamlit as st

st.set_page_config(page_title="🌟 심리 테스트", layout="centered")

# CSS 스타일: 어두운 배경 + 가독성 높은 글씨 + 모던한 느낌
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

body {
    background: #1e1e2f;
    font-family: 'Poppins', sans-serif;
    color: #e0e0e0;
    margin: 0 10%;
}

.title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 10px;
    color: #ff6584;
    text-shadow: 1.5px 1.5px 8px #65001a;
    letter-spacing: 3px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 45px;
    color: #aaa;
    font-weight: 600;
}

.question-card {
    background: #2a2a40;
    border-radius: 20px;
    padding: 25px 35px;
    margin-bottom: 28px;
    box-shadow: 0 8px 18px rgba(255, 101, 132, 0.35);
    transition: transform 0.3s ease;
    border: 1px solid #ff6584;
}

.question-card:hover {
    transform: scale(1.04);
    box-shadow: 0 15px 30px rgba(255, 101, 132, 0.7);
}

.question-text {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #ff7a9e;
}

.stRadio > div {
    font-size: 17px;
    margin-left: 12px;
    color: #ffd1dc;
}

button[kind="primary"] {
    background: #ff6584;
    border-radius: 15px;
    padding: 14px 30px;
    font-weight: 700;
    font-size: 20px;
    border: none;
    box-shadow: 0 8px 18px rgba(255, 101, 132, 0.6);
    transition: background 0.3s ease;
}

button[kind="primary"]:hover {
    background: #ff3a60;
    box-shadow: 0 12px 28px rgba(255, 58, 96, 0.85);
    cursor: pointer;
}

.result-box {
    background: #2c2c44;
    border-radius: 25px;
    padding: 35px 50px;
    margin-top: 50px;
    box-shadow: 0 12px 35px rgba(255, 101, 132, 0.85);
    text-align: center;
    color: #ffe6eb;
}

.result-title {
    font-size: 42px;
    font-weight: 900;
    margin-bottom: 18px;
    color: #ff6584;
    text-shadow: 2px 2px 10px #66001c;
}

.result-desc {
    font-size: 20px;
    margin-bottom: 25px;
    font-weight: 600;
    line-height: 1.5;
    color: #ffd1dc;
}

.recommend {
    font-size: 19px;
    margin: 12px 0 6px;
    font-weight: 700;
    color: #ff99b3;
}

.recommend-desc {
    font-size: 16px;
    margin-bottom: 15px;
    color: #ffc9d6;
    font-style: italic;
}

textarea {
    background: #3a3a58 !important;
    color: #ffe6eb !important;
    border-radius: 15px !important;
    padding: 18px !important;
    font-size: 16px !important;
    font-family: 'Poppins', sans-serif !important;
    border: 1px solid #ff6584 !important;
    box-shadow: 0 6px 20px rgba(255, 101, 132, 0.6) !important;
    resize: none !important;
}

.reset-btn {
    background: #ff3a60 !important;
    border-radius: 18px !important;
    padding: 14px 35px !important;
    font-weight: 700 !important;
    font-size: 20px !important;
    border: none !important;
    box-shadow: 0 12px 28px rgba(255, 58, 96, 0.9) !important;
    margin-top: 45px !important;
    transition: background 0.3s ease !important;
}

.reset-btn:hover {
    background: #ff1a43 !important;
    cursor: pointer !important;
}

.footer {
    margin-top: 75px;
    font-size: 15px;
    text-align: center;
    color: #ccc;
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
        "분석형": (
            "🎯 분석형", 
            "논리적이고 계획적인 타입이에요. 상황을 체계적으로 분석하고 문제를 해결하는 데 뛰어납니다.",
            "『논리의 기술』 - 논리적 사고력을 키우는 책으로, 문제 해결에 도움이 됩니다.",
            "《인셉션》 - 꿈속에서 꿈을 조작하는 복잡한 스토리와 논리적 사고가 돋보이는 영화입니다."
        ),
        "감정형": (
            "💖 감정형", 
            "감정을 잘 이해하고 공감하는 스타일입니다. 주변 사람들과 깊은 유대감을 형성합니다.",
            "『감정 수업』 - 감정을 이해하고 조절하는 법을 배우는 데 도움이 되는 책입니다.",
            "《이터널 선샤인》 - 감정의 깊이를 다룬 사랑 이야기로 마음을 울리는 영화입니다."
        ),
        "혼란형": (
            "🌀 혼란형", 
            "걱정이 많고 내면이 깊어요. 불안한 상황에서도 자신을 이해하려 노력합니다.",
            "『나는 생각이 너무 많아』 - 생각이 많아 고민하는 이들을 위한 책입니다.",
            "《인사이드 아웃》 - 감정의 다양한 면을 귀엽고 감동적으로 그린 애니메이션입니다."
        ),
        "행동형": (
            "🔥 행동형", 
            "즉흥적이고 에너지 넘치는 스타일입니다. 어려움 앞에서도 빠르게 대처합니다.",
            "『기억 전달자』 - 행동과 선택에 관한 생각을 깊게 할 수 있는 책입니다.",
            "《포레스트 검프》 - 다양한 삶의 순간들을 즉흥적으로 살아내는 주인공의 이야기입니다."
        ),
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
    st.text_area("📤 결과 공유 (복사해서 사용하세요)", share_text, height=170)

if st.button("🔄 다시 시작하기", key="reset_button", help="테스트를 초기화하고 다시 시작합니다."):
    st.session_state.submitted = False
    st.session_state.answers = [None] * len(questions)
    st.experimental_rerun()

st.markdown('<div class="footer">© 2025 심리 테스트 앱 - 재미로만 즐겨주세요!</div>', unsafe_allow_html=True)
