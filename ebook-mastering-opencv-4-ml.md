# 1. ml with opencv
## a. color quantization with kmeans
=> giảm bớt số lượng màu sắc trong ảnh sử dụng kmeans

các bước thực hiện:
1. reshape img array sang (-1,3) 
2. sử dụng kmeans để tạo thành các cụm => lấy center của mỗi cụm là màu sắc đại diện cho cụm đó (nhớ convert về int sau khi có center từ kmeans)
3. từ img array => convert sang label => từ label convert sang center của label đó

## b. classification with knn & svm
trong sách đã thực hiện bài toán nhận diện chữ số viết tay.

- đầu tiên họ đã thử nghiệm vs k (trong knn) và % data training khác nhau để so sánh

Tuy nhiên điểm hay của phần này là họ đã thực hiện preprocessing data trước khi train và đã improve performance:

- preprocessing1: de-skew (khử độ lệch của chữ số trong ảnh) bằng cách xác định ảnh lệch =  `cv2.momments` và xoay ảnh lại sử dụng `cv2.warpAffine` => pp này đã giúp tăng acc (training 50%, k = 3) từ 92.6 lên 95% (các thử nghiệm khác cũng tăng, nhưng mình lấy 1 mốc để so sánh) 
- preprocessing2: ngoài deskew, sử dụng thêm descriptor Histogram of Oriented Gradients (HOG) => 1 loại image descriptor phổ biến => acc (cùng đkien 50% train, k=3) tăng lên ~98%

tham khảo thêm về HOG: https://phamdinhkhanh.github.io/2019/11/22/HOG.html

- svm (sử dụng HOG và deskew) cho acc (50% train) đến 98.6%, khi thực hiện tuning hyperparameter, acc lên đến 99.2%

```markdown
theo mình các algorithm trên vẫn nên dùng sklearn, còn opencv chỉ để xử lý ảnh trước
=> vì vậy nếu đã biết sklearn, mình nghĩ chỉ nên đọc qua cách sử dụng là đc
```
# 2. deep learning

```markdown
để benchmark task object detection, có 3 dataset đc sử dụng:
  - PASCAL VOC (PASCAL Visual Object Classification) - 20 cats - 10k images
  - ImageNet - 200 cats - 500k images
  - COCO (Common Objects in Context) - 2.5M labels trong 328k images

và sử dụng mAP (mean average precison)
```

## load input to blob (from image/images) 
- opencv có thể dùng các pretrain network của tf, pytorch, onnx, caffe, darknet để thực hiện inference
- `cv2.dnn.blobFromImage()`
```python
retval=cv2.dnn.blobFromImage(image[, scalefactor[, size[, mean[, swapRB[,crop[, ddepth]]]]]]) => create 4 dimension (thêm batch_size)
retval=cv2.dnn.blobFromImages(images[, scalefactor[, size[, mean[, swapRB[,crop[, ddepth]]]]]]) => create 4 dimension (thêm batch_size)
```
=> `blobFromImage` có thể resize, crop, normalize (with mean), scale, swap channel R-B
- chú ý crop trong func này crop từ tâm (center)

```python
# Create a list of images:
images = [image, image2]
# Call cv2.dnn.blobFromImages():
blob_images = cv2.dnn.blobFromImages(images, 1.0, (300, 300), [104., 117.,123.], False, False)
# Set the blob as input and obtain the detections:
net.setInput(blob_images)
detections = net.forward()
```

=> `net.getPerfProfile()` =>  overall time for inference and timings (in ticks) for the layers

## load model
```python
# Load the serialized caffe model from disk:
net = cv2.dnn.readNetFromCaffe("ResNet-50-deploy.prototxt", "ResNet-50-model.caffemodel")

# Load the serialized caffe model from disk:
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")
```

## flow
- load input to blob `cv2.dnn.blobFromImage`/ `cv2.dnn.blobFromImages`
- load model `cv2.dnn.readNetFromCaffe`,...
- setinput `net.setInput(blob)`
- forward `preds = net.forward()`

# 3. face detection, tracking & recognition
## face detection
có 2 approach:
- haar cascade-based
- deep learning-based

## haar-cascade
- cascade có thể detect object khác ngoài face (body, plate,...)
- có thể download cascade classifier files ở: https://github.com/opencv/opencv/tree/master/data/haarcascades
```python
# cách 1:
cas = cv2.CascadeClassifier(cascade_file) => đc sử dụng để load classifer từ file
face = cas.detectMultiScale(gray) => return list of rectangles

# cách 2
cv2.face.getFacesHAAR(img, cascade_file) => return list of rectangles
```
- CascadeClassifier().detectMultiScale(gray) => input là gray, output là list of rectangles => ngoài ra có params để detect object theo range size (minSize, maxSize)
- face.getFacesHAAR(img, cascade_file) => input là bgr, output là list of rectangles

## deep learning
- khi inference sử dụng deep learning => opencv sẽ return array có dim cuối cùng là 7, trong đó:
  - detections[0, 0, i, 0] => index của image trong batch 
  - detections[0, 0, i, 2] => confidence
  - detections[0, 0, i, 3:7] => tọa độ (đã normalize)
