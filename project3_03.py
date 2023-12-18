import os
import streamlit as st
from PIL import Image

# 세션 상태를 관리하는 클래스
class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

# 세션 상태를 가져오는 함수
def get_state(**kwargs):
    if not hasattr(st, '_session_state'):
        st._session_state = SessionState(**kwargs)
    return st._session_state

state = get_state(submissions=[])

st.set_page_config(
      page_title="자동차 diy하기",
      layout="wide"
)
image = Image.open('header.jpg')
st.image(image)

st.header(":santa: 3.편리한 자동차 발명하기", divider='rainbow')
st.subheader(':memo: 학습 목표 : ')
st.markdown('#### :ballot_box_with_check: 1. 발명기법을 이용하여 자동차 옵션 아이디어를 발명할 수 있다.')
st.markdown('#### :white_medium_square: 2. 발명품을 픽토그램을 이용하여 표현할 수 있다.')
st.divider()

#발명정의
st.subheader(':writing_hand: 발명이란?', divider='violet')
st.markdown("""
            <div style="background-color:lightpink; padding:10px; border-radius:5px;">
            <p style="font-size:20px;">창의적인 아이디어와 기술적인 방법을 이용하여 이전에 없었던</p>
            <p style="font-size:20px;">새로운 것을 만드는 것.</p>
            </div>
            """, unsafe_allow_html=True)
st.divider()

# YouTube 동영상 추가
st.subheader('::writing_hand: 발명기법영상 시청하기', divider='violet')
video_url = 'https://www.youtube.com/watch?v=NCdKGJ0b0nY'
st.video(video_url)
st.divider()

# 발문하기
st.subheader(':writing_hand: 발명계획서 작성하기', divider='violet')
group_name = st.text_input('##### **명칭을 입력해주세요.**')
method = st.text_input('##### **어떠한 기법을 이용했나요?**')
character = st.text_input('##### **특징을 입력하세요.**')

if st.button('발명완료', use_container_width = True):
    if group_name and method and character:
        state.submissions.append((group_name, method, character))
        st.success('발명 계획서가 제출되었습니다.')
    else:
        st.warning('모든 빈칸을 채워주세요.')

st.divider()

st.subheader(':writing_hand: 발명 결과 ', divider='violet')

for i in range(0, len(state.submissions), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(state.submissions):
            group_name, method, character = state.submissions[i + j]
            with cols[j]:
                st.write(f"명칭: {group_name}")
                st.write(f"기법: {method}")
                st.write(f"특징: {character}")

st.divider()