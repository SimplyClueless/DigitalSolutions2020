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

msg.attach(MIMEText(message, "plain"))

filename = os.path.basename(fileLocation)
with open(fileLocation, "rb") as file:
    attachment = file.read()
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment)
part.add_header("Content-Disposition", "attachment; filename=%s" % filename)

msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, sendToEmail, text)
server.quit()