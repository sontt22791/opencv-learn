import cv2
import dlib

cap = cv2.VideoCapture(0)
tracker = dlib.correlation_tracker()

# Structure to hold the coordinates of the object to track:
points = []

# This is the mouse callback function:
def mouse_event_handler(event, x, y, flags, param):
    # references to the global points variable
    global points

    # If left button is click, add the top left coordinates of the object to be tracked:
    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]

    # If left button is released, add the bottom right coordinates of the object to be tracked:
    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))

cv2.namedWindow('out') # fai khai báo windows, nếu k mouse callback sẽ ko biết check event ở window nào
cv2.setMouseCallback('out', mouse_event_handler)

tracking_state = False # flag

while True:
    isok, frame = cap.read()

    if not isok:
        break

    # We set and draw the rectangle where the object will be tracked if it has the two points:
    if len(points) == 2:
        print(points)
        cv2.rectangle(frame, points[0], points[1], (0, 0, 255), 3)
        dlib_rectangle = dlib.rectangle(points[0][0], points[0][1], points[1][0], points[1][1])

    # sau khi xác định đc 2 point của object => bấm s để bắt đầu track
    if cv2.waitKey(1) & 0xFF == ord('s'):
        tracker.start_track(frame, dlib_rectangle)
        tracking_state = True
        points = [] # reset về [] để ko bị thay đổi dlib_rectangle

    if tracking_state == True:
        tracker.update(frame)
        pos = tracker.get_position()
        cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)

    cv2.imshow('out', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()