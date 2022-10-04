import hmac

hmacMensaje = hmac.msgInput
hmacClave = hmac.keyInput

hmacCalculado = hmac.hmacFuncion(hmacMensaje,hmacClave)
paquete = []
paquete.append((hmacMensaje,hmacCalculado))
print(paquete)