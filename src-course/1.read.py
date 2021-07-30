import cv2
import numpy as np

print(np.ones(shape=(3,4)))

img = cv2.imread("resources/lena.jpg")
cv2.imshow("out", img)
cv2.waitKey(0)

# cap = cv2.VideoCapture("resources/example_01.mp4") # read file
cap = cv2.VideoCapture(0) # camera

while True:
    success, img = cap.read()
    if success == False:
        break
    cv2.imshow("out", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(1)

