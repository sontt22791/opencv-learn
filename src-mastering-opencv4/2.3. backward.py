import cv2

cap = cv2.VideoCapture('../resources/example_01.mp4')

# We get the index of the last frame of the video file:
frame_index = cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print("starting in frame: '{}'".format(frame_index))

while cap.isOpened() and frame_index >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    ret, frame = cap.read()

    if ret is True:

        cv2.imshow('out', frame)

        frame_index = frame_index - 1
        print("next index to read: '{}'".format(frame_index))

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
