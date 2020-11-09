import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Ultrasonic:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo

        print(self.trigger)
        print(self.echo)

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def Distance(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        print("1")

        StartTime = time.time()
        StopTime = time.time()

        print("2")

        while GPIO.input(self.echo) == 0:
            StartTime = time.time()

        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
            
        print("3")

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2

        print("4")
        
        return distance

ultrasonic = Ultrasonic(22, 27)

while True:
    distance = ultrasonic.Distance()    
    print ("Measured Distance = %.1f cm" % distance)
    time.sleep(1)