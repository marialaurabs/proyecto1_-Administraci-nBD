READ ME:

Proyecto de administraci�n de base de datos:

Para poder visualizar correctamente el funcionamiento del proyecto debe seguir los siguientes pasos:

1.  Descargar el proyecto en forma de archivo comprimido y extraerlo.
2.  Ejecutar pgAdmin.
3.  Importar la base de datos  �sambil.sql� y cambiar la clave en el archivo sub2.py.
4.  Abrir dos cmd en el editor de c�digo de su preferencia.
4.1 En el primero debe ejecutar el comando sub2.py.
4.2 Posteriormente en el segundo debe ejecutar el comando pub2.py.
5.  A continuaci�n podr� visualizar las salidas en la cmd.
6.  Si desea parar la ejecuci�n del proyecto solo debe hacer ctrl+c en la cmd donde previamente ejecut� el sub2.py.

Si desea ver los datos que fueron generados e insertados en postgreSQL debe ir a las propiedades de las tablas deseadas y verificar, tambi�n podr� visualizar el c�digo de los procedimientos almacenados las vistas y los triggers.

Gr�ficas:

1.  Abrir el archivo en Jupyter notebook.
2.  Ingresar el usuario y contrase�a de PostgreSQL
3.  Ejecutar 

Librerias que se deben instalar:
import ssl 
import sys 
import psycopg2 
import paho.mqtt.client
import json
import numpy as np
import datetime
from random import randint
import random
import time