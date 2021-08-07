import cv2
import dlib

cap = cv2.VideoCapture(0)
# khởi tạo detector
detector = dlib.get_frontal_face_detector()
# We initialize the correlation tracker.
tracker = dlib.correlation_tracker()

while True:
    isok, frame = cap.read()
    if isok is not True:
        break

    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    rects = detector(gray,0) # xác định bbox của face

    if len(rects) > 0:
        for r in rects:
            tracker.start_track(frame, r)

            print(tracker.update(frame))

            # Get the position of the tracked object:
            pos = tracker.get_position()
            # Draw the position:
            cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)

    cv2.imshow('out', frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
    # if cv2.waitKey(1) == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()