import os
import smtplib
from email.message import EmailMessage


email_password = "rvkoknkeqypveimr"
email_username = "chris.warren.2019@gmail.com"
msg = EmailMessage()

msg["Subject"] = "Test Message"
msg["From"] = email_username
msg["To"] = "pytest@mailinator.com"
msg.set_content("This is a test message that is being sent out to test the program we're building.")

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
    smtp.set_debuglevel(2)
    smtp.login(email_username, email_password)
    smtp.send_message(msg)