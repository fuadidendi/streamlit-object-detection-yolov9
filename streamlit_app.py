from ultralytics import YOLO
import streamlit as st
import altair as alt
import cv2

st.set_page_config(
    page_title="YoloV9 Object Detection Dashboard",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

with st.sidebar:
    st.title('🎥 YoloV9 Object Detection Dashboard')
    
    video_source_list = ['Local', 'Youtube']
    selected_video_source = st.selectbox('Select video source', video_source_list)

# App Layout
col = st.columns((4.5, 2), gap='medium')

# 1st Column
with col[0]:
    st.markdown('#### Video demo')
    if(selected_video_source == 'Youtube'):
        youtube_link = st.text_input('Enter your Youtube video link here 👇', 'https://www.youtube.com/')
        VIDEO_URL = youtube_link
        st.video(VIDEO_URL)
    else:
        st.text('Run from Local Video 👇')
        on = st.toggle('Start video')
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)

        while on:
                _, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FRAME_WINDOW.image(frame)
        else:
                st.write('Video stopped')

# wnd Column
with col[1]:
    st.markdown('#### Description')
    if selected_video_source=='Youtube':
        st.text('Youtube selected')
    else:
        st.text('Local selected')