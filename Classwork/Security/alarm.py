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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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

    def SendFile(self, file):
        filename = file
        with open(filename, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)

        part.add_header("Content-Disposition", f"attachment; filename= {filename}")

        self.msg.attach(part)
        message = self.msg.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.sendToEmail, message)
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

        self.GPIO_TRIGGER = self.trigger
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        self.GPIO_ECHO = self.echo
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def Distance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        
        return distance

class Buzzer:
    def __init__(self, buzzer):
        self.buzzer = buzzer

        GPIO.setup(self.buzzer, GPIO.OUT)
    
    def Beep(self, delay):
        GPIO.output(self.buzzer, GPIO.HIGH)
        print("Beep")
        time.sleep(delay)
        GPIO.output(self.buzzer, GPIO.LOW)
        print("No Beep")
        time.sleep(delay)

email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", "s06442@sheldoncollege.com", "Benjamin Bristow")
camera = Camera()
ultrasonic = Ultrasonic(18, 24)
buzzer = Buzzer(23)
videoFile = "roomCapture.h264"

def Alarm(delay):
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    currentDate = time.strftime("%d/%m/%Y", gmtime())
    text = f"Your motion sensor has been activated at {currentTime} {currentDate}"
    email.msg.attach(MIMEText(text, "plain"))

    camera.camera.start_recording(videoFile)

    while (delay >= 0.0):
        buzzer.Beep(delay)
        delay -= 0.02
        
    camera.camera.stop_recording()

    email.SendFile(videoFile)

while True:
    distance = ultrasonic.Distance()
    print ("Measured Distance = %.1f cm" % distance)
    if (distance <= 20.0):
        Alarm(1)
    time.sleep(0.1)