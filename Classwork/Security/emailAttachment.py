import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

fileLocation = 'C:\\Users\\benja\\Documents\\Github\\DigitalSolutions2020\\Classwork\\Security\\Capture.png'
email = "sheldoncollegeiot@gmail.com"
password = "P@ssword#1"
sendToEmail = "s06442@sheldoncollege.com"
subject = "Benjamin Bristow"
message = "Hi this is a message"

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = sendToEmail
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain", "utf-8"))

filename = os.path.basename(fileLocation)
with open(fileLocation, "rb") as file:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='img1.png')

    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')

    # read attachment file content into the MIMEBase object
    mime.set_payload(file.read())

    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, sendToEmail, text)
server.quit()