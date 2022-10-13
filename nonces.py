import random
from datetime import datetime

def generate_nonce(length=64):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

file1 = open("nonces.txt", "a")
file1.close()

def gen_nonce():
    file1 = open("nonces.txt", "r")
    lista = []
    for linea in file1:
        lista.append(linea.strip())
    file1.close()
    if(len(lista)==0):
        cod_nonce = generate_nonce()
    else:
        v = random.random()
        if(v > 0.8):
            cod_nonce = lista[0]
        else:
            cod_nonce = generate_nonce()
    return cod_nonce

archivo1 = "./log/" + str(datetime.now().strftime('%Y_%m'))


def sel(k,cont):
    file1 = open("nonces.txt", "r")
    lista = []
    for linea in file1:
        lista.append(linea.strip())
    file1.close()
    if(cont <= 0):
        file1 = open("nonces.txt", "a")
        file1.write(str(k) + "\n")
        file1.close()
    else:
        file = open(archivo1 + ".txt", "a")
        n = False
        print(lista)
        for m in lista:
            if(m == k):
                file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(
                datetime.now().strftime('%H:%M')) + ": FALLOREPLAY - Se ha realizado un replay\n")
                n = True
                return "FALLO, HA OCURRIDO UN REPLAY"
        if(n==False):
            file1 = open("nonces.txt", "a")
            file1.write(str(k) + "\n")
            file1.close()
            file.write("Dia " + str(datetime.now().strftime('%d')) + " Hora " + str(datetime.now(
            ).strftime('%H:%M')) + ": ACIERTO - No se ha realizado un replay\n")
            return "No ha habido replay y Insertado nuevo nonce en base de datos"  
        file.close()