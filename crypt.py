"""Enviar e Receber Mensagens Criptografadas"""

# 253612

from random import sample
from json import dumps, dump, load
from qrcode import make
from datetime import datetime
from PIL import Image
from pyzbar.pyzbar import decode
from ast import literal_eval
from os import listdir, remove
from alphabet import ALPHABET

class Crypt(object):
	"""docstring for Crypt"""
	def __init__(self):
		super(Crypt, self).__init__()
		self.numbers = list(range(10, 99))
		self.alphabet = ALPHABET

	def with_random_token(self, text: str):

		token = sample(self.numbers, 3)

		token = int(''.join([str(i) for i in token]))

		full_text = []

		for word in text.lower():

			word = ''.join([str(self.alphabet.get(i)*token) for i in word][0])

			full_text.append(word)

		encrypt_text = {
			'encrypt_text': full_text
		}

		qrcode_image_data = make(encrypt_text)

		path_image = 'qrcodes/' + str(int(datetime.now().timestamp())) + '.png'

		qrcode_image_data.save(
			path_image
		)

		with open('logs/logs.json', 'r') as file:

			data = load(file)

		data.append({
			'token': token,
			'pathimage': path_image,
		})

		with open('logs/logs.json', 'w') as file:

			dump(data, file, indent = 2)

		return {'token': token}

	def decrypt_text(self, path: str, token: str):

		data_image = literal_eval(decode(Image.open(path))[0].data.decode('ascii'))

		reversed_alphabet = dict(map(reversed, self.alphabet.items()))

		text = ''.join([reversed_alphabet.get(int(i)/int(token)) for i in data_image['encrypt_text']])

		return text

	def list_all_messages(self):
		
		with open('logs/logs.json', 'r') as file:

			data = load(file)

		return dumps(data, indent = 2)

	def delete_and_reset_all_messages(self):

		for i in listdir('qrcodes/'):

			remove('qrcodes/' + i)

		remove('logs/logs.json')

		data = []

		with open('logs/logs.json', 'w') as file:

			dump(data, file, indent = 2)

		return None
