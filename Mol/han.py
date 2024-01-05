import cv2
import mediapipe as mp
import pyautogui



class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                print(handLms)
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    def positionFinder(self,image,  draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            for Hand in  self.results.multi_hand_landmarks:
                 for id, lm in enumerate(Hand.landmark):
                     h,w,c = image.shape
                     cx,cy = int(lm.x*w), int(lm.y*h)
                     lmlist.append([id,cx,cy])

                 if draw:
                     cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)

        return image


def generate_frames():
    cap = cv2.VideoCapture(0)
    tracker = handTracker()
    
    while True:
        success,image = cap.read()
        if not success:
           continue
        image = tracker.handsFinder(image)
        image= tracker.positionFinder(image)
        # You can draw on the frame using the results

        # Encode the frame and yield it to the response
        ret, buffer = cv2.imencode('.jpg', image)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
