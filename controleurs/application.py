import json

from modele.echecs import *

joueur_list = []

class UserManager:
    def charger_donnees_json(self):
        with open("joueur.json","r") as f:
            for json_obj in f:
                joueur_dict = json.loads(json_obj, cls= JoueurDecoder)
                joueur_list.append(joueur_dict)

    def enregister_donnees_json(self) :
        with open("joueur.json","w") as f:
            json.dump(joueur_list,f, indent=4, cls=JoueurEncoder)
    def select_joueur(self):
        print("Veuillez choisir un joueur.")
        with open("joueur.json") as data_f:
            data = json.load(data_f)
            print(data)
            print(f" Joueur : " +" Nom: "+ data["nom_famille"] +" Prenom: "+ data["prenom"] +" Date de naissance: "+ data["date_naissance"])
        pass
    def supprimer_joueur(self):
        pass
    def ajouter_joueur(self,nom_famille, prenom, date_naissance):
        joueur = Joueur(nom_famille, prenom, date_naissance)
        joueur_list.append(joueur)
    def extraire_informations_joueur(self):
        with open('joueur.json','r') as file:
            data = json.load(file)
            nom_famille = data['nom_famille']
            prenom = data['prenom']
            date_naissance = data['date_naissance']
            print(f"Nom Famille: {nom_famille} , Prenom: {prenom} , Date de naissance: {date_naissance}")

class TournamentManager:
    def supprimer_tournoi(self):
        pass
    def ajouter_tournoi(self):
        pass
    def extraire_informations_tournoi(self):
        pass
class MenuManager:
    pass