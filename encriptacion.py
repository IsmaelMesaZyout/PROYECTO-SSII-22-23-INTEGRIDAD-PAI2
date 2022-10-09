import base64
from Crypto.Cipher import AES

plainName = input('Nombre del archivo con texto plano (Ej. archivo): ')
text = open(plainName+".txt","r").read()
#print text

keyFile = input('Archivo donde esta la llave plox (Ej. llave): ')
encodedkey = open(keyFile+".txt","r").read()
decodedKey = base64.b64decode(encodedkey)
#print 'Decoded Key: '+decodedKey

obj = AES.new(decodedKey, AES.MODE_CBC, 'This is an IV123')
ciphertext = obj.encrypt(text)
#print 'Original Ciphertext: '+ciphertext
encodedCipher = base64.b64encode(ciphertext)
#print 'Base64 Ciphertext  : '+encodedCipher

cipherFile = open(plainName+".aes.txt","w")
cipherFile.write(encodedCipher)
cipherFile.close()