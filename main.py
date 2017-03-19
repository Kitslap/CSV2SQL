# PROJET PYTHON KAROLAK 2017
# BURBAUD Pierre - GNERUCCI Maxime
# Script pour inscrire un fichier csv dans une base de donnée.
# Programme principal
# /!\ Le CSV doit contenir des dates de naissance pour tous les utilisateurs. /!\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from update import Update
from create import Create

# Vérifie si la base existe déjà, si elle existe : utilise la fonction update autrement la fonction create.
if os.path.isfile("./file_db.db"):
	Update()
else:
	Create()
