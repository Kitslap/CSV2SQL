# PROJET PYTHON KAROLAK 2017
# BURBAUD Pierre - GNERUCCI Maxime
# Fonctions : Generateur de hash de mot de passe aléatoire et Générateur de login.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import random

# Fonction : Generateur de hash md5 de password random.
# Utilise hashlib et random.

def GenPw():

# Bibliothèque de caractère

    librandom = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" 
    

# Choisit aléatoirement 10 caractères de la blibliothèque et genère un hash md5 du password.
# On aurait pu le faire en 2 étapes en vue de récupérer le mot de passe en clair. Ici il ne sera jamais généré et restera inconnu.
    
    pw = hashlib.md5("".join(random.sample(librandom,10)).encode('utf-8')).hexdigest()
    
    return pw

# Fonction : Générateur de login.


def GenLogin(nom , prenom, dnaiss) :

# Première lettre du prénom associé au nom de famille suivi de la date de naissance mélangé. ( Le choix de la date mélangé relève de la confidentialité de l'utilisateur. )
    nom_unspaced = nom.replace(' ','')
    login = prenom[0] + nom_unspaced + "_" + dnaiss[8] + dnaiss[0] + dnaiss[9] + dnaiss[7] + dnaiss[3] + dnaiss[6] + dnaiss[1] + dnaiss[4]
    return login
