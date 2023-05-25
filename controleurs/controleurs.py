import json

from modele.echecs import Joueur, JoueurEncoder

def ajouter_joueur():
    joueur = Joueur("A01","N03","TERRINE","Joffrey","13/01/1998")
    with open("joueur.json","w") as f:
        json.dump(joueur, f, cls=JoueurEncoder)

def extraire_informations_joueur():
    with open('joueur.json','r') as file:
        data = json.load(file)
        num_joueur = data['num_joueur']
        num_club = data['num_club']
        nom_famille = data['nom_famille']
        prenom = data['prenom']
        date_naissance = data['date_naissance']
        print(f" Num Joueur: {num_joueur} , Num Club: {num_club} , Nom Famille: {nom_famille} , Prenom: {prenom}")

ajouter_joueur()
extraire_informations_joueur()