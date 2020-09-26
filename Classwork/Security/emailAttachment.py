import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog

email = "sheldoncollegeiot@gmail.com"
password = "P@ssword#1"
sendToEmail = "s06442@sheldoncollege.com"

msg = MIMEMultipart()
msg["Subject"] = "Benjamin Bristow"
msg["From"] = email
msg["To"] = sendToEmail

text = "Hi this is a message"
msg.attach(MIMEText(text, "plain"))

filename = filedialog.askopenfilename(initialdir = "/", title = "Select Attachment File", filetypes=[("All", "*.*")])
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