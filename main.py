import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💞", layout="centered")

# CSS 스타일 (카드 디자인)
st.markdown("""
    <style>
    .result-card {
        background-color: #fff5f8;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff99b3;
        box-shadow: 2px 2px 10px rgba(255, 153, 179, 0.3);
        margin-top: 20px;
    }
    .celeb {
        font-weight: bold;
        color: #ff4d6d;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 궁합 + 이상형 연예인 데이터
compatibility_data = {
    ("INTJ", "ENFP"): {
        "score": 5,
        "desc": "서로 다른 성향이 잘 맞는 궁합! 계획적인 INTJ와 자유로운 ENFP가 좋은 균형을 만듭니다.",
        "ideal_celeb": "박보검, 아이유"
    },
    ("ENFP", "INFJ"): {
        "score": 4,
        "desc": "깊이 있는 대화를 즐기며 서로의 가치관을 존중하는 이상적인 관계.",
        "ideal_celeb": "수지, 공유"
    },
    ("ISTJ", "ESFP"): {
        "score": 3,
        "desc": "서로의 차이를 이해하면 보완이 가능한 궁합.",
        "ideal_celeb": "이승기, 손예진"
    },
    ("ENTP", "ENTP"): {
        "score": 2,
        "desc": "재미는 있지만 서로 너무 비슷해 금방 질릴 수 있습니다.",
        "ideal_celeb": "유재석, 김고은"
    }
}

# 타이틀
st.markdown("<h1 style='text-align: center; color: #ff4d6d;'>💞 MBTI 궁합 테스트 💞</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>두 사람의 MBTI를 선택하면 궁합과 이상형 연예인을 알려드립니다!</p>", unsafe_allow_html=True)

# MBTI 선택
mbti_list = sorted(set([mb]()_
