# Learning path

các nguồn mà mình đã học
1. [LEARN OPENCV in 3 HOURS with Python with 3 projects](https://www.youtube.com/watch?v=WQeoO7MI0Bs) => clip này chỉ nên xem phần project và thực hành, còn lý thuyết chỉ đề cập đến 1 số code về 1 vấn đề nhỏ => khó hiểu bản chất và khó sử dụng => ko phù hợp vs beginner => nên xem thứ 3
2. [Full Tutorial with Python - Freecodecamp](https://www.youtube.com/watch?v=oXlwWbU8l2o) => clip này mình nghĩ nên xem sau khi đọc xong ebook => nên xem thứ 2
3. [ebook Mastering OpenCV 4 with Python](https://github.com/PacktPublishing/Mastering-OpenCV-4-with-Python) => nên xem/học đầu tiên

# 1 số library ngoài opencv có thể tham khảo
- [scikit-image](https://scikit-image.org/docs/stable/auto_examples/index.html)
- [dlib]() (nhớ fai cài cmake và g++ trước) => có thể thực hiện face detection, face/object tracking, face recognition 
- [face_recognition]()
- [cvlib]()
- [imutils](https://github.com/jrosebr1/imutils) => đây là lib của team pyimagesearch.com, có hỗ trợ 1 số func translation, rotate, warpPerspective
![](images/face.png)

# structure
- ebook: sách về opencv
- images: cách ảnh sử dụng trong notes
- resources: ảnh/video dùng để practice
- src-course: code mà mình practice của 2 clip youtube
- src-mastering-opencv4: code practice của ebook mastering
- src-original: code gốc của ebook và course youtube

# guide
- [ebook-mastering-opencv-4.md](ebook-mastering-opencv-4.md)
- [ebook-mastering-opencv-4-ml.md](ebook-mastering-opencv-4-ml.md)
- [custom cascade.md](custom-cascade.md)

# sample projects:
1. object detection
- object detection with opencv (sử dụng deep learning pretrain model): https://www.youtube.com/watch?v=HXDD7-EnGBY
- object detection trên raspberry pi: https://www.youtube.com/watch?v=Vg9rrOFmwHo

2. ocr receipt 

flow:
- sử dụng 1 ảnh form chuẩn
- dùng `ORB` trong cv2 để matching receipt cần detect vs form
- sử dụng các points matching ở trên => align các receipt theo chuẩn form
- dùng mouse-event để xác định các bbox trên form và ảnh receipt đã align
- dùng `Tesseract` để convert bbox đã detect ở trên sang text

part1: https://www.youtube.com/watch?v=W9oRTI6mLnU

part2: https://www.youtube.com/watch?v=cUOcY9ZpKxw

3. text detection sử dụng `Tesseract`

https://www.youtube.com/watch?v=6DjFscX4I_c

4. virtual paint (project1 trong clip `LEARN OPENCV in 3 HOURS with Python with 3 projects`)

flow:
- segment màu sắc của bút theo nắp bút sử dụng `cv2.inRange` (do nắp bút có màu sắc)
- detect contour bao quanh nắp bút sau khi đã có mask tạo từ bước 1
- lưu points khi di chuyển bút vào list, sau đó draw các point đó 

5. number plate detection (project3 trong clip)

project này sử dụng rus_number_plate cascade của opencv để detect

6. document scanner (project 2 trong clip)

project này detect contour bao quanh document, sau đó dùng `cv2.approxPolyDP` để detect các góc và thực hiện warpPerspective


# Note
- four_points_transform (trong link https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/) cũng như trong imutils khác vs Perspective thông thường
là nó ước lượng chiều dài, rộng của object sau khi align =  max của nó trong ảnh gốc thay vì fai tự define w,h => mặc dù vậy theo mình nó sẽ có nhược điểm là đối vs ảnh quá nghiêng thì 
nó sẽ align ko đc như mong muốn. => vì vậy khi align nên tính đến aspect ratio để align đc chuẩn hơn (đọc phần `Improving your top-down transform results by computing the aspect ratio` trong link)
- trong link trên có nói về làm sao để xác định 4 góc của object 1 cách auto => theo mình đang hiểu thì 1 số task cụ thể, có 1 cách là xác định contour và lấy contour có area lớn nhất (có thể fai search thêm)