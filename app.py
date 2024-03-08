from ultralytics import YOLO
import cv2 as cv

# Load the YOLOv9 model
print("[INFO] loading YOLOv9 model...")
model = YOLO('yolov9c.pt')

# initialize the video stream
print("[INFO] starting video stream...")
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# # Run predictions
# results = model.predict('test.jpg')

# # Display results
# results[0].show()

while True:
     # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame, stream end? Exiting ...")
        break

    results = model.predict(frame, show=True)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()