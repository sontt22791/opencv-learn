import cv2
import numpy as np

import stackimages

img = cv2.imread('./model/test_face_detection.jpg')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

cas_alt2 = cv2.CascadeClassifier('./model/haarcascade_frontalface_alt2.xml')
cas_default = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')

faces_alt2 = cas_alt2.detectMultiScale(gray)
faces_default = cas_default.detectMultiScale(gray)

img_faces_alt2 = img.copy()
img_faces_default = img.copy()

for (x,y,w,h) in faces_alt2:
    cv2.rectangle(img_faces_alt2,pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255),thickness=2)

for (x,y,w,h) in faces_default:
    cv2.rectangle(img_faces_default,pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255),thickness=2)


img_faces_haar_alt2 = img.copy()
img_faces_haar_default = img.copy()

val, faces_haar_alt2 = cv2.face.getFacesHAAR(img, face_cascade_name='./model/haarcascade_frontalface_alt2.xml')
val, faces_haar_default = cv2.face.getFacesHAAR(img, face_cascade_name='./model/haarcascade_frontalface_default.xml')

for (x,y,w,h) in np.squeeze(faces_haar_alt2):
    cv2.rectangle(img_faces_haar_alt2,pt1=(x,y), pt2=(x+w, y+h), color=(0,255,255),thickness=2)

for (x,y,w,h) in np.squeeze(faces_haar_default):
    cv2.rectangle(img_faces_haar_default,pt1=(x,y), pt2=(x+w, y+h), color=(0,255,255),thickness=2)

imgstack = stackimages.ManyImgs(scale=0.4, imgarray=[[gray,img_faces_alt2, img_faces_default],
                                                     [img,img_faces_haar_alt2,img_faces_haar_default]])
cv2.imshow('faces_alt2', imgstack)
cv2.waitKey()