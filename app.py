from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2

# Load the YOLOv9 model
print("[INFO] loading YOLOv9 model...")
model = YOLO('yolov9c.pt')

# initialize the video stream
print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame, stream end? Exiting ...")
        break

    results = model.predict(frame)

    for r in results:
        
        annotator = Annotator(frame)
        
        boxes = r.boxes
        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

    frame = annotator.result()
    cv2.imshow('YOLO V9 Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()