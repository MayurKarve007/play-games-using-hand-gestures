
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np
import math


def findDistance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        return length, info



def mouse(img,hands):

    lmlist = hands[0]['lmList']
    length, info= findDistance(lmlist[8][0:2], lmlist[4][0:2])
    if length <18:
        ind_x, ind_y = lmlist[8][0], lmlist[8][1]
        mid_x,mid_y= lmlist[12][0], lmlist[12][1] 
        conv_x = int(np.interp(ind_x, (0,640),(-100, 2250)))
        conv_y = int(np.interp(ind_y, (0,480),(-100, 1150)))
        pyautogui.moveTo(conv_x,conv_y)
        print(conv_x,conv_y) 
        length1, info1= findDistance(lmlist[12][0:2], lmlist[4][0:2])
        length2, info1= findDistance(lmlist[8][0:2], lmlist[12][0:2])
        if length1 <15 and length2 <15:
            pyautogui.click(button = "left")
    return img
        