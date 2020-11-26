# Email modules
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Camera modules
import cv2
import numpy as np
from datetime import datetime

#from sense_hat import SenseHat

# GPIO modules
#import RPi.GPIO as GPIO

# Other modules
import time

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

    def SendEmail(self):
        context = ssl.create_default_context()
        self.message = self.msg.as_string()
        print(self.email)
        print(self.password)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.sendToEmail, self.message)
            server.quit()

        print("Email Sent!")

    def AttachText(self, text):
        self.msg.attach(MIMEText(text, "plain"))

    def AttachFile(self, file):
        filename = file
        with open(filename, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)

        part.add_header("Content-Disposition", f"attachment; filename= {filename}")

        self.msg.attach(part)

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 30)
        self.cam.set(3, 1280)
        self.cam.set(4, 720)

        self.font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter("roomCapture.avi", self.fourcc, 30, (1280, 720))

    def Record(self, recordTime):
        tick = 0

        while tick < recordTime * 10:
            self.ret, self.img = self.cam.read()

            self.img = cv2.flip(self.img, 0)
            cv2.putText(self.img, "You're being recorded", (400, 100), self.font, 2, (0, 83 ,207), 2, cv2.LINE_AA)
            cv2.putText(self.img, str(datetime.now()), (1000, 700), self.font, .5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('Security Camera', self.iSmg)

            self.out.write(self.img)
            tick += 1
            print(tick)

        self.cam.release()
        cv2.destroyAllWindows()


class RPSenseHatS:
    pass
    #def Accelerometer(self):
     #   red = (255, 0, 0)
#
 #       acceleration = sense.get_accelerometer_raw()
  #      x = acceleration["x"]
   #     y = acceleration["y"]
    #    z = acceleration["z"]
#
 #       x = abs(x)
  #      y = abs(y)
   #     z = abs(z)


class Ultrasonic:
    def __init__(self, trigger, echo):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

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
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.buzzer = buzzer

        GPIO.setup(self.buzzer, GPIO.OUT)
    
    def On(self):
        GPIO.output(self.buzzer, GPIO.HIGH)

    def Off(self):
        GPIO.output(self.buzzer, GPIO.LOW)

    def Beep(self, delay):
        self.On()
        print("Beep")
        time.sleep(delay)
        self.Off()
        print("No Beep")
        time.sleep(delay)