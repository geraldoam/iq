from iqoptionapi.stable_api import IQ_Option
import logging
import time
import os
import sys

# Error Password 
error_password="""{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""


# Logo do CLI
def bannerProject():
	os.system("cls")
	print("""


  _                     _   _             
 (_)                   | | (_)            
  _  __ _    ___  _ __ | |_ _  ___  _ __  
 | |/ _` |  / _ \| '_ \| __| |/ _ \| '_ \ 
 | | (_| | | (_) | |_) | |_| | (_) | | | |
 |_|\__, |  \___/| .__/ \__|_|\___/|_| |_|
       | |       | |                      
       |_|       |_|                      

                                                        
[ Bem vindo a sua consulta com o Robô IQ Option ]

""")


def consultInformation():
	print("""> Olá, seja bem vindo ao protótipo de teste do BOT.
	> Por favor, preencha os dados. \n""")

	print("\n[LOGIN] Seu email:")
	email = input()

	print("\n[LOGIN] Sua senha:")
	password = input()

	return email, password


def apiConnect(email, password):
	I_want_money = IQ_Option(email, password)
	while_run_time=10
	check,reason=I_want_money.connect()	

	return I_want_money, while_run_time, check, reason


def apiLogin(I_want_money, while_run_time, check, reason):
	if check:
		print("\n\n\n[CONECTADO] Bem vindo! Robô iniciado.")
	while True: 
		if I_want_money.check_connect()==False:#detect the websocket is close
			print("Tentando reconectar...")
			check,reason=I_want_money.connect()         
		if check:
			# Parâmetros pós conectado
			totalDinheiro = I_want_money.get_balance()
			print("""\n\n[PAINEL DE CONTROLE]""")
			print("\n[SALDO] " + str(totalDinheiro))
			print("[MOEDA] " + str(I_want_money.get_currency()))
			time.sleep(1000)
		else:
			if reason==error_password:
				print("Erro! Senha inválida.")
			else:
				print("Sem conexão com internet!")

	else:

		if reason=="[Errno -2] Name or service not known":
			print("Sem conexão com internet!")
		elif reason==error_password:
			print("Erro! Senha inválida.")



# Chama as Funções

bannerProject()
email, password = consultInformation()
I_want_money, while_run_time, check, reason = apiConnect(email, password)
apiLogin(I_want_money, while_run_time, check, reason)