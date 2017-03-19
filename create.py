# PROJET PYTHON KAROLAK 2017
# BURBAUD Pierre - GNERUCCI Maxime
# Fonction : Création d'une base et d'une table, la remplit avec les données d'un CSV.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, sqlite3
from features import GenPw, GenLogin

# Fonction Create : Création d'une base de donnée vierge avec des champs basé sur la première ligne du csv et la remplit avec le CSV.
# Utilise csv sqlite3 et les 2 modules pour générer les logins et mots de passes.

def Create():	
        con = sqlite3.connect("./file_db.db")
        cur = con.cursor()

# Création de la table, avec les champs voulus avec une commande SQL.
        cur.execute("CREATE TABLE users (nom, nomj, prenom, dnaiss, fonction, depart, courriel, tel, mobile, login, pw, UNIQUE(login));")

# Parcours du CSV...
        with open('export.csv',encoding="utf-8") as fin:
                dr = csv.reader(fin)
# Saut de la première ligne.
                dr.__next__()
				
# Dictionaire associant les champs au champs du CSV. 
                dicts = ({'nom': line[0], 'nomj': line[1], 'prenom': line[2], 'dnaiss': line[3], 'fonction': line[4], 'depart': line[5], 'courriel': line[6], 'tel': line[7], 'mobile': line[8], 'login' : GenLogin(line[0],line[2],line[3]), 'pw' : GenPw()} for line in dr)
                to_db = ((i['nom'], i['nomj'], i['prenom'], i['dnaiss'], i['fonction'], i['depart'], i['courriel'], i['tel'], i['mobile'], i['login'], i['pw']) for i in dicts)
				
# Execution en boucle de la commande SQL permettant de remplir chaque utilisateurs.
                cur.executemany("INSERT INTO users (nom, nomj, prenom, dnaiss, fonction, depart, courriel, tel, mobile, login, pw) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
                con.commit()
