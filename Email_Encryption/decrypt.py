from flask import flash
from Crypto.Cipher import AES
import os
# import RFC defined groups for DHE
from DHE_groups import groups

# get private key
private_key = eval(os.environ.get("bob_private_key"))


def key(public_key):
    # define prime num for DHE
    P = groups[14][1]

    # calculate the secret key using public key received and my private key
    secret_key = str(pow(public_key, private_key, P))[0:32].encode()
    return secret_key


def Decrypt(key, body, tag, nonce):
    # create the cipher using the same key and nonce as encryption
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    # decrypt the message
    plaintext = cipher.decrypt(body)

    try:
        # verify the msg's authenticity
        cipher.verify(tag)
        flash("The message is authentic: {}".format(
            plaintext.decode()), "success")

    except ValueError:
        flash("Key incorrect or message corrupted", "error")
