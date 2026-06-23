# Streamlit 의 data flow 와 data 가 처리되는 방식

# Streamlit 에선 'widget 에 입력한 data 가 변경'될때 마다 python 파일 '전체'가 다시 실행된다. (py 파일 위에서부터 아래까지 전부 다시 실행)
# 가령 사용자가 무언가를 입력하거나 slider 를 드래그 해서 data 가 변경될때마다 ..

import streamlit as st
import numpy as np
import pandas as pd

import os
import time

from dotenv import load_dotenv
load_dotenv()

print(f'✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...')

# 다양한 입력 widgets 들
#    https://docs.streamlit.io/develop/api-reference/widgets


st.title(time.strftime('%Y-%m-%d %H:%M:%S'))  # 확인해보자, 새로고침도.

model = st.selectbox("Choose your model", ("GPT-3", "GPT-4"))
st.markdown(f"모델: :green[{model}]")

# reload(새로고침, 요청) -> widget 에서 사용자 선택한 내역 리셋됨
# rerun -> widget 에서 사용자 선택한 내역을 기억하여 반영.

# ⭐️ 웹개발자들에겐 미리 말하지만, 
# 이건 React.js 나 flutter 의 동작과는 다릅니다 <- 이들은 화면의 일부분을 업데이트 하는 동작이다.
# streamlit 은 전체 페이지가 refresh(?) 된다.

name = st.text_input("너 이름이 뭐니?")
st.markdown(f"name: :green[{name}]")

if model == "GPT-3":
    st.write("cheap")
else:
    st.write("expensive")
    country = st.text_input("What is your country?")
    st.write(country)

st.markdown("---")

button = st.button('버튼을 누르세요')  # 클릭되면 True 리턴
if button:
    st.write(':blue[버튼] 이 눌렸습니다')

# ---------------------------------------------------
# st.download_button() => bool 리턴
#  버튼을 클릭하면 다운로드

# 파일 다운로드 버튼. 
# 샘플 데이터 생성
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.dataframe(df)

st.download_button(
    label='CSV로 다운로드',
    data=df.to_csv(),
    file_name='sample.csv',
    mime='text/csv',
)

agree = st.checkbox("동의하십니까?")

if agree:
    st.write('동의! 보감! :100:')

mbti = st.radio(
    label="너의 MBTI 는?",
    options=('ISTP', 'ESFP', '선택지 없음'),
    index=2,
)

if mbti == 'ISTP':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ESFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

st.file_uploader(
    "파일선택(csv or excel)",
    type=['csv', 'xls', 'xlsx'],
)

