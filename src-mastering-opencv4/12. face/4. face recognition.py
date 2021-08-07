import cv2
import numpy as np
import matplotlib.pyplot as plt
import stackimages

# train_img_files = ['model/jared_1.jpg','model/jared_2.jpg','model/obama.jpg']
# test_img_files = ['model/jared_4.jpg','model/jared_3.jpg']
train_img_files = ['face_images/img3.jpg','face_images/img8.jpg','face_images/img44.jpg','face_images/img1.jpg']
test_img_files = ['face_images/img7.jpg','face_images/img9.jpg','face_images/img46.jpg','face_images/img54.jpg']

cas = cv2.CascadeClassifier('model/haarcascade_frontalface_alt2.xml')
model = cv2.face.LBPHFaceRecognizer_create()

def detect_face(path):
    img = cv2.imread(path)
    # gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    faces_bbox = cas.detectMultiScale(img, 1.3, 5)
    x, y, w, h = faces_bbox[0]
    face = img[y:y + h, x:x + w]
    face = cv2.resize(face, dsize=(224,224))
    return cv2.cvtColor(face, code=cv2.COLOR_BGR2GRAY)


faces = []
for f in train_img_files:
    face = detect_face(f)
    # cv2.imshow('train' + f, face)
    faces.append(face)

cv2.imshow('out', stackimages.ManyImgs(scale=1,imgarray=[faces.copy()]))
# print(faces)
print([f.shape for f in faces])
# for idx,f in enumerate(faces):
#     cv2.imshow('out'+str(idx),f)
# cv2.waitKey()


# TRAIN
# model.train(faces,np.array([0,0,5]))
model.train(faces,np.array([0,1,2,3]))
model.save("model.yml")
model.read("model.yml")

# PREDICT
for f in test_img_files:
    face = detect_face(f)
    idx, conf = model.predict(face)
    print(idx, conf)
    imgstack = stackimages.ManyImgs(scale=1, imgarray=[[face, detect_face(train_img_files[idx])]])
    cv2.putText(imgstack, text=f + '-' + str(idx)+ '-'+ str(conf), org=(0,10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0,0,255))
    cv2.imshow('out'+f, imgstack)

# imgstack = stackimages.ManyImgs(scale=0.2,imgarray=[faces])
# cv2.imshow('out', imgstack)
cv2.waitKey(0)