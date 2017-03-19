# PROJET PYTHON KAROLAK 2017
# BURBAUD Pierre - GNERUCCI Maxime
# Fonction : Mise à jour de la base de donnée
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, sqlite3
from features import GenPw, GenLogin

# Fonction Update : permet d'inscrire les nouveaux utilisateurs, de mettre à jour les utilisateurs déjà présents et de supprimmer les utilisateurs partis.
# Utilise csv sqlite3 et les 2 modules pour générer les logins et mots de passes.

def Update():
    
    con = sqlite3.connect("./file_db.db")
    cur = con.cursor()

# Parcours du CSV dans le but de créer et de remplire une base "temporaire" neuve et à jour.
    with open('export.csv',encoding="utf-8") as fin:
        dr = csv.reader(fin)
        dr.__next__()
        dicts = ({'nom': line[0], 'nomj': line[1], 'prenom': line[2], 'dnaiss': line[3], 'fonction': line[4], 'depart': line[5], 'courriel': line[6], 'tel': line[7], 'mobile': line[8], 'login' : GenLogin(line[0],line[2],line[3]), 'pw' : GenPw()} for line in dr)
        to_dbt = ((i['nom'], i['nomj'], i['prenom'], i['dnaiss'], i['fonction'], i['depart'], i['courriel'], i['tel'], i['mobile'], i['login'], i['pw']) for i in dicts)
        cur.execute("CREATE TABLE users_tmp (nom, nomj, prenom, dnaiss, fonction, depart, courriel, tel, mobile, login, pw, UNIQUE(login));")
        con.commit()
        cur.executemany("INSERT INTO users_tmp (nom, nomj, prenom, dnaiss, fonction, depart, courriel, tel, mobile, login, pw) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_dbt)
        con.commit()

# Parcours du CSV afin d'jouter les utilisateurs non présents dans la base de donnée.       
    with open('export.csv',encoding="utf-8") as fin:
        dr = csv.reader(fin)
        dr.__next__()
        dicts = ({'nom': line[0], 'nomj': line[1], 'prenom': line[2], 'dnaiss': line[3], 'fonction': line[4], 'depart': line[5], 'courriel': line[6], 'tel': line[7], 'mobile': line[8], 'login' : GenLogin(line[0],line[2],line[3]), 'pw' : GenPw()} for line in dr)
        to_db = ((i['nom'], i['nomj'], i['prenom'], i['dnaiss'], i['fonction'], i['depart'], i['courriel'], i['tel'], i['mobile'], i['login'], i['pw']) for i in dicts)
        cur.executemany("INSERT OR IGNORE INTO users (nom, nomj, prenom, dnaiss, fonction, depart, courriel, tel, mobile, login, pw) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
        con.commit()


# Supprime les utilisateurs absents de la base temporaire.
    cur.execute('''DELETE FROM users WHERE 
    users.login NOT IN (SELECT users_tmp.login FROM users_tmp)
    ''')
    con.commit()
	
# Mise à jour à des champs qui ont été changés présent dans la base temporaire dans la base vivante.
    cur.execute('''UPDATE users
		SET fonction = (SELECT fonction FROM users_tmp WHERE users_tmp.login = users.login),
		mobile = (SELECT mobile FROM users_tmp WHERE users_tmp.login = users.login),
		tel = (SELECT tel FROM users_tmp WHERE users_tmp.login = users.login),
	        depart = (SELECT depart FROM users_tmp WHERE users_tmp.login = users.login),
		courriel = (SELECT courriel FROM users_tmp WHERE users_tmp.login = users.login),
		nom = (SELECT nom FROM users_tmp WHERE users_tmp.login = users.login)
		''')
    con.commit()
	
# Supprime la table temporaire.
    cur.execute('''DROP TABLE users_tmp
    ''')
    con.commit()     
        

    
        

  
    
