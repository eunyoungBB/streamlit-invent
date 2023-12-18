import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.set_page_config(
      page_title="자동차 diy하기",
      layout="wide"
)
image = Image.open('header.jpg')
st.image(image)
st.header(':mrs_claus: 1. 픽토그램', divider='rainbow')
st.subheader(':memo: 학습 목표 : ')
st.markdown('#### :white_medium_square: 1. 발명기법을 이용하여 자동차 옵션 아이디어를 발명할 수 있다.')
st.markdown('#### :ballot_box_with_check: 2. 발명품을 픽토그램을 이용하여 표현할 수 있다.')
st.divider()


st.subheader('::writing_hand: 도쿄올림픽 픽토그램 영상시청', divider='violet')
# YouTube 동영상 추가
video_url = 'https://www.youtube.com/watch?v=clsiu7DaIcg'
st.video(video_url)
st.divider()

# 발문하기
st.subheader(':writing_hand: 생각해보기: 픽토그램이란?', divider='violet')
with st.form(key='my_form'):
    student_result = st.text_input("#### **영상을 보고 픽토그램에 대해 한줄로 정리해보세요!** :blush:")

    if st.form_submit_button('제출'):
        st.write(f"#### {student_result} (이)라고 생각했군요!")
        st.write("#### 픽토그램은 그림(picture)과 전보(telegram)의 합성어로")
        st.write("#### 정보를 알리기 위해 문자를 사용하지 않고도 이해할 수 있도록 조합한 그림입니다.:clap:")
st.divider()

#픽토그램 도감 만들기
st.subheader(':writing_hand: 자주쓰이는 픽토그램에는 어떤 것들이 있을까요?', divider='violet')
pokemons = [
    {
        "name": "비상구",
        "image_url": "https://i.namu.wiki/i/7ok3yBPJ8OqD4ZunyEGDqdz3k4CKYGslsnAqjaIQrSdheFsPTX_fC9bgq8d7kKxKBNaLe7PmVN4eQzjneBvzfG8h2Pp51EhDvowSDdy7eT6lypYxA1FbSQEkLDKrzNvd-I0CabNKhNP4bgRL25p15A.svg"
    },
    {
        "name": "화장실",
        "image_url": "https://i.namu.wiki/i/8jQzEf4NgK5Qr-oLaJucPJFEpTOEKCILn3B1BYcw8UW43KBrcXZt0wIMfpIPDqkFIhCCBJ7e8i5a0M7c5mBSdAMztXrKdLSmJL5tUuFDHOu2yBOGRxFISXS0E2gft3McPmMh7KT-Dh_K6BCItPOgzA.svg",
    },
    {
        "name": "금연",
        "image_url": "https://thumb.ac-illust.com/7e/7e7c78061a774d01e972ee00d0bff891_t.jpeg",
    },
    {
        "name": "소화기",
        "image_url": "https://us.123rf.com/450wm/lcosmo/lcosmo1607/lcosmo160700001/59714330-%ED%94%BD%ED%86%A0%EA%B7%B8%EB%9E%A8-%EB%B9%A8%EA%B0%84%EC%83%89-%EC%8B%A0%ED%98%B8-%EC%86%8C%ED%99%94%EA%B8%B0-%ED%99%94%EC%83%81-%EC%BB%A4%EB%AE%A4%EB%8B%88%EC%BC%80%EC%9D%B4%EC%85%98-%EC%9E%AC%EB%A3%8C-%EB%B0%8F-%EC%95%88%EC%A0%84-%EB%B0%8F-%ED%99%94%EC%9E%AC-%EC%98%88%EB%B0%A9%EC%97%90.jpg"
    },
    {
        "name": "안전밸트",
        "image_url": "https://www.shutterstock.com/image-vector/seat-belt-icon-260nw-725209042.jpg"
    },
    {
        "name": "경고",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1OVeas4sakAq2aBp1zHWA14LtxAwIhkSmhA&usqp=CAU"
    }
]
for i in range(0, len(pokemons), 3):
    row_pokemons = pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"#### **{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
st.divider()

# 선택형문항
st.subheader(':writing_hand: 픽토그램의 특징으로 맞는 것을 "모두" 고르시오.', divider='violet')

options = ['##### **1. 쉽고 빠른 정보전달이 가능하다.**', '##### **2. 국가별로 통용되는 기호가 다르다.**', '##### **3. 픽토그램에서 색은 큰 의미가 없다.**', '##### **4. 단순 명료한 의미를 가진다.**', '##### **5. 사람들이 알아볼 수 있는 사실적이고 자세한 그림이다.**']
correct_answers = [options[0], options[3]]
answers = []
for i, option in enumerate(options):
    answers.append(st.checkbox(option))

if st.button('제출하기'):
    if [answers[i] for i in [0, 3]] == [True, True] and sum(answers) == 2:
        st.markdown("""
            <div style="background-color:lightblue; padding:10px; border-radius:5px;">
            <h4>정답입니다! &#128079; &#128079; &#128079;</h4>
            <p style="font-size:20px;">픽토그램은 쉽고 빠르게 정보전달을 할 수 있으며,</p>
            <p style="font-size:20px;">단순 명료한 의미를 가지며,</p>
            <p style="font-size:20px;">세계 공용으로 사용가능 하다는 특징을 가지고 있어요.&#128515;</p>
            </div>
            """, unsafe_allow_html=True)
        st.divider()
        st.subheader(':mrs_claus: 이러한 픽토그램이 특징을 이용하여 자동차 옵션을 발명하고 이를 픽토그램으로 만들어볼까요?')
    else:
        st.write('#### 오답입니다. 다시 시도해보세요.:disappointed_relieved:')
st.divider()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("project3_01.py", "1. 픽토그램이란?"),
        Page("project3_02.py", "2. 자동차 option이란?"),
        Page("project3_03.py", "3. 자동차 옵션 아이디어 발명하기"),
        Page("project3_04.py", "4. 픽토그램으로 표현하기") 
    ]
)

