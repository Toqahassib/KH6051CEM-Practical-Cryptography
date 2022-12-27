# KH6051CEM-Practical-Cryptography

The encrypted E-mail communication application begins with a sender creating a message on an e-mail client. The e-mail message will then be encrypted by AES encryption algorithm using a generated key from Diffie Hellman’s method. After that, it is sent to a sending mail server, also known as an MTA (Mail Transfer Agent). Following that, the MTA transfers it to the recipient's mail server, which is also an MTA. SMTP (Simple Mail Transport Protocol) is used to transfer emails between MTAs. Once the recipient received the encrypted email message, they should be able to decrypt it using the same generated key.

## Requirements


## Installing 

> git clone https://github.com/Toqahassib/KH6051CEM-Practical-Cryptography/

## running 

1. Run the app.py file.
2. Visit 127.0.0.1:5000 on your browser.
