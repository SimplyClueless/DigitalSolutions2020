import RPi.GPIO as GPIO
from datetime import datetime
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 60
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(1280, 720))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
buzzer = 23
delay = 1

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

def Distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    
    return distance

def Alarm():
    global delay
    
    while (delay >= 0.0):
        print(delay)
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(delay)

        delay -= 0.02
        
    delay = 1

try:
    while True:
        distance = Distance()
        print ("Measured Distance = %.1f cm" % distance)
        if (distance <= 20.0):
            Alarm()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()