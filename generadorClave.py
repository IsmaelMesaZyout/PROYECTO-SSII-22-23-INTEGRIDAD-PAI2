import base64
import hashlib
from Crypto.Random import random

nKey = input('Tamanio de la llave pofavo ')
rnd = random.getrandbits(nKey) #print rnd
m = hashlib.md5()
m.update(str(rnd))
print (m.digest()) #print m.digest_size

keyFile = open("keyFile.txt","w")
encoded = base64.b64encode(m.digest())
#print encoded
keyFile.write(encoded)
keyFile.close()