#car Detetction

import cv2


#video_capture = cv2.VideoCapture('dataset/video1.avi')
#video_capture = cv2.VideoCapture('dataset/video2.avi')
video_capture = cv2.VideoCapture('dataset/video3.mp4')
#video_capture = cv2.VideoCapture('dataset/video4.mp4')

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, img = video_capture.read()
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('car_detected', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()