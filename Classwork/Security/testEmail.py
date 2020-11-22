from sensors import Email

email = Email("sheldoncollegeiot@gmail.com", "P@ssword#1", "s06442@sheldoncollege.com", "Benjamin Bristow")

email.AttachText("This is a test for text attachment")
email.AttachFile("roomCapture.avi")
email.SendEmail()
