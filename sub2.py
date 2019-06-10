import ssl #Is designed to create secure connection between client and server.
import sys #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
import psycopg2 
import paho.mqtt.client
import json
import numpy as np
import datetime
from random import randint
import random
import time


myConnection = psycopg2.connect(host = 'localhost', user= 'postgres', password ='laura997', dbname= 'sambil')
ListaPersonaN= []
ListaPersonaS = []

def eleccion(a):
    lista=a["personas"]
    print(lista)

    for x in lista:
        id = x["idpersona"]
        if (x["aux"]=="1"):
            AgregarListaTlf(id)
        else:
            AgregarListaNoTlf(id)
        cur = myConnection.cursor()
        cur.execute("""insert into entrada(idpersona,acceso) values(%s,1);""", id)
        myConnection.commit()

# Elige la persona que realizará las acciones 
def elegirpersona():
    numero = round(randint(0,1))
    if(numero==0):
        tam=len(ListaPersonaN)-1
        elegido = round(randint(0,tam))
        persona = ListaPersonaN[elegido]
        print("La persona elegida es ", persona)
        recorridoNo(persona)
    elif(numero==1):
        tam=len(ListaPersonaS)-1
        elegido = round(randint(0,tam))
        persona = ListaPersonaS[elegido]
        print("La persona elegida es ", persona)
        recorridoSi(persona)
    
        
# Agrega a la lista a los usuarios que no tengan telefono    
def AgregarListaNoTlf(id):
    ListaPersonaN.append(id)

# Agrega a la lista a los usuarios que tienen telefono
def AgregarListaTlf(id):
    ListaPersonaS.append(id)

# Realiza el recorrido de los usuarios que no tienen telefono
def recorridoNo(persona):
    cur = myConnection.cursor()
    cur.execute("select estado from persona where idpersona = %s;", persona)
    sel = cur.fetchone()[0]
    print("La accion elegida es:")
    print(sel)
    # La persona sale del centro comercial
    if sel==4:
        cur = myConnection.cursor()
        cur.execute("""UPDATE persona SET estado = 1 where idpersona = %s""", persona)
        myConnection.commit()
        cur.close()
    # La persona entra al centro comercial   
    elif sel==1:
        aux = round(randint(2,4))
        if aux==3:
            feria(persona)
        elif aux==2:
            comprarno(persona)
        elif aux==4:
            salir(persona)
    # La persona compra 
    elif sel==2:
            aux2 = round(randint(3,4))
            if aux2 == 3:
                feria(persona)
            elif aux2 == 4:
                salir(persona)
    # La persona entra en feria 
    elif sel ==3:
            cur = myConnection.cursor()
            cur.execute("""INSERT INTO ocupacion(idpersona, estado, idmesa) values(1,0,1); """)
            myConnection.commit()
            cur.close()
            aux3 = random.choice((2,4))
            if aux3 == 2:
                comprarno(persona)
            elif aux3 == 4:
                salir(persona)

# Recorrido que realiza la persona que si tiene telfono
def recorridoSi(persona):
    cur = myConnection.cursor()
    cur.execute("select estado from persona where idpersona = %s;", persona)
    sel = cur.fetchone()[0]
    print("La accion elegida es:")
    print(sel)
    # La persona sale del centro comercial
    if sel==4:
        cur = myConnection.cursor()
        cur.execute("""UPDATE persona SET estado = 1 where idpersona = %s""", persona)
        myConnection.commit()
        cur.close()
    # La persona entra al centro comercial      
    elif sel==1:
        aux = round(randint(2,4))
        if aux==3:
            feria(persona)
        elif aux==2:
            comprarSi(persona)
        elif aux==4:
            salir(persona)
    # La persona compra 
    elif sel==2:
            aux2 = round(randint(3,4))
            if aux2 == 3:
                feria(persona)
            elif aux2 == 4:
                salir(persona)
    # La persona entra en feria
    elif sel ==3:
            cur = myConnection.cursor()
            cur.execute("""INSERT INTO ocupacion(idpersona, estado, idmesa) values(%s,0,1); """,persona)
            cur.execute("UPDATE mesa set estado=0 where idmesa=1")
            myConnection.commit()
            cur.close()
            aux3 = random.choice((2,4))
            if aux3 == 2:
                comprarSi(persona)
            elif aux3 == 4:
                salir(persona)



# Funcion que permite al usuario salir del centro comercial               
def salir(persona):
    print("La persona salio del centro comercial")
    cur = myConnection.cursor()
    print(persona)
    cur.execute("""UPDATE persona SET estado = 4  where idpersona = %s;""", persona)
    myConnection.commit()
    cur.close()

# Funcion que permite al usuario entrar y salir de la feria del centro comercial
def feria(persona):
    mesa=1
    print("La persona entro en la feria")
    cur = myConnection.cursor()
    cur.execute("""UPDATE persona SET estado = 3  where idpersona = %s;""", persona)
    myConnection.commit()
    cur.close()
    cur = myConnection.cursor()
    cur.execute("select count(idmesa) from mesa where estado = 0;")
    select = cur.fetchone()[0]
    print(select)
    if select==1:
        cur.execute("select idmesa from mesa where estado = 0;")
        sel = cur.fetchone()[0]
        print("La persona elegida es:")
        print(sel)
        cur = myConnection.cursor()
        cur.execute("""UPDATE mesa SET estado = 1 where idmesa=1; """)
        myConnection.commit()
        cur.close()
        cur = myConnection.cursor()
        # Procedimiento almacenado
        cur.execute(" select ocupacion_sentado(%s,%s) ",(persona,mesa))
        myConnection.commit()
        cur.close()
    recorridoNo(persona)

def probando():
    cur = myConnection.cursor()
    cur.execute("""INSERT INTO ocupacion(idpersona, estado, idmesa) values(1,0,1); """)
    myConnection.commit()
    cur.close()
    
# Funcion que permite a los usuarios que no tienen telefono hacer una compra
def comprarno(id):
    #Simular las columnas que tengan 
    #Monto
    print("Persona sin telefono realizo una compra")
    idcomprano = 1
    idtienda = 1
    monto = round(randint(1000,5000))
    print("Monto de la compra")
    print(monto)
    #Random entre 5000 y un millon
    cur = myConnection.cursor()

    # Procedimiento almacenado
    cur.execute("select comprar_no(%s,%s,%s);",(idtienda, id, monto))
    myConnection.commit()

# Funcion que permite a los usuarios que  tienen telefono hacer una compra
def comprarSi(id):
    #Simular las columnas que tengan 
    #Monto
    print("Persona con telefono realizo una compra")
    idcomprano = 1
    idtienda = 1
    monto = round(randint(1000,5000))
    print("Monto de la compra")
    print(monto)
    #Random entre 5000 y un millon
    cur = myConnection.cursor()

    #Procedimiento almacenado
    cur.execute("select comprar_si(%s,%s,%s);",(idtienda, id, monto))
    myConnection.commit()

# Conexion
def on_connect(client, userdata, flags, rc):    
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='unimet/#', qos = 0)        

def on_message(client, userdata, message):   
   a = json.loads(message.payload)
   print(a) 
   print(message.qos)   
   print('------------------------------')  
   eleccion(a) 
   print("Personas sin telefono: ")
   print(ListaPersonaN)
   print("Personas con telefono: ")
   print(ListaPersonaS)
   sen = True
   while sen==True:
     elegirpersona()
     time.sleep(1)


# MAIN
def main():	
    try:
        client = paho.mqtt.client.Client(client_id='Bug_Dou', clean_session=False)
        client.on_connect = on_connect
        print("----")
        client.message_callback_add('unimet/admin/bd', on_message)
        client.connect(host='localhost') 
        client.loop_forever()
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Ha ocurrido un error", error)
       


if __name__ == '__main__':
	main()
	sys.exit(0)