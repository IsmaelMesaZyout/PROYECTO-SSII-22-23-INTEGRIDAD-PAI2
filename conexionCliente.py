import socket
import random
import time
import aperturaBaseDatos

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

file = open("./conf.txt", "r")
config = []
for line in file:
    line = line.strip()
    words = line.split("=")
    config.append(words[1])
num_pruebas = config[0]
file.close()

cursor = aperturaBaseDatos.conexion.cursor()

def run_query(query=''):
    cursor = aperturaBaseDatos.conexion.cursor()   
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data

def sel():
    val1 = "SELECT * FROM tablepai2"
    val1 = run_query(val1) 
    return val1

def gen_nonce():
    val = "SELECT * FROM tablepai2"
    val = run_query(val)
    print(val)
    if(len(val)==0):
        cod_nonce = generate_nonce()
    else:
        v = random.random()
        if(v > 0.1):
            print(val[0][0])
            cod_nonce = val[0][0]
        else:
            cod_nonce = generate_nonce()
    return cod_nonce

def generate_nonce(length=64):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

def comprobacion(user_input):
    try:
        if(int(user_input)):
            return True
    except ValueError:
        return False

def gen_transacciones():
    cuenta_Or   = random.randint(0,99999)
    cuenta_Dest = 65478
    cantidad    = random.randint(0,1000000)
    cadena = str(cuenta_Or) + " " + str(cuenta_Dest) + " " + str(cantidad) + " " + str(gen_nonce())
    return cadena


while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  
        msgInput = gen_transacciones()
        print(msgInput)
        #keyInput = input("Enter the Secret Key = ")
        s.send(msgInput.encode())
        time.sleep(10)