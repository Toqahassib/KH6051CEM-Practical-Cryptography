# KH6051CEM-Practical-Cryptography

The encrypted E-mail communication application begins with a sender creating a message on an e-mail client. The e-mail message will then be encrypted by AES encryption algorithm using a generated key from Diffie Hellman’s method. After that, it is sent to a sending mail server, also known as an MTA (Mail Transfer Agent). Following that, the MTA transfers it to the recipient's mail server, which is also an MTA. SMTP (Simple Mail Transport Protocol) is used to transfer emails between MTAs. Once the recipient received the encrypted email message, they should be able to decrypt it using the same generated key.

## Requirements

> python3

> pip install flask

> pip install pycryptodome


## Installing 

> git clone https://github.com/Toqahassib/KH6051CEM-Practical-Cryptography.git

## running 

1. Run the app.py file.
2. Visit 127.0.0.1:5000 on your browser.

## Increase the security

To increase the security of the generated secret key, change the group number of the prime number and its generator. The group numbers are - 14, 15, 16, 17, and 18. As the group number increases, the security and the time it takes to calculate the secret key increases.

1. In file sendmail.py (lines 13 & 14), change number 14 to the desired number.
2. In file decrypt.py (line 13), change number 14 to the desired number.
