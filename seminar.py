import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier('palm_v4.xml')
fist_cascade = cv2.CascadeClassifier('fist_v3.xml')

lower = np.array([0, 58, 50], dtype = "uint8")
upper = np.array([30, 255, 255], dtype = "uint8")

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        x=faces[0,0]
        y=faces[0,1]
        w=faces[0,2]
        h=faces[0,3]
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        converted = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(roi_color, roi_color, mask = skinMask)

        cv2.imshow("face", cv2.flip(skin,1))
    if len(fists) > 0:
        x=fists[0,0]
        y=fists[0,1]
        w=fists[0,2]
        h=fists[0,3]
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        converted = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(roi_color, roi_color, mask = skinMask)

        cv2.imshow("fist", cv2.flip(skin,1))
    if len(hands) > 0:
        x=hands[0,0]
        y=hands[0,1]
        w=hands[0,2]
        h=hands[0,3]
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        converted = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(roi_color, roi_color, mask = skinMask)

        cv2.imshow("hand", cv2.flip(skin,1))
    cv2.imshow('img',cv2.flip(img,1))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
