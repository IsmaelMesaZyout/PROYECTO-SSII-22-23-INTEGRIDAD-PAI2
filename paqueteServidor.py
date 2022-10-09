import hmac
paqueteServer = []
msgInput = input("Enter the Message = ")
keyInput = input("Enter the Secret Key = ")
hmacCalculado = hmac.hmacFuncion(msgInput,keyInput)
paqueteServer.append(("23249 67856 2000",hmacCalculado))
print(paqueteServer)
clave = "1234"
hmacServer = hmac.hmacFuncion(str(paqueteServer[0][0]), clave)
print(hmacServer)
