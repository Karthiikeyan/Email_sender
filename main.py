from email.message import EmailMessage
import smtplib
import ssl
from quotes import quote
import random

mail = EmailMessage()
my_email = "YOUR MAIL ID"
password = "ENTER PASSWORD"

subject = "Morning Motivation"
body = random.choice(quote)
receive_mail = 'RECIEVER EMAIL'

mail['From'] = my_email
mail['To'] = receive_mail
mail['subject'] = subject
mail.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:

    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email, to_addrs=receive_mail, msg=mail.as_string())



