import streamlit as st
st.set_page_config(page_title = "Trắc nghiệm tính cách", page_icon = ":question:",layout = "wide")


col1,col2, col3, col4, col5 = st.columns(5)
col6,col7 = st.columns([2,1])

with col1:
    b1 =st.button("Con mèo")
with col2:
    b2 = st.button("Con chó")
with col3:
    b3 = st.button("Con khỉ")
with col4:
    b4 = st.button("Đại bàng")
with col5:
    b5 = st.button("Con gà")

if b1:
   
    with col6:
        st.write("Âm thanh")
        audio = open('assets/cat.mp3','rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=oFGz1kcRPfY'
        st.video(video,format = 'video/mp4')
    with col7:
        image = 'assets/cat.jpg'
        st.image(image,caption = "Con mèo")
        
if b2:
    
    with col6:
        st.write("Âm thanh")
        audio = open('assets/dog.mp3','rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=hPzfZvpoW4A'
        st.video(video,format = 'video/mp4')
    with col7:
        image = 'assets/dog.jpg'
        st.image(image,caption = "Con chó")
if b3:
   
    with col6:
        st.write("Âm thanh")
        audio = open('assets/monkey.mp3','rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=8d3z4QpUnrQ'
        st.video(video,format = 'video/mp4')
    with col7:
        image = 'assets/monkey.jpg'
        st.image(image,caption = "Con khỉ")
if b4:
    with col6:
        st.write("Âm thanh")
        audio = open('assets/eagle.mp3','rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=T7pk7f649qU'
        st.video(video,format = 'video/mp4')
    with col7:
        image = 'assets/eagle.jpg'
        st.image(image,caption = "Đại bàng")
if b5:
    with col6:
        st.write("Âm thanh")
        audio = open('assets/chicken.mp3','rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=a0ZBh_ggwJk'
        st.video(video,format = 'video/mp4')
    with col7:
        image = 'assets/chicken.jpg'
        st.image(image,caption = "Con gà")
with st.sidebar:
    st.title("Trắc nghiệm tính cách:")
    if b1:
        st.write("con vật bạn chọn là con mèo")
    if b2:
        st.write("con vật bạn chọn là con chó")
    if b3:
        st.write("con vật bạn chọn là con sư tử")
    if b4:
        st.write("con vật bạn chọn là con ngựa")
    if b5:
        st.write("con vật bạn chọn là thiên nga")
            

        
