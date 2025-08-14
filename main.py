import streamlit as st

# MBTI별 데이터
mbti_data = {
    "INTJ": {
        "desc": "전략가형 — 장기적인 계획과 분석을 즐기고 차분한 성격",
        "look": "차가운 첫인상, 깔끔하고 단정한 스타일을 선호",
        "ideal": "지적인 대화가 가능한 사람, 계획적이고 자기 관리 잘하는 사람",
        "image": "https://i.ibb.co/Zc2VNhq/intj.jpg"
    },
    "ENFP": {
        "desc": "재기발랄한 활동가형 — 새로운 경험과 사람을 좋아하는 타입",
        "look": "밝고 활발한 표정, 캐주얼하고 개성 있는 패션",
        "ideal": "함께 웃고 모험할 수 있는 사람, 즉흥적인 데 매력 느끼는 타입",
        "image": "https://i.ibb.co/Jr99sgh/enfp.jpg"
    },
    "INFJ": {
        "desc": "옹호자형 — 깊이 있는 관계와 가치 추구를 좋아하는 타입",
        "look": "잔잔하고 따뜻한 미소, 차분하고 깔끔한 복장",
        "ideal": "마음이 따뜻하고 배려심 깊은 사람, 가치관이 맞는 사람",
        "image": "https://i.ibb.co/Y8s6fjq/infj.jpg"
    },
    "ESTP": {
        "desc": "사업가형 — 에너지 넘치고 현실 감각이 뛰어난 타입",
        "look": "활기찬 표정, 스포츠 스타일이나 스트리트 패션 선호",
        "ideal": "자유롭고 재미있는 사람, 즉흥적인 모험 즐기는 사람",
        "image": "https://i.ibb.co/NnXc7Yw/estp.jpg"
    }
}

st.set_page_config(page_title="MBTI 외모 & 이상형 추천", page_icon="💘", layout="centered")

st.title("💘 MBTI 기반 외모 & 이상형 추천")
st.markdown("MBTI를 선택하면 해당 유형의 특징, 이미지, 이상형을 알려드립니다!")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_data.keys()))

if st.button("결과 보기"):
    data = mbti_data[selected_mbti]
    st.subheader(f"💡 {selected_mbti} — {data['desc']}")
    st.image(data["image"], use_container_width=True)
    st.markdown(f"**외모 특징:** {data['look']}")
    st.markdown(f"**이상형:** {data['ideal']}")
