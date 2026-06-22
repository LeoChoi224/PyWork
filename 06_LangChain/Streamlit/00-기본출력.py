# 간단한 프로토타입(간단한 동작 체크용으로 유용)
import streamlit as st

import numpy as np
import pandas as pd

import os
import time

from dotenv import load_dotenv
load_dotenv()

print(f'✅ {os.path.basename( __file__ )} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')  # 실행파일명, 현재시간출력
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...') # 필요한 환경변수

st.title('기본출력')
st.title('스마일:sunglasses:')

st.header('헤더 입력 가능! :sparkles:')
st.subheader('이것은 subheader')

st.text('일반 텍스트')
st.caption('캡션도 넣을 수 있다.')

sample_code = '''
def function():
    print('hello streamlit')
'''

st.text(sample_code)
st.code(sample_code)

st.markdown("streamlit 은 **마크 다운 문법 지원** 합니다.")
st.markdown("텍스트 색상을 :green[초록색]으로, **:blue[파란색]**")
st.markdown(r"$\sqrt{x^2+y^2}$ LaTex 문법 수식 표현")
st.latex("\sqrt{x^2+y^2}")
st.markdown("---")

st.title("Dataframe, Metric")

# DataFrame 생성
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.dataframe(df)
st.table(df)

st.metric(label="온도", value="10도", delta="1.2도")
st.metric(label="삼성전자", value="201,000원", delta="-23,000원")

st.markdown('---')
st.title('write()')

st.write('hello')
st.write(10, 20, 30)
st.write([1, 2, 3, 4])
st.write({'x' : 100, 'y' : 200})

import re
st.write(re)

# streamlit 의 magic
[100, 200, 300, 400]
"홍묵 " * 4

