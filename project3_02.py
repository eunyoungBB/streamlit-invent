import streamlit as st
from PIL import Image
print("page reload")


st.set_page_config(
      page_title="자동차 diy하기",
      layout="wide"
)
image = Image.open('header.jpg')
st.image(image)

st.header(":santa: 2.자동차 내부 버튼의 의미?!", divider='rainbow')
st.subheader(':memo: 학습 목표 : ')
st.markdown('#### :ballot_box_with_check: 1. 발명기법을 이용하여 자동차 옵션 아이디어를 발명할 수 있다.')
st.markdown('#### :white_medium_square: 2. 발명품을 픽토그램을 이용하여 표현할 수 있다.')
st.divider()

#자동차 옵션정의
st.subheader(':writing_hand: 자동차 option', divider='violet')
st.markdown("""
            <div style="background-color:lightyellow; padding:10px; border-radius:5px;">
            <p style="font-size:20px;">자동차 옵션이란 자동차를 살 때 선택이 가능한 추가품목을 말합니다.</p>
            <p style="font-size:20px;">이러한 옵션들은 우리를 안전하고 편리하게 만들어 주고 기술이 발전하면서 기능은 더욱 다양해지고 강화되고 있습니다.</p>
            <p style="font-size:20px;">우리의 삶을 더욱 풍요롭게 만드는 옵션들은 어떤 것이 있을까요?&#128515;</p>
            </div>
            """, unsafe_allow_html=True)
st.divider()

# 옵션도감
st.subheader(':writing_hand: 자동차 내부 버튼들의 의미를 알아보자', divider='violet')

initial_pokemons = [
    {
        "name": "에어컨",
        "character" : "온도를 조절해줌",
        "image": './image/에어컨.jpeg'
    },  
    {
        "name": "비상등",
        "character" : "비상상황, 방어운전, 매너 운전 시 표기",
        "image": './image/비상등.jpeg'
    },
    {
        "name": "김서림방지",
        "character" : "앞 유리의 김서림을 제거해 줌",
        "image": './image/김서림방지.jpeg'
    },
    {
        "name": "핸들열선",
        "character" : "겨울철 손시려울 때 핸들을 따뜻하게 만들어줌",
        "image": './image/핸들열선.jpeg'
    },
    {
        "name": "엉뜨",
        "character" : "좌석 시트에 따뜻한 열이 올라옴",
        "image": './image/엉뜨.jpeg'
    },
      {
        "name": "엉차",
        "character" : "좌석 시트가 시원하게 쿨링됨",
        "image": './image/엉차.jpeg'
    },
    {
        "name": "크루즈컨트롤",
        "character" : "패달밟지 않아도 속도 자동 조절",
        "image": './image/크루즈컨트롤.jpeg'
    },
    {
        "name": "주차보조",
        "character" : "차량 전,후방 센서 일정거리 물체 감지 후 경고해주는 기능",
        "image": './image/후방보조.jpeg'
    },
    {
        "name": "오토홀드",
        "character" : "정차 시 브레이크 잡아주는 기능",
        "image": './image/오토홀드.jpeg'
    },
    {
        "name": "sync",
        "character" : "독립 설정 가능한 에어컨 온도를 모두 같이 조절할 수 있음",
        "image": './image/SYNC.jpeg'
    },
    {
        "name": "SHIFT LOCK",
        "character" : "시동 꺼진 상태에서 변속레버 바꿈 기능(이중주차 꿀버튼)",
        "image": './image/SHIFT LOCK.jpeg'
    },
]

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i + 3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"#### **{i + j + 1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image"])
                st.markdown(f"###### {pokemon['character']}")
st.divider()

def save_image(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        extension = uploaded_file.name.split('.')[-1]
        filename = f'./image/{uploaded_file.name}'
        image.save(filename)
        return filename
    except Exception as e:
        print(f"Error saving image file: {e}")
        return None
        
# 옵션 추가하기
st.subheader(':writing_hand: 이 외에도 우리 가족차에 있는 옵션 추가하기', divider='violet')
with st.form(key="form"):
    name = st.text_input(label="이름")
    character = st.text_input(label="특징")
    image = st.file_uploader('이미지파일을 업로드 하세요', type = ['png', 'jpg', 'jpeg', 'gif', 'bmp'])
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("이름을 입력해주세요.")
        else:
            # 이미지 파일이 업로드되었는지 확인합니다.
            if image:
                # 이미지 파일을 저장하고, 저장된 파일의 경로를 가져옵니다.
                image_path = save_image(image)
            else:
                image_path = "./image/default.png"
            
            # 새로운 옵션을 추가합니다.
            st.session_state.pokemons.append({
                "name": name,
                "character": character,
                "image": image_path
            })
            
            # 옵션도감을 갱신합니다.
            st.experimental_rerun()
st.divider()