import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from random import randint

def on_connect(client, userdata, flags, rc):
	print('connected')

def main():
	client = paho.mqtt.client.Client("Unimet", False)
	client.qos = 0
	client.connect(host='localhost')
    
	
	payload = {
        "personas" : [
            {"idpersona":"1", "edad":"20", "sexo":"masculino", "macaddress":"3001", "estado":"1", "aux":"1"}, 
            {"idpersona":"2", "edad":"30", "sexo":"femenino", "macaddress":"3002", "estado":"1", "aux" :"1"},
            {"idpersona":"3", "edad":"40", "sexo":"femenino", "macaddress":"3003", "estado":"1", "aux":"1"},
            {"idpersona":"4", "edad":"50", "sexo":"femenino", "macaddress":"3004", "estado":"1", "aux":"0"},
            {"idpersona":"5", "edad":"60", "sexo":"masculino", "macaddress":"3005", "estado":"1", "aux":"0"},
            {"idpersona":"6", "edad":"15", "sexo":"masculino", "macaddress":"3006", "estado":"1", "aux":"1"}, 
            {"idpersona":"7", "edad":"35", "sexo":"femenino", "macaddress":"3007", "estado":"1", "aux" :"1"},
            {"idpersona":"8", "edad":"40", "sexo":"femenino", "macaddress":"3008", "estado":"1", "aux":"1"},
            {"idpersona":"9", "edad":"52", "sexo":"femenino", "macaddress":"3009", "estado":"1", "aux":"0"}
        ]
    }

	client.publish('unimet/admin/bd',json.dumps(payload),qos=0)

if __name__ == '__main__':
	main()
	sys.exit(0)
