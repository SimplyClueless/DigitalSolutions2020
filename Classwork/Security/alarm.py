import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
from picamera import PiCamera
import os
import time
from time import strftime, gmtime
from subprocess import call

class Email:
    def __init__(self, email, password, sendToEmail, subject):
        self.email = email
        self.password = password
        self.sendToEmail = sendToEmail
        self.subject = subject

        self.msg = MIMEMultipart()
        self.msg["Subject"] = self.subject
        self.msg["From"] = self.email
        self.msg["To"] = self.sendToEmail

    def SendFile():
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

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.camera.rotation = 180

class Ultrasonic:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO_TRIGGER = self.trigger
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO_ECHO = self.echo
        GPIO.setup(GPIO_ECHO, GPIO.IN)

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

class Buzzer:
    def __init__(self, buzzer):
        self.buzzer = buzzer

        GPIO.setup(self.buzzer, GPIO.OUT)
    
    def Beep(delay):
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(delay)

email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", "s06442@sheldoncollege.com", "Benjamin Bristow")
camera = Camera()
ultrasonic = Ultrasonic(18, 24)
buzzer = Buzzer(23)

def Alarm(delay):
    print("Alarm Triggered")
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    currentDate = time.strftime("%d:%m:%Y", gmtime())
    text = f"Your motion sensor has been activated at {currentTime} {currentDate}"
    msg.attach(MIMEText(text, "plain"))

    camera.start_recording("roomCapture.h264")

    while (delay >= 0.0):
        print(delay)
        buzzer.Beep(delay)
        delay -= 0.02
        
    camera.stop_recording()

    command = "MP4Box -add roomCapture.h264 roomCapture.mp4"
    call([command], shell=True)
    SendFile()

while True:
    distance = ultrasonic.Distance()
    print ("Measured Distance = %.1f cm" % distance)
    if (distance <= 20.0):
        Alarm(1)
    time.sleep(0.1)