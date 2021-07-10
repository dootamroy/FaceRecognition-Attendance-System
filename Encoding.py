# created by Dootam Roy @2021

import cv2
import numpy as np
import face_recognition


def findEncodings(images):      # encoding of the Student images.
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
