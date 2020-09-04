import smtplib # Simple Mail Transfer Protocol
from email.mime.text import MIMEText # Library for text in an email
from email.mime.multipart import MIMEMultipart # Library for attachments and subject information
from email.mime.base import MIMEBase # basic mime functions for email creation
import os.path # read write access to OS file system (Only for attachments)
import time

email = "sheldoncollegeiot@gmail.com"
password = "P@ssword#1"
sendToEmail = "s06442@sheldoncollege.com"#; s05913@sheldoncollege.com; s05755@sheldoncollege.com; s08940@sheldoncollege.com; sheldoncollegeiot@gmail.com"
subject = "Benjamin Bristow"
message = """Greetings friends!\n 
        This is a message sent from me cause I'm cool!\n
        Have an amazing day you lovely people!\n
        \n
        - Ben"""

msg = MIMEMultipart() # Initialises MIME
msg["From"] = email
msg["To"] = sendToEmail
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain")) # Creating the message with type

server = smtplib.SMTP("smtp.gmail.com", 587) # Access GMAIL server and port
server.starttls() # Transport layer service = encryption protocol
server.login(email, password) # Login to sender email server
text = msg.as_string() # Attach message to variable

x = 0
while x < 2:
    server.sendmail(email, sendToEmail, text)
    print("Sent", x)
    time.sleep(1)
    x += 1

server.quit()
