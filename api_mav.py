from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz # pip install python-dateutil
import sys


API = IQ_Option('lucasncborges@gmail.com', 'contateste')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL

while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		
		API.connect()
	else:
		print('\n\nConectado com sucesso')
		break
	
	time.sleep(1)

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

def timestamp_converter(x, retorno = 1):
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6] if retorno == 1 else hora.astimezone(tz.gettz('America/Sao Paulo'))



x = perfil()
print('Email: ' +  x['email'])
print('Nickname: ' + x['nickname'])
print('Moeda: ' + x['currency'])
print('Conta criada em: ' + timestamp_converter(x['created']))