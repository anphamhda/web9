import streamlit as st
import os

def get_asset_path(filename):
    """
    Trả về đường dẫn tuyệt đối đến tệp trong thư mục 'assets',
    bất kể nơi gọi hàm đang ở đâu.
    
    :param filename: Tên tệp cần truy cập trong thư mục 'assets'
    :return: Đường dẫn tuyệt đối đến tệp trong thư mục 'assets'
    """
    # Lấy đường dẫn tuyệt đối đến thư mục chứa script hiện tại
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Xây dựng đường dẫn đến thư mục 'assets' và tệp cụ thể
    asset_dir = os.path.join(script_dir, 'assets')
    
    # Tạo đường dẫn đầy đủ đến tệp
    file_path = os.path.join(asset_dir, filename)
    
    # Kiểm tra xem tệp có tồn tại không
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Tệp {filename} không tồn tại trong thư mục 'assets'.")
    
    return file_path


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
        audio = open(get_asset_path('cat.mp3'),'rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=oFGz1kcRPfY'
        st.video(video,format = 'video/mp4')
    with col7:
        image = get_asset_path('cat.jpg')
        st.image(image,caption = "Con mèo")
        
if b2:
    
    with col6:
        st.write("Âm thanh")
        audio = open(get_asset_path('dog.mp3'),'rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=hPzfZvpoW4A'
        st.video(video,format = 'video/mp4')
    with col7:
        image = get_asset_path('dog.jpg')
        st.image(image,caption = "Con chó")
if b3:
   
    with col6:
        st.write("Âm thanh")
        audio = open(get_asset_path('monkey.mp3'),'rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=8d3z4QpUnrQ'
        st.video(video,format = 'video/mp4')
    with col7:
        image = get_asset_path('monkey.jpg')
        st.image(image,caption = "Con khỉ")
if b4:
    with col6:
        st.write("Âm thanh")
        audio = open(get_asset_path('eagle.mp3'),'rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=T7pk7f649qU'
        st.video(video,format = 'video/mp4')
    with col7:
        image = get_asset_path('eagle.jpg')
        st.image(image,caption = "Đại bàng")
if b5:
    with col6:
        st.write("Âm thanh")
        audio = open(get_asset_path('chicken.mp3'),'rb')
        st.audio(audio,format = 'audio/mp3')

        st.write("Video")
        video = 'https://www.youtube.com/watch?v=a0ZBh_ggwJk'
        st.video(video,format = 'video/mp4')
    with col7:
        image = get_asset_path('chicken.jpg')
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
            

        
