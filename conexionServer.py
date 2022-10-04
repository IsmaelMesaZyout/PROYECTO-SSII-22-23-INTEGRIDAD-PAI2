import socket
 
#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.bind(("localhost", 60))
s.listen(1)
 
sc, addr = s.accept()
 
 
while True: 
    recibido = sc.recv(1024)
 
    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break
 
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print("Recibido")
 
    #Devolvemos el mensaje al cliente
    sc.send(recibido)
 