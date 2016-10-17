import string
import base64
upper_base_alpha =string.ascii_uppercase
low_base_alpha = string.ascii_lowercase
#a = open('ex4_1_data.txt')
#cipher_string = a.read()
#def cipherconverter(cipher_string):
from Crypto.Cipher import DES, AES
from hashlib import md5

def main():
	key = md5('hippopotamus').hexdigest()
	a=''
	with open('ex4_1_data.txt') as fin:
		a = fin.read()
#	for i in xrange(len('upper_base__alpha'))   :only needed for the caesarDecode function.
#		caesarOutput = caesarDecode(a, i)   :only needed for the caesarDecode function.	
		caesarOutput = caesarDecode(a, 6)

		atbashOutput = atbashConvert(caesarOutput)

		base64Output = base64Convert(atbashOutput)

		strippedB64output = base64Output.split(': ')[1]

		print len(strippedB64output)

		aes128Output = aes128Convert(strippedB64output, key)
#	print(caesarOutput)
#	print(atbashOutput)
	print(aes128Output)

def caesarEncode(data, shift):
	result=''
	for letter in data:
        	if letter.isupper():
			#use .find() to pull down the place number of the character
                	start_position = string.ascii_uppercase.find(letter)
			#move the position by subtracting a number
                	encoded_position = (start_position + shift) % 26
			result += upper_base_alpha[encoded_position]
		elif letter.islower():
			start_position = string.ascii_lowercase.find(letter)
			encoded_position = (start_position + shift) % 26
			result += low_base_alpha[encoded_position]
		else:
			result += letter
	return result

def caesarDecode(data, shift):
	return caesarEncode(data, shift * -1)




def atbashConvert(data):
	result = ''
	for letter in data:
#		print('in function')
		if letter.isupper():
			base_position = string.ascii_uppercase.find(letter)
			encoded_position = ((base_position + 1) * -1)
			result += string.ascii_uppercase[encoded_position]
		elif letter.islower():
			base_position = string.ascii_lowercase.find(letter)
			encoded_position = ((base_position + 1) * -1)
			result += string.ascii_lowercase[encoded_position]
		else:
			result += letter
	return result


def base64Convert(data):
	stripped_data = data[287:] #take input from atbash starting at correct point
	decoded_data = base64.b64decode(stripped_data)
	return decoded_data

def aes128Convert(data, key):
	aes = AES.new(key)
	return aes.decrypt(data)		
#use the md5 hash of the word hippo, encrypt it using aes 128, use that output as the decrypt key for the 
#encrypted data the word hippo to get the key

if __name__ == '__main__':
	main()

