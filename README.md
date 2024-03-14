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
Local video selected as video source

![Alt text](local_video.png?raw=true "Local Video Source")

Youtube video selected as video source, you should input the youtube link video

![Alt text](youtube_video.png?raw=true "Youtube Video Source")