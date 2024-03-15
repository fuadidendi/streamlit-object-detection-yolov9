# Object Detection using YoloV9 and Streamlit Python

## Folder contents

The project **streamlit-object-detection-with-yolov9** contains one source main file [streamlit_app.py](streamlit_app.py). 

I used **yolov9c.pt** model. You can download the model [here](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov9c.pt), or you can see more from [Ultralytics YOLOV9](https://docs.ultralytics.com/models/yolov9/#performance-on-ms-coco-dataset).

Below is short explanation of remaining files in the project folder.

```
├── app.py
├── streamlit_app.py            This is the file object detection using YoloV9 and Streamlit
└── README.md                   This is the file you are currently reading
```

## How to run
Clone this repository
```sh
git clone https://github.com/fuadidendi/streamlit-object-detection-yolov9.git
```
Go to the directory and run by
```sh
streamlit run streamlit_app.py
```

## Preview
### Local Video Source
Local video selected as video source. Make sure there is a camera connected to your device.
Just toggle on the Start Video and the real-time object detection from your camera will be begin.

### Youtube Video Source
Youtube video is selected as the video source, you must enter the YouTube video link.
Here below preview when you use youtube video as video source. I used No Copyright Video [Tokyo Walk - Pedestrian | Free Footage Stock Video](https://www.youtube.com/watch?v=OUlP6JLVKYo)

![Alt text](snip-youtube-object-detection-yolov9-streamlit.gif?raw=true "Youtube Video Source")