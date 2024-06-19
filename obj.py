import numpy as np
import imutils
import cv2
import time
import pyttsx3

prototxt = "MobileNetSSD_deploy.prototxt.txt"
model    = "MobileNetSSD_deploy.caffemodel"

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat","bottle", "bus" , "car", "cat", 
           "chair","cow", "diningtable", "dog","horse", "motorbike", "person","pottedplant", "sheep"
           "sofa","train","tvmonitor","mobile"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("Loading model...")

net = cv2.dnn.readNetFromCaffe(prototxt, model)
print("Model Loaded")
print("Starting Camera Feed")

CAP = cv2.VideoCapture(0)
time.sleep(2.0)
w, h = None, None

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    ret, frame = CAP.read()
    if frame is None:
        print("Error: frame is None. Exiting...")
        break

    # Resize the frame to a fixed width of 1000 pixels while maintaining aspect ratio
    frame = imutils.resize(frame, width=1000)
    if w is None or h is None:
        (h, w) = frame.shape[:2]

    imResizeBlob = cv2.resize(frame, (300, 300))
    blob = cv2.dnn.blobFromImage(imResizeBlob, 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detection = net.forward()
    print(detection)
    detshape = detection.shape[2]
    for i in np.arange(0, detshape):
        confidence = detection[0, 0, i, 2]
        confThresh = 0.5
        if confidence > confThresh:
            idx = int(detection[0, 0, i, 1])
            print("ClassID:", detection[0, 0, i, 1])
        if w is not None and h is not None:
            box = detection[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
            if startY - 15 > 15:
                y = startY - 15
            else:
                y = startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, COLORS[idx], 2)
            # Convert the label to voice
            engine.say(label)
            engine.runAndWait()

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
CAP.release()
cv2.destroyAllWindows()