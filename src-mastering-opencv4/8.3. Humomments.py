import cv2

def run(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, thresh=75, maxval=255, type=cv2.THRESH_BINARY)
    m1 = cv2.moments(array=thresh)
    hm1 = cv2.HuMoments(m = m1)
    print(f'm1 : {m1}')
    print(f'hm1 : {hm1.flatten()}')

    cts, h = cv2.findContours(thresh,mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
    m = cv2.moments(array=cts[0])
    hm = cv2.HuMoments(m = m)
    print(f'm : {m}')
    print(f'hm : {hm.flatten()}')

run('../resources/shape_features.png')
run('../resources/shape_features_reflection.png')
run('../resources/shape_features_rotation.png')