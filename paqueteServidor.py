import paqueteCliente
import hmac

paquete1 = paqueteCliente.paquete

paqueteServer = []
paqueteServer.append((paquete1[0][0],paquete1[0][1]))

clave = "1234"
hmacServer = hmac.hmacFuncion(paquete1[0][0], clave)

if(hmacServer == paquete1[0][1]):
    print("todo OK")