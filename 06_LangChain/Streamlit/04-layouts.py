import streamlit as st
import os
import time

import numpy as np

from dotenv import load_dotenv
load_dotenv()


print(f'✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...')

st.title('layout')

# layout
#  streamlit 에서 제공하는 다양한 레이아웃
#  공식: https://docs.streamlit.io/develop/api-reference/layout  (◀ 함 보자!)

# ────────────────────────────────────────────────────────

# 레이아웃 사용방식
# 방식1
cont = st.container(border=True)
cont.write('container 내부')
cont.markdown('container 내부의 markdown')

st.write('홍무기')
cont.write('민재')

# 방식2 : (추천) with 사용
with st.container(border=True):
    st.write('컨테이너 안 입니다')
    st.bar_chart(np.random.randn(50, 3))


# container vs. empty
# container() : 여러 요소들을 담는다
# empty() : 한개의 요소만 담는다.

with st.empty():
    st.write("이민재")
    st.write("최홍묵")

with st.sidebar:
    st.title('sidebar')
    st.text_input('홍묵이 어디갔지?')


st.title("tabs")
tab_one, tab_two, tab_three = st.tabs(['희준', '정준', '하석'])

with tab_one:
    st.subheader('alpha')

with tab_two:
    st.subheader('bravo')

with tab_three:
    st.subheader('charlie')

