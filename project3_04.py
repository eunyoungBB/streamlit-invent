import os
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.set_page_config(
      page_title="자동차 diy하기",
      layout="wide"
)
image = Image.open('header.jpg')
st.image(image)
st.header(':mrs_claus: 4. 픽토그램으로 표현하기', divider='rainbow')
st.subheader(':memo: 학습 목표 : ')
st.markdown('#### :white_medium_square: 1. 발명기법을 이용하여 자동차 옵션 아이디어를 발명할 수 있다.')
st.markdown('#### :ballot_box_with_check: 2. 발명품을 픽토그램을 이용하여 표현할 수 있다.')
st.divider()

#autodraw활용하기
st.subheader(':writing_hand: Autodraw 활용하기', divider='violet')
st.markdown("""
            <div style="background-color:lightyellow; padding:10px; border-radius:5px;">
            <h4> Autodraw 란?</h4>
            <p style="font-size:20px;">구글에서 개발한 인공지능 그림 그리기 프로그램으로</p>
            <p style="font-size:20px;">간단한 손그림을 그리면 AI가 유추한 아이콘을 자동으로 생성해주는 편리한 기능을 가짐!</p>
            <p style="font-size:20px;"><a href="https://www.autodraw.com/" target="_blank">https://www.autodraw.com/</a></p>
            </div>
            """, unsafe_allow_html=True)
st.divider()


st.subheader(':writing_hand: 발명아이디어를 픽토그램으로 표현하기', divider='violet')
# 조 이름 입력
group_name = st.text_input('**조 이름을 입력해주세요.**')
# 컨텐츠1(픽토그램), 컨텐츠2(발명아이디어 명칭 입력)
con1, con2 = st.columns([0.5,0.5])
with con2: 
    #  파일 저장하는 함수 정의
    def save_uploaded_file(directory, file):
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(os.path.join(directory, file.name),'wb') as f: 
            f.write(file.getbuffer())
        
        return st.success('파일 업로드 성공')

    # jpg 파일 업로드 부분
    jpg_file = st.file_uploader(':file_folder: **Autodraw로 작업한 파일(.jpg)을 업로드 하세요.**', type = ['jpg','png','jpeg', 'gif', 'bmp'])

with con1: 
    # 발명아이디어 명칭 입력
    invent = st.text_input('**발명아이디어 명칭을 입력하세요:**')
  
# 제출 버튼
image_folder = os.getcwd() + '/img'

# 'img' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 제출 버튼이 눌렸을 때만 파일 리스트를 가져옵니다.
if st.button('탐구 결과 보고', use_container_width = True):
    if jpg_file is None:
        st.warning('파일을 업로드하세요.')
    elif group_name is None or group_name == '':
        st.warning('조 이름을 입력하세요.')
    elif invent is None or invent == '':
        st.warning('명칭을 입력하세요.')
    else:
        filename = group_name + '.jpg'
        jpg_file.name = filename
        invent_name = invent
        save_uploaded_file('img', jpg_file)

        files = os.listdir(image_folder)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        my_range = range(len(image_files))

st.divider()


# 픽토그램 공유하기
st.subheader('픽토그램 공유하기', divider='violet')
cols = st.columns(1)
image_folder = os.getcwd() + '/img'
files = os.listdir(image_folder)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
print(image_files) 
my_range = range(len(image_files))

for i in my_range:
    with cols[i % 1].expander(group_name):
        st.image('img' + '/' + image_files[int(i)], caption = image_files[int(i)])

st.divider()
