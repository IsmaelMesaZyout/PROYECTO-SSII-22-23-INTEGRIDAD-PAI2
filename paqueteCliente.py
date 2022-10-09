import hmac

def func(msgInput,keyInput):
    paquete = []
    mensaje = msgInput
    print(mensaje)
    hmacCalculado = hmac.hmacFuncion(mensaje,keyInput)
    paquete.append((mensaje,hmacCalculado))
    print(paquete)
    return paquete