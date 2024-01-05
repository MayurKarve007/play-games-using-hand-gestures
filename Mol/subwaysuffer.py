import cv2
import numpy as np
import pyautogui
from cvzone.HandTrackingModule import HandDetector
import math
# from Mol.originalmouse import mouse

def findDistance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        return length, info


def generate_frames_subwaysuffer():
 wCam, hCam = 640, 480
 cap = cv2.VideoCapture(0)
 detector = HandDetector(detectionCon=0.9, maxHands=1)
 wScr, hScr = pyautogui.size()
 hScr = hScr + 1200
 wScr = wScr + 1500   


 frameR = 100
 smoothening = 10
 plocX, plocY = 0, 0
 clocX, clocY = 0, 0


 while True:
    success, img = cap.read()
    if not success:
        continue
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img ,flipType=False)

    if hands:
        # img=mouse.mouse(img,hands)

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
         length2, info2= findDistance(lmlist[8][0:2], lmlist[12][0:2])
         if length1 <15 and length2 <15:
            pyautogui.click(button = "left")
        x1, y1 = lmlist[8][0], lmlist[8][1]
        x2, y2 = lmlist[12][0], lmlist[12][1]

            
            # cv2.circle(img, (mid_x, mid_y), 5, (0, 255, 255), 2)
        fingers = detector.fingersUp(hands[0])
        if fingers[1] == 1 and fingers[2] == 1:
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            r, t = 9, 2

            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            if -55 > (clocX - plocX):
                pyautogui.press('left')

            if -55 > (plocX - clocX):
                pyautogui.press('right')

            if -39 > (clocY - plocY):
                pyautogui.press('up')

            if -30 > (plocY - clocY):
                pyautogui.press('down')

            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
    ret, buffer = cv2.imencode('.jpg', img)
    if not ret:
        continue
    yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
