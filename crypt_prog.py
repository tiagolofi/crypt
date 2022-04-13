
from crypt import Crypt

crypter = Crypt()

while True:

	print('1. Deseja criar ou ler uma mensagem criptografada?\n')

	route = str(input('2. Y (criar nova mensagem) ou R (ler mensagem) ou N (fechar programa)\n\n'))
	
	if route == 'Y':

		message = str(input('\nMensagem: '))

		try:

			print(crypter.with_random_token(text = message), '\n\n')

			print('OBS: Lembre-se de salvar o token acima.\n')


		except:

			print('\nErro: caracteres como acentos, números e letras maiúsculas não são aceitos.\n')

			pass

	elif route == 'R':

		path = str(input('\nCaminho para a imagem: '))

		token = str(input('Token: '))

		try:

			print('\n', crypter.decrypt_text(path = path, token = token), '\n')

		except:

			print('\nToken ou Caminho para a imagem podem estar incorretos.\n')

			pass

	elif route == 'N':

		break

	else:

		print('\nErro: comando não encontrado!\n')