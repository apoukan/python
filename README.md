#🔐 Mini Outils de Chiffrement/Déchiffrement AES en Python

Ce dépôt contient deux scripts Python permettant de chiffrer et déchiffrer un fichier texte à l'aide de la bibliothèque pyaes en mode AES CTR. Il s'agit d'une démonstration simple de l'utilisation de la cryptographie symétrique pour la protection des données.

## 📁 Contenu
encrypt_file.py : chiffre un fichier texte donné.
decrypt_file.py : déchiffre un fichier précédemment chiffré avec le script précédent.

## 📦 Prérequis

Avant d'exécuter les scripts, installez la bibliothèque pyaes si elle n'est pas déjà installée :
```bash
pip install pyaes
```

### 🔐 Script de Chiffrement – encrypt_file.py
Ce script :
Lit le contenu d'un fichier texte (test.txt).
Supprime le fichier original.
Chiffre les données avec la clé AES "ilfaitbeauaparis" (16 octets).
Enregistre le contenu chiffré dans un nouveau fichier portant l’extension .hacked.

Exemple d’exécution
```bash
python encrypt_file.py
```
Après exécution, un fichier test.txt.hacked sera généré.

### 🔓 Script de Déchiffrement – decrypt_file.py
Ce script :
Lit un fichier chiffré (test.txt.hacked).
Déchiffre les données avec la même clé AES.
Supprime le fichier chiffré.
Recrée le fichier d’origine (test.txt).

Exemple d’exécution
```bash
python decrypt_file.py
```
Après exécution, le fichier original test.txt est restauré.

##⚠️ Attention
Ces scripts sont des démonstrations pédagogiques. Ne pas les utiliser en production sans les adapter et renforcer la sécurité (notamment la gestion des clés).
La clé de chiffrement est codée en dur dans les deux scripts. Il est recommandé de la rendre configurable (via un fichier de configuration ou une variable d’environnement) dans un cas réel.

👤 Auteur
Réalisé par Sivanesan dans le cadre d’une démonstration en cybersécurité.
