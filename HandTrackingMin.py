import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture frame. Check camera connection.")
        break

    cv2.imshow("Image", img)

    cv2.waitKey(1)
