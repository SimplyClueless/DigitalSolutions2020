from sensors import Email

email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", "s06442@sheldoncollege.com", "Benjamin Bristow")
sense = RPSenseHat()

maxAcceleration = 4
currentAcceleration = 0

while True:
    if currentAcceleration >= maxAcceleration:
        email.AttachText("I've McFallen and I need assistance!")
        email.SendEmail()