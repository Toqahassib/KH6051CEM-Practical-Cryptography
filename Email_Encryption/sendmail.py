from flask import flash
import smtplib
from smtplib import SMTPRecipientsRefused
import ssl
from email.message import EmailMessage
import os
# importing AES
from Crypto.Cipher import AES
# importing groups for diffie hellman
from DHE_groups import groups

P = groups[14][1]
G = groups[14][0]

# private key
private_key = eval(os.environ.get("private_key"))

# define email data
sender = 'toqahassib@gmail.com'
password = os.environ.get("EMAIL_PASS")


def SendMail(receiver, subject, body):
    public_key = int(pow(G, private_key, P))
    secret_key = str(pow(public_key, private_key, P))[0:32].encode()

    # create new instance of cipher
    cipher = AES.new(secret_key, AES.MODE_EAX)

    nonce = cipher.nonce

    encrypted_msg, tag = cipher.encrypt_and_digest(body.encode())
    print(tag)
    print("\n", encrypted_msg)

    content = "Encrypted msg is: {} \nTag is: {} \nnonce is: {} \nPublic Key is: {}".format(
        encrypted_msg, tag, nonce, public_key)

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


SendMail('test', 'test', 'test')
