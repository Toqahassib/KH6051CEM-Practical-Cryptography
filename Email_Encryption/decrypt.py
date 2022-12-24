# importing AES
from flask import flash
from Crypto.Cipher import AES

key = b'C&F)H@McQfTjWnZr'


def Decrypt(body, tag, nonce):
    # generate new instance with the key and nonce same as encryption cipher
    cipher = AES.new(key, AES.MODE_EAX,
                     nonce)
    # decrypt the data
    plaintext = cipher.decrypt(body)

    try:
        cipher.verify(tag)
        flash("The message is authentic: {}".format(
            plaintext.decode()), "success")

    except ValueError:
        flash("Key incorrect or message corrupted", "error")
