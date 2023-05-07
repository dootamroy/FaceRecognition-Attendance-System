# created by Dootam Roy @2021

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
# from PIL import ImageGrab

from Encoding import *
from markAttendance import *
from CaptureScreen import *


Capture = 1       # val 0 == [captures web cam] val 1 == [captures screen].

path = 'Student_Images'  # Directory for fetching the student images.
images = []  # List of all the images to be imported.
StudentNames = []  # name of the student as pic name.
myList = os.listdir(path)  # list of images.
print(myList)

# [Name of the Student's pic should be his/her name].

for img in myList:
    curImg = cv2.imread(f'{path}/{img}')  # read the image.
    images.append(curImg)
    StudentNames.append(os.path.splitext(img)[0])
print(StudentNames)


encodeListKnown = findEncodings(images)    # Encoding all the images.
print(f'Encoding Complete : {len(encodeListKnown)}')


cap = cv2.VideoCapture(0)                  # Start capturing video.

while True:
    if Capture == 0:                   # Condition for either capturing webcam or screen.
        success, img = cap.read()

    else:
        img = captureScreen()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)      # for finding index from the list faceDist which has the least distance.

        if faceDis[matchIndex]< 0.5:
            name = StudentNames[matchIndex].upper()
            # print(name)
            markAttendance(name)
        else:
            name = 'Unknown'
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4          # cos we have earlier resized the images to 1/4th.
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()