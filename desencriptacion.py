import base64
from Crypto.Cipher import AES

cipherName = raw_input('Nombre del archivo con texto cifrado (Ej. test.aes): ')
ciphertext = open(cipherName+".txt","r").read()
#print ciphertext

keyFile = raw_input('Archivo donde esta la llave plox (Ej. llave): ')
encodedkey = open(keyFile+".txt","r").read()
decodedKey = base64.b64decode(encodedkey)
#print 'Decoded Key: '+decodedKey

decodedcipher = base64.b64decode(ciphertext)

obj = AES.new(decodedKey, AES.MODE_CBC, 'This is an IV123')
originalFile = cipherName[0:len(cipherName)-4]
newFile = open("New"+originalFile+".txt","w")
#print obj.decrypt(decodedcipher)
newFile.write(obj.decrypt(decodedcipher))
newFile.close()