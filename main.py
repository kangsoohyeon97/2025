import streamlit as st

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "desc": "전략가형 — 장기적인 계획과 분석을 즐기는 타입",
        "hobbies": ["전략 보드게임", "독서", "개인 프로젝트 개발", "투자 분석"],
        "image": "https://i.ibb.co/Zc2VNhq/intj.jpg"
    },
    "ENFP": {
        "desc": "재기발랄한 활동가형 — 새로운 경험과 사람을 좋아하는 타입",
        "hobbies": ["여행", "연극", "창작 활동", "사교 모임"],
        "image": "https://i.ibb.co/Jr99sgh/enfp.jpg"
    },
    "ISTP": {
        "desc": "장인형 — 손으로 무언가 만드는 걸 좋아하는 타입",
        "hobbies": ["등산", "자동차 튜닝", "낚시", "드론 조종"],
        "image": "https://i.ibb.co/jwtsMxB/istp.jpg"
    },
    "INFJ": {
        "desc": "옹호자형 — 깊이 있는 관계와 가치 추구를 좋아하는 타입",
        "hobbies": ["일기 쓰기", "명상", "봉사활동", "예술 감상"],
        "image": "https://i.ibb.co/Y8s6fjq/infj.jpg"
    },
    "ESFP": {
        "desc": "자유로운 영혼형 — 지금 이 순간을 즐기는 타입",
        "hobbies": ["콘서트 가기", "댄스", "요리", "여행"],
        "image": "https://i.ibb.co/mb0CJXM/esfp.jpg"
    }
}

st.set_page_config(page_title="MBTI 취미 추천", page_icon="🎯", layout="centered")

st.title("🎯 MBTI 기반 취미 추천")
st.markdown("당신의 MBTI를 검색하거나 선택하세요!")

# 검색 기능
search_query = st.text_input("MBTI 검색 (예: ENFP)").upper()

# MBTI 선택 박스
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("또는 MBTI 선택", mbti_list)

# 검색 우선
if search_query in mbti_data:
    selected_mbti = search_query

# 버튼 클릭 시 결과 표시
if st.button("취미 추천 받기"):
    if selected_mbti in mbti_data:
        data = mbti_data[selected_mbti]
        st.subheader(f"💡 {selected_mbti} — {data['desc']}")
        st.image(data["image"], use_container_width=True)
        st.markdown("**추천 취미:**")
        for hobby in data["hobbies"]:
            st.write(f"- {hobby}")
    else:
        st.warning("해당 MBTI 데이터가 없습니다.")
