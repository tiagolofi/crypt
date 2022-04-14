"""Programa de criptografia baseado em QRCODE ver. 0.0.1"""

from crypt import Crypt

crypter = Crypt()

while True:

	print('1. Deseja criar ou ler uma mensagem criptografada?\n')

	route = str(input('2. Y (criar nova mensagem), R (ler mensagem), L (listar mensagens), D (deletar todas as mensagens) ou N (fechar programa)\n\n'))
	
	if route == 'Y':

		message = str(input('\nMensagem: '))

		try:

			print(crypter.with_random_token(text = message), '\n\n')

			print('OBS: Lembre-se de salvar o token acima.\n')

		except:

			print('\nErro: caracteres como acentos e números não são aceitos.\n')

			pass

	elif route == 'R':

		path = str(input('\nCaminho para a imagem: '))

		token = str(input('Token: '))

		try:

			print('\n', crypter.decrypt_text(path = path, token = token), '\n')

		except:

			print('\nToken ou Caminho para a imagem podem estar incorretos.\n')

			pass

	elif route == 'L':

		messages = crypter.list_all_messages()

		if len(messages) == 0:

			print('\nNenhuma mensagem foi criada.\n')

		else:

			print('\n', messages, '\n')

	elif route == 'D':

		try:

			crypter.delete_and_reset_all_messages()
			
			print('\nTodas as mensagens foram excluídas.\n')

		except:
		
			print('\nErro ao tentar excluir mensagens!\n')

	elif route == 'N':

		break

	else:

		print('\nErro: comando não encontrado!\n')