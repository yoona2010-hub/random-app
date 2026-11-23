import streamlit as st
import pandas as pd

# 1. 초기 데이터 구성
type_performance = [
    ['겨울왕국', 0, '19만원'],
    ['레베카', 27, '15만원'],
    ['오페라의 유령', 116, '17만원']
]

# 2. 예매 함수 (def 및 if 조건문)
def def_performance(pfm_name, ticket):
    for pfm in type_performance:
        if pfm[0] == pfm_name:
            sit = pfm[1]
            if sit <= 0:
                st.error("이 공연의 티켓은 전부 매진 되었습니다.")
            else:
                pfm[1] = sit - ticket
                st.success(f"{pfm_name} {ticket}매 예매 완료")

# 3. 처음 화면 (입력)
selected_pfm = st.text_input("공연선택:[공연목록:겨울왕국 / 레베카 / 오페라의 유령]")
ticket_num = st.number_input("공연티켓 갯수 입력:[1~300개까지]", min_value=1, max_value=300, step=1)

# 4. 버튼을 눌렀을 때만 결과 화면 등장
if st.button("예매하기"):
    # 함수 실행
    def_performance(selected_pfm, ticket_num)

    # for문 순회 후 데이터프레임 전환
    df_data = []
    for item in type_performance:
        df_data.append({
            '공연명': item[0],
            '남은좌석의 갯수': item[1],
            '공연금액': item[2]
        })

    df = pd.DataFrame(df_data)

    # 결과 표 출력
    st.table(df)
