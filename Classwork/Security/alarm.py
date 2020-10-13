import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
from datetime import datetime
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from datetime import datetime
from subprocess import call

email = "sheldoncollegeiot@gmail.com"
password = "P@ssword#1"
sendToEmail = "s06442@sheldoncollege.com"

msg = MIMEMultipart()
msg["Subject"] = "Benjamin Bristow"
msg["From"] = email
msg["To"] = sendToEmail

text = "Your motion sensor has been activated at "
msg.attach(MIMEText(text, "plain"))

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(640, 480))

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
    print("Alarm Triggered")
    camera.start_preview()
    camera.start_recording("roomCapture.h264")

    while (delay >= 0.0):
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(delay)

        delay -= 0.02
        
    camera.stop_recording()
    camera.stop_preview() 
    delay = 1
    SendFile()

def SendFile():
    command = "MP4Box -add roomCapture.h264 roomCapture.mp4"
    call([command], shell=True)

    filename = "roomCapture.mp4"
    with open(filename, "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())
    encoders.encode_base64(part)

    part.add_header("Content-Disposition", f"attachment; filename= {filename}")

    msg.attach(part)
    message = msg.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email, password)
        server.sendmail(email, sendToEmail, message)
        server.quit()

    print("File Sent")

while True:
    distance = Distance()
    print ("Measured Distance = %.1f cm" % distance)
    if (distance <= 20.0):
        Alarm()
    time.sleep(0.1)