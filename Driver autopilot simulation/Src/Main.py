import cv2
import time
import random

# Load pre-trained classifier for face and eyes detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Threshold values
DROWSY_THRESHOLD = 5   # seconds of closed eyes = drowsy
ALCOHOL_PROBABILITY = 0.1  # random chance to simulate drunk driver

def detect_driver_state(frame):
    """Detect if driver is drowsy (eyes closed)"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_detected = False
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) > 0:
            eyes_detected = True
    
    return eyes_detected

def autopilot_engage(reason):
    print(f"[AUTO-PILOT] Activated due to {reason}!")
    print("[AUTO-PILOT] Slowing down the car...")
    time.sleep(2)
    print("[AUTO-PILOT] Searching for safe roadside spot...")
    time.sleep(2)
    print("[AUTO-PILOT] Pulling over safely. Hazard lights ON.")
    time.sleep(2)
    print("[AUTO-PILOT] Waiting until driver is capable again.\n")

def simulate():
    cap = cv2.VideoCapture(0)  # open webcam
    closed_eye_start = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            eyes_open = detect_driver_state(frame)

            # Random chance to simulate drunk driver
            if random.random() < ALCOHOL_PROBABILITY:
                autopilot_engage("possible alcohol influence")
                continue

            if not eyes_open:
                if closed_eye_start is None:
                    closed_eye_start = time.time()
                else:
                    duration = time.time() - closed_eye_start
                    if duration > DROWSY_THRESHOLD:
                        autopilot_engage("drowsiness detected")
                        closed_eye_start = None
            else:
                closed_eye_start = None

            # Show frame
            cv2.imshow('Driver Monitoring System', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    simulate()
