import numpy as np
from datetime import datetime
import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(3, 1280)
cam.set(4, 720)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.mp4', fourcc, 30, (1280, 720))

while True:
    ret, img = cam.read()

    img = cv2.flip(img, 4)
    cv2.putText(img, "You're a faggot", (400, 100), font, 2, (0, 83 ,207), 2, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (1000, 700), font, .5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Security Camera', img)

    out.write(img)

    k = cv2.waitKey(3) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()