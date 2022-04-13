"""Enviar e Receber Mensagens Criptografadas"""

from random import sample
from json import dumps
from qrcode import make
from datetime import datetime
from PIL import Image
from pyzbar.pyzbar import decode
from ast import literal_eval

class Crypt(object):
	"""docstring for Crypt"""
	def __init__(self):
		super(Crypt, self).__init__()
		self.numbers = list(range(10, 99))
		self.alphabet = {
			'a': 40, 'b': 3, 'c': 91, 
			'd': 73, 'e': 25, 'f': 61, 
			'g': 84, 'h': 92, 'i': 83, 
			'j': 60, 'k': 53, 'l': 23,
			'm': 13, 'n': 31, 'o': 12, 
			'p': 20, 'q': 51, 'r': 6, 
			's': 49, 't': 57, 'u': 18, 
			'v': 8, 'w': 19, 'x': 24, 
			'y': 80, 'z': 14, ' ': 27
		}

	def with_random_token(self, text: str):

		token = sample(self.numbers, 3)

		token = int(''.join([str(i) for i in token]))

		full_text = []

		for word in text:

			word = ''.join([str(self.alphabet.get(i)*token) for i in word][0])

			full_text.append(word)

		encrypt_text = {
			'encrypt_text': full_text
		}

		qrcode_image_data = make(encrypt_text)

		qrcode_image_data.save(
			'qrcodes/' + str(token) + ' - ' + str(int(datetime.now().timestamp())) + '.png'
		)

		return {'token': token}

	def decrypt_text(self, path: str, token: str):

		data_image = literal_eval(decode(Image.open(path))[0].data.decode('ascii'))

		reversed_alphabet = dict(map(reversed, self.alphabet.items()))

		text = ''.join([reversed_alphabet.get(int(i)/int(token)) for i in data_image['encrypt_text']])

		return text
