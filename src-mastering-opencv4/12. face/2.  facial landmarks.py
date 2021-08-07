import cv2
import numpy as np

img = cv2.imread('../../resources/Photos/lady.jpg')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

cas = cv2.CascadeClassifier('model/haarcascade_frontalface_alt2.xml')
faces = cas.detectMultiScale(image=gray)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255), thickness=2)

facemark = cv2.face.createFacemarkLBF()
facemark.loadModel("model/lbfmodel.yaml")
ok, landmarks = facemark.fit(img, faces)
print ("landmarks LBF", ok, landmarks)
print(landmarks[0][0].shape)

for p in landmarks[0][0]:
    print(p.astype(np.int16))
    cv2.circle(img, center=p.astype(np.int16), radius=2, color=(0,0,255), thickness=-1)

cv2.imshow('out', img)
cv2.waitKey()