import os
import pyaes

#ouvrir un fichier chiffré
file_name = "test.txt.hacked"
file = open(file_name, "rb")
file_data = file.read()

#ma clé pour décrypter
key = b"ilfaitbeauaparis"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#supprimer le fichier chiffré
os.remove(file_name)

# créer un nouveau fichier déchiffré
new = file_name.removesuffix('.hacked')
new_file = open(new, "wb")
new_file.write(decrypt_data)
new_file.close()
