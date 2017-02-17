# PROJET PYTHON KAROLAK 2017
# BURBAUD Pierre - GNERUCCI Maxime
# Script pour inscrire un fichier csv dans une base de donnée
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import modules/wil.py
import modules/widb.py

# Ouverture du fichier RH
fichier = open("export.csv", "r")
next(fichier)

# Parcours du fichier ( en ignorant la premiere ligne )

for ligne in ficher
    ent = wil(ligne)
# Ecrire dans la db
    widb(ent)

