import socket
import hmac
import random
import aperturaBaseDatos
from datetime import datetime

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
def l(v):
    clave = "1234"
    hmacServer = hmac.hmacFuncion(gen_prueba_random(v)[0][0], clave)  # type: ignore
    return hmacServer

def gen_prueba_random(cadena):
    v = random.random()
    x= cadena.split(" ")
    if(v > 0.65):
        x[2] = random.randint(0,1000000)
        cadena = x[0] + " " + x[1] + " " + str(x[2]) + str(x[3])
    return (cadena, x[3])

def func(msgInput,keyInput):
    paquete = []
    mensaje = msgInput
    hmacCalculado = hmac.hmacFuncion(mensaje,keyInput)  # type: ignore
    paquete.append((mensaje,hmacCalculado))
    return hmacCalculado

file = open("./conf.txt", "r")
config = []
for line in file:
    line = line.strip()
    words = line.split("=")
    config.append(words[1])
num_pruebas = config[0]
file.close()



def run_query(query=''):    
    cursor = aperturaBaseDatos.conexion.cursor()
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data

cursor = aperturaBaseDatos.conexion.cursor()
cont = 0
archivo = "./log/" + str(datetime.now().strftime('%Y_%m'))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        for i in range(int(num_pruebas)):
            data = conn.recv(1024)
            print(f"Connected by {addr}")
            p = data.decode()
            t = "1234"
            x = func(p,t)
            file = open(archivo + ".txt", "a")
            if(x == str(l(p))):
                mensaje = "no ha habido una modificacion"
                print(mensaje)
                file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(datetime.now(
                    ).strftime('%H:%M')) + ": ACIERTO - No se ha modificado ningún mensaje\n")  
            else:
                mensaje = "ha habido una modificacion"
                print(mensaje)
                file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(
                        datetime.now().strftime('%H:%M')) + ": FALLO - Se ha modificado un mensaje\n")
            file.close()

            file = open(archivo + ".txt", "a")
            if(cont == 0):
                cursor.execute("INSERT INTO tablepai2(Nonce, NumeroCuenta) VALUES (%s,%s)",(gen_prueba_random(p)[1], 324343))
                aperturaBaseDatos.conexion.commit()
                cont += 1
            else:
                val = "SELECT * FROM tablepai2"
                val = run_query(val)
                n = False
                for m in val or []:
                    if(m[0] == gen_prueba_random(p)[1]):
                        n = True
                        print("FALLO, HA OCURRIDO UN REPLAY")
                        file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(
                        datetime.now().strftime('%H:%M')) + ": FALLO - Se ha realizado un replay\n")
                if(n==False):
                    cursor.execute("INSERT INTO tablepai2(Nonce, NumeroCuenta) VALUES (%s,%s)",(gen_prueba_random(p)[1], 324343))
                    aperturaBaseDatos.conexion.commit()
                    print("No ha habido replay y Insertado nuevo nonce en base de datos")
                    file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(datetime.now(
                    ).strftime('%H:%M')) + ": ACIERTO - No se ha realizado un replay\n")  
                file.close()


file = open(archivo + ".txt", "r")
cont = 0
for line in file:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == 'FALLO':
            cont = cont + 1
            
file.close()
file = open(archivo + ".txt", "a")
file.write("Han ocurrido un total de " + str(cont) + " fallos\n")
file.close()