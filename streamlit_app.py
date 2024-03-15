from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import streamlit as st
import altair as alt
from vidgear.gears import CamGear
import cv2

# set desired quality as 720p
options = {"STREAM_RESOLUTION": "720p"}

# Load the YOLOv9 model
print("[INFO] loading YOLOv9 model...")
model = YOLO('yolov9c.pt')

# initialize the video stream
print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)

st.set_page_config(
    page_title="YoloV9 Object Detection Dashboard",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

def plot_boxes(frame):
    results = model.predict(frame)

    for r in results:
        
        annotator = Annotator(frame)
        
        boxes = r.boxes
        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

    frame = annotator.result()

    return frame

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
        FRAME_WINDOW = st.image([])
        stream = CamGear(
            source=youtube_link,
            stream_mode=True,
            logging=True,
            **options
        ).start()

        while True:
             frame = stream.read()
             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
             plot_boxes(frame)
             FRAME_WINDOW.image(frame)
    else:
        st.text('Run from Local Video 👇')
        on = st.toggle('Start video')
        FRAME_WINDOW = st.image([])

        while on:
                _, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                plot_boxes(frame)
                FRAME_WINDOW.image(frame)
        else:
                cap.release()
                st.write('Video stopped')

# wnd Column
with col[1]:
    st.markdown('#### Description')
    if selected_video_source=='Youtube':
        st.text('Youtube selected')
    else:
        st.text('Local selected')