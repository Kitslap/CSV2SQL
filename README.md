# Projet Python : CSV2SQL

[Projet ASSR Python 2017](https://git.karolak.fr/assr/projet-python-2017)

## Énoncé
Votre responsable vous demande de constituer une base de données de tout le personnel de l'entreprise, afin que cette base de données puisse servir de base pour l'authentification des utilisateurs sur les différents applicatifs.
La RH, à partir de son logiciel, vous fournit (à chaque mouvement/changement dans la société) un export au format CSV de tout le personnel, sur le modèle suivant : https://github.com/Kitslap/Python2017/blob/Main-patch-2.0/export.csv

Les utilisateurs devront :
( Ce qui a été coché a été fait. )
- [x] posséder un identifiant unique et stable
- [x] avoir un mot de passe aléatoire généré et stocké de manière sécurisée
- [ ] avoir une appartenance au groupe de leur département (comptabilité, etc.)
- [x] être mis à jour s'ils changent de groupe ou de nom
- [x] pouvoir être mis à jour sans devoir leur créer un nouveau compte ou réinitialiser l'existant
- [x] être supprimé lorsqu'ils ont quitté l'entreprise

## Consignes
travail seul ou à deux
rendu fichiers Python dans un dossier (nommé suivant « votre_nom ») dans un archive ZIP (pareillement nommée), exemple : 
	
	karolak.zip
	|__ karolak/
	   |__ main.py
 	   |__ […]
	
à déposer sur Eprel/Moodle

## Notation
| Critères												|	Points		|
|-------------------------------------------------------|---------------|
| [x] fonctionnel 											|		10		|
| [x] code propre 											| 		2		|
| [x] code optimisé											|		4		|
| [x] utilisation des modules (csv, sqlite3, configparser)	|		2		|
| [x] utilisation de fonctions								|		2		|
| [x] découpage du code en modules (plusieurs fichiers)		|		2		|
| [ ] utilisation de classes								|		2		|
| [ ] respect de la PEP8 (guide de style)					|		1		|
| [ ] respect de la PEP257 (docstrings)						|		1		|
| [ ] utilisation d'un ORM pour la partie SQL				|		2		|
| [ ] écriture de tests										|	2 (bonus)	|

BURBAUD Pierre GNERUCCI Maxime - LP ASSR - IUT SENART - 2017 - Projet Python CSV2SQL

SPECIAL THANKS : FORTUNAT Jacob 
