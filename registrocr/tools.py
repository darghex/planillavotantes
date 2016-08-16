from settings import BASE_DIR

def send_sms():
	from elibom.Client import *
	import csv
	ACCOUNT = 'niwradsax@gmail.com'
	PASSWORD = 'dYFFzAgEXS'
	SMS = 'Este domingo apoyame con tu VOTO por el equipo de CAMBIO RADICAL: Mauricio-Alcalde, Jaramillo-Gobernador, Maya-Diputado CR 51 y por mi, al Concejo MAXJONNY CR 1'
	PHONE_FILE = "%s/phones.csv" % BASE_DIR
	elibom = ElibomClient(ACCOUNT, PASSWORD)
	
	f = open(PHONE_FILE)
	import pdb
	pdb.set_trace()	
	reader = csv.reader(f)
	for row in reader:
		try:
			response = elibom.send_message("57%s" % row[0], SMS)
			print "Enviado a %s" % row[0]
		except:
			print "Error al enviar %s" % row[0]

	f.close()
	