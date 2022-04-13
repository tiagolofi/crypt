
from crypt import Crypt

crypter = Crypt()

while True:

	print('Deseja criar ou ler uma mensagem criptografada?\n\n')

	route1 = str(input('Y (criar nova mensagem) ou R (ler mensagem) ou N (fechar programa)\n\n'))
	
	if route1 == 'Y':

		message = str(input('Mensagem: '))

		print(crypter.with_random_token(text = message), '\n\n')

		print('Lembre-se de salvar o token acima.\n')

	elif route1 == 'R':

		path = str(input('Caminho para a imagem: '))

		token = str(input('Token: '))

		print(crypter.decrypt_text(path = path, token = token))

	elif route1 == 'N':

		break

	else:

		print('Comando não encontrado')