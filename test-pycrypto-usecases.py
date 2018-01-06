#!/usr/bin/python
# -*- coding: utf-8 -*-
import Crypto

def encrypt(plaintext, key):
   from Crypto.Cipher import Blowfish as blow

   b = blow.new(key)
   LIM=8 #might have to change if we chose to use a different cipher or block size
   #nice pad soln: https://stackoverflow.com/a/32311090
   pad = lambda s: s + (LIM - len(s) % LIM) * chr(LIM - len(s) % LIM)
   return b.encrypt(pad(plaintext))

def decrypt(ciphertext, key):
   from Crypto.Cipher import Blowfish as blow

   b = blow.new(key)
   LIM=8 #might have to change if we chose to use a different cipher or block size
   unpad = lambda s : s[:-ord(s[len(s)-1:])]
   return unpad(b.decrypt(ciphertext))


def generate_and_store_key_to_file(password):
    keydir = './key'

    import hashlib
    LIM = 16
    MASTER_KEY = 'MASTER_KEY'
    key = hashlib.md5(MASTER_KEY).hexdigest()[:LIM]
    encrypted_key = encrypt(key, password)  # using encrypt() from Task#1
    FILE = 'KEY.KEY'
    with open("{:s}/{:s}".format(keydir, FILE), 'w+') as f:
        f.write(encrypted_key)

    return True

def read_key_from_file(password):
   keydir = "./key"

   # This is where your code goes.
   FILE='KEY.KEY'
   with open("{:s}/{:s}".format(keydir, FILE), "r") as f:
       return decrypt(f.read(), password)

   return None


# This is to test the code for this task.
key = "MASTER KEY" # the encryption key goes here!
plaintext = "I am at the harbor and I am witnessing human trafficking."

ciphertext = encrypt(plaintext, key)
assert plaintext != ciphertext
decrypted = decrypt(ciphertext, key)
assert plaintext == decrypted

print "IN:{:s} | EN: {:s} | DE: {:s} | KEY: {:s}".format(plaintext, ciphertext, decrypted, key)

print "Task completed! Please continue."


# This is to test the code for this task.
assert generate_and_store_key_to_file("secretpassword")
assert read_key_from_file("secretpassword")
print read_key_from_file("secretpassword")
print "FINAL Task completed! Please continue."
