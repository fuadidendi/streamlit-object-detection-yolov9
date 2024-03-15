from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import streamlit as st
import cv2
from vidgear.gears import CamGear

# Function to plot bounding boxes on frames
def plot_boxes(frame, model):
    results = model.predict(frame)
    annotator = Annotator(frame)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # Box coordinates
            c = box.cls      # Class ID
            annotator.box_label(b, model.names[int(c)])
    return annotator.result()

# Function to process and display video
def process_video(source, model, options=None):
    if source == 'Local':
        cap = cv2.VideoCapture(0)  # Local webcam
    else:  # YouTube source
        cap = CamGear(source=source, stream_mode=True, logging=True, **options).start()

    FRAME_WINDOW = st.empty()

    while True:
        if source == 'Local':
            ret, frame = cap.read()
            if not ret:
                break
        else:  # YouTube source
            frame = cap.read()
            if frame is None:
                break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = plot_boxes(frame, model)
        FRAME_WINDOW.image(frame)

    if source == 'Local':
        cap.release()

# Load the YOLOv9 model
model = YOLO('yolov9c.pt')

# Streamlit UI setup
st.set_page_config(page_title="YoloV9 Object Detection Dashboard", page_icon="🎥", layout="wide", initial_sidebar_state="expanded")

st.title('🎥 YoloV9 Object Detection Dashboard')

# Sidebar
with st.sidebar:
    video_source = st.radio('Select video source', ['Local', 'YouTube'])
    youtube_link = ""
    if video_source == 'YouTube':
        youtube_link = st.text_input('YouTube video link', '')

# Set desired quality
options = {"STREAM_RESOLUTION": "720p"}

# Process video
if st.button('Start'):
    if video_source == 'YouTube' and youtube_link:
        process_video(youtube_link, model, options)
    elif video_source == 'Local':
        process_video('Local', model)

# Note on closing resources
st.sidebar.markdown("### Note")
st.sidebar.markdown("Close the browser tab or stop the app to release webcam resources properly when using Local video source.")