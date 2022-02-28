
#!/usr/bin/env python3

from Crypto.Cipher import DES

plaintext = "Python rocks!"

key = "12345678"

def padding(plaintext):
	while len(plaintext) % 8 != 0:
		plaintext = plaintext + " "
	return plaintext

plaintext = padding(plaintext)

des = DES.new(key, DES.MODE_ECB)

cyphertext = des.encrypt(plaintext)
print(cyphertext)

plaintext = des.decrypt(cyphertext)
print(plaintext)
