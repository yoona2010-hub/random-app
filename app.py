import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 뽑아보세요.")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "마라탕",
    "쌀국수",
    "햄버거",
    "파스타",
    "국밥",
    "비빔밥",
    "부대찌개",
    "샌드위치",
    "라멘",
    "카레",
]

st.divider()

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  # random.choice()를 사용해 리스트에서 무작위로 하나 선택
  selected_menu = random.choice(lunch_menus)

  # 결과 출력 및 축하 효과
  st.success(f"오늘의 추천 메뉴는 **'{selected_menu}'** 입니다! 맛있게 드세요! 😋")
  st.balloons()
