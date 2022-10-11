import socket
import random
import secrets
import time 
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

def comprobacion(user_input):
    try:
        if(int(user_input)):
            return True
    except ValueError:
        return False

def gen_nonce():
    cod_nonce = secrets.token_urlsafe()
    return cod_nonce

def gen_transacciones():
    cuenta_Or   = random.randint(0,99999)
    cuenta_Dest = 65478
    cantidad    = random.randint(0,1000000)
    cadena = str(cuenta_Or) + " " + str(cuenta_Dest) + " " + str(cantidad) + " " + str(gen_nonce())
    return cadena

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(num_pruebas)
    for i in range(int(num_pruebas)):
        msgInput = gen_transacciones()
        print(msgInput)
        #keyInput = input("Enter the Secret Key = ")
        s.send(msgInput.encode())
        #time.sleep(10)