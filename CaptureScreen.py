# created by Dootam Roy @2021


# FOR CAPTURING SCREEN RATHER THAN WEBCAM.
import cv2
import numpy as np
from PIL import ImageGrab


def captureScreen(bbox=(300, 300, 690 + 300, 530 + 300)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr
