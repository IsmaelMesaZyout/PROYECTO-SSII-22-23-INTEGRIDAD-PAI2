import socket
 
s = socket.socket()

s.connect(("localhost", 60))
 
while True:
    mensaje = input("Mensaje a enviar >> ")
 
    s.send(mensaje)
 
    if mensaje == "close":
        break
print("Adios.")
