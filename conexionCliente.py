import socket
import paqueteCliente
import paqueteServidor

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def comprobacion(user_input):
    try:
        if(int(user_input)):
            return True
    except ValueError:
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(f"Received {data!r}")
    x = paqueteCliente.func(paqueteServidor.msgInput,paqueteServidor.keyInput)
    if(x[0][1] == paqueteServidor.hmacServer):
        mensaje = "todo ok"
        print(mensaje)  
    else:
        mensaje = "no ok"
        print(mensaje)