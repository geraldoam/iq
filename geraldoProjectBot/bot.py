from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz # pip install python-dateutil
import sys
import fileinput
import os
import getpass

############################################################################################
# Erro de Password, Ignora isso.
############################################################################################
error_password="""{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""
############################################################################################




############################################################################################
# Banner do CLI
############################################################################################
def bannerProject():
	os.system("cls")
	print("""


.______        ______   .______     ______          __         
|   _  \      /  __  \  |   _  \   /  __  \        |  |    _   
|  |_)  |    |  |  |  | |  |_)  | |  |  |  |       |  |  _| |_ 
|      /     |  |  |  | |   _  <  |  |  |  |       |  | |_   _|
|  |\  \----.|  `--'  | |  |_)  | |  `--'  |       |  |   |_|  
| _| `._____| \______/  |______/   \______/        |__|        
                                                               

                                              

""")
############################################################################################
############################################################################################



############################################################################################
# Pergunta o Email e Senha do Usuário
############################################################################################
def consultInformation():
	print("""[] Seja bem vindo ao seu robô I+.
[] Por favor, preencha os dados abaixo. \n""")

	print("\n[ LOGIN ] Seu email:")
	email = input()

	print("\n[ LOGIN ] Sua senha:")
	password = getpass.getpass('')


	return email, password
############################################################################################




############################################################################################
# Conecta o Usuário com a API
############################################################################################
def apiConnect(email, password):
	API = IQ_Option(email, password)
	while_run_time=10
	check,reason=API.connect()	

	API.change_balance("PRACTICE")

	return API, while_run_time, check, reason
############################################################################################




############################################################################################
# Consulta informações do usuário na API (Copiei do MAV mesmo KKKKKKKKKK)
############################################################################################
def perfil():
	perfil = json.loads(json.dumps(API.get_profile_ansyc()))
	
	return perfil
	
	'''
		name
		first_name
		last_name
		email
		city
		nickname
		currency
		currency_char 
		address
		created
		postal_index
		gender
		birthdate
		balance		
	'''
############################################################################################




############################################################################################
# Carrega a lista de sinais com o arquivo (sinais.txt)
############################################################################################
def carregar_sinais():
	arquivo = open('sinais.txt', encoding='UTF-8')
	lista = arquivo.read()
	arquivo.close

	lista = lista.split('\n')

	for index,a in enumerate(lista):
		if not a.rstrip():
			del lista[index]

	return lista
############################################################################################



############################################################################################
# Painel de Controle Principal
############################################################################################
def painelControle(credencialPerfil):
	print("""\n\n

                                                                 
	         _         _      _                    _           _     
	 ___ ___|_|___ ___| |   _| |___    ___ ___ ___| |_ ___ ___| |___ 
	| . | .'| |   | -_| |  | . | -_|  |  _| . |   |  _|  _| . | | -_|
	|  _|__,|_|_|_|___|_|  |___|___|  |___|___|_|_|_| |_| |___|_|___|
	|_|                                                              


""")

	print("""	---------------------------------------------------------------------""")
	print("  			Seja bem vindo " + str(credencialPerfil['name']) + ".	")
	print("  			Você tem um total de " + str(credencialPerfil['balance']) + " na sua conta.")
	print("  			Atualmente sua moeda é " + str(credencialPerfil['currency']) + ".")
	print("""	---------------------------------------------------------------------""")
############################################################################################



############################################################################################
# A opção do menu abaixo do Painel de Controle
############################################################################################
def switchControlPainel():
	print("  			Para continuar selecione uma opção.\n")
	print("""  			[ Digite 1 ] Para usar o arquivo \"sinais.txt\".""")
	print("""	---------------------------------------------------------------------""")
	switchControlPainelOption = int(input())

	return switchControlPainelOption
############################################################################################



############################################################################################
# Abre o arquivo sinais.txt e lê, transforma em JSON
############################################################################################
def lerSinais(lista):
	json.dumps(carregar_sinais(), indent=1)

	lista = carregar_sinais()

	contLine = 1

	for sinal in lista:
		dados = sinal.split(', ')

		# Contador de Linhas

		os.system("cls || clear")
		print("\n\n[ TUDO CERTO ] Lendo arquivo.... \n \n")

		time.sleep(2)

		print("Informações da " + str(contLine) + "º linha. \n")

		print("Você selecionou para comprar no dia " + str(dados[0]) + ".")
		print("Na hora " + str(dados[1]) + ".") 
		print("Com a paridade " + str(dados[2]) + ".") 
		print("Duração de " + str(dados[3]) + ".") 
		print("Com " + str(dados[4]) + " de entrada.") 
		print("Com direção " + str(dados[5]) + ".")
		contLine += 1 
		input()
############################################################################################



############################################################################################
# Chama as funções acima, isso aqui é a parte do Login e verificação dos Dados
############################################################################################
bannerProject()
email, password = consultInformation()
API, while_run_time, check, reason = apiConnect(email, password)
############################################################################################



############################################################################################
# Se a conexão com a API for True, ele obedece esse bloco.
############################################################################################
if check:
	os.system("cls || clear")
	print("\n\n[ CONECTADO ] Bem vindo! Aguarde....")
	time.sleep(3)
while True: 
	if API.check_connect()==False:#detect the websocket is close
		print("Tentando reconectar...")
		check,reason=API.connect()         
	if check:
		os.system("cls || clear")
		# Parâmetros pós conectado

		credencialPerfil = perfil()
		painelControle(credencialPerfil)

		time.sleep(2)

		switchControlPainelOption = switchControlPainel()

		if switchControlPainelOption == 1:
			time.sleep(3)
			# Chama a função
			lista = carregar_sinais()
			lerSinais(lista)

		print("\n\n\nAcabaram todas as linhas. Obrigado por usar o Bot.")
		exit()
	else:
		if reason==error_password:
			print("Erro! Senha inválida.")
			exit()
		else:
			print("Sem conexão com internet!")
			exit()

else:

	if reason=="[Errno -2] Name or service not known":
		print("Sem conexão com internet!")
	elif reason==error_password:
		print("Erro! Senha inválida.")

