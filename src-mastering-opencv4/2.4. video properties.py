import cv2

cap = cv2.VideoCapture('../resources/Videos/dog.mp4')

frame_idx = cap.get(cv2.CAP_PROP_FRAME_COUNT)-1
while True and frame_idx >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES,frame_idx)
    _, frame = cap.read()
    cv2.imshow('out', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    frame_idx -= 1


print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# print(cap.get(cv2.CAP_PROP_FPS))

cap.release()
cv2.destroyAllWindows()
