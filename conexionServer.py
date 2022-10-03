from socket import socket

# Crear el socket.
with socket() as s:
    # Asociarlo a una dirección de IP y un puerto.
    s.bind(("localhost", 6190))
    # Indicar que este socket actuará como servidor.
    s.listen()
    # Esperar a la conexión del cliente.
    print("Esperando al cliente...")
    conn, address = s.accept()
    print(f"address[0]:address[1] se ha conectado.")
    # Esperar a que el cliente envíe datos.
    while True:
        data = conn.recv(1024)
        # Chequear que no esté vacío.
        if data:
            # Imprimirlo en pantalla y cerrar el socket.
            print("El cliente ha enviado:", data)
            break

# El socket se cierra automáticamente al salir del bloque "with".
print("Conexión cerrada.")