from flask import flash
import smtplib
from smtplib import SMTPRecipientsRefused
import ssl
from email.message import EmailMessage
import os
# import aes algorithm
from Crypto.Cipher import AES
# import RFC defined groups for DHE
from DHE_groups import groups

# define prime number and generate for DHE key exchange
P = groups[14][1]
G = groups[14][0]

# get my private key
private_key = eval(os.environ.get("alice_private_key"))

# define email and password of the sender's email
sender = 'toqahassib@gmail.com'
password = os.environ.get("EMAIL_PASS")


def SendMail(receiver, subject, body):
    # calculate my public key using my private key received and the prime and the generator numbers
    alice_public_key = int(pow(G, private_key, P))
    bob_public_key = eval(os.environ.get("bob_public_key"))

    # calculate the secret key using my public key received and my private key
    secret_key = str(pow(bob_public_key, private_key, P))[0:32].encode()

    # create new cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_EAX)
    # create the nonce
    nonce = cipher.nonce

    # encrypt and digest the message
    encrypted_msg, tag = cipher.encrypt_and_digest(body.encode())
    content = "Encrypted msg is: {} \nTag is: {} \nnonce is: {} \nPublic Key is: {}".format(
        encrypted_msg, tag, nonce, alice_public_key)

    # set the email contents
    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)

    # add ssl layer
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            # login and send the email
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email.as_string())

        flash("Mail Sent Successfully!", "success")
    except SMTPRecipientsRefused:
        flash("The email address '{}' is not valid".format(
            receiver), "error")
