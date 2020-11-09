from sensors import Email, Camera, Ultrasonic, Buzzer
import time
from time import strftime, gmtime

email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", "s06442@sheldoncollege.com", "Benjamin Bristow")
camera = Camera()
ultrasonic = Ultrasonic(22, 27)
buzzer = Buzzer(17)
videoFile = "roomCapture.avi"

def Alarm(delay):
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    currentDate = time.strftime("%d/%m/%Y", gmtime())
    text = f"Your motion sensor has been activated at {currentTime} {currentDate}"

    buzzer.On()
    camera.Record(60)
    buzzer.Off()

    email.SendFile(text, videoFile)

Alarm(1)

"""
while True:
    distance = ultrasonic.Distance()
    print ("Measured Distance = %.1f cm" % distance)
    if (distance <= 5.0):
        Alarm(1)
    time.sleep(0.1)
"""
