from flask import flash
import smtplib
from smtplib import SMTPRecipientsRefused
import ssl
from email.message import EmailMessage
import os
# importing AES
from Crypto.Cipher import AES


# encryption key
key = b'C&F)H@McQfTjWnZr'

# define email data
sender = 'toqahassib@gmail.com'
password = os.environ.get("EMAIL_PASS")


def SendMail(receiver, subject, body):
    # create new instance of cipher
    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce

    encrypted_msg, tag = cipher.encrypt_and_digest(body.encode())

    content = "Encrypted msg is: {} \nTag is: {} \nnonce is: {}".format(
        encrypted_msg, tag, nonce)

    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)

    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email.as_string())

        flash("Mail Sent Successfully!", "success")
    except SMTPRecipientsRefused:
        flash("The email address '{}' is not valid".format(
            receiver), "error")
