import cv2
import time

cap = cv2.VideoCapture('../resources/example_01.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        start = time.time()

        cv2.imshow('out', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

        end = time.time()

        processing_time_frame = end - start

        print("fps: {}".format(1.0 / processing_time_frame))

    else:
        break
