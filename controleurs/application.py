import json

from modele.echecs import Joueur, JoueurEncoder

class UserManager:
    def supprimer_joueur(self):
        pass
    def ajouter_joueur(self,nom_famille, prenom, date_naissance):
        joueur = Joueur(nom_famille, prenom, date_naissance)
        with open("joueur.json","w") as f:
            json.dump(joueur, f, cls=JoueurEncoder)
    def extraire_informations_joueur(self):
        with open('joueur.json','r') as file:
            data = json.load(file)
            num_joueur = data['num_joueur']
            num_club = data['num_club']
            nom_famille = data['nom_famille']
            prenom = data['prenom']
            date_naissance = data['date_naissance']
            print(f" Num Joueur: {num_joueur} , Num Club: {num_club} , Nom Famille: {nom_famille} , Prenom: {prenom}")

class TournamentManager:
    def supprimer_tournoi(self):
        pass
    def ajouter_tournoi(self):
        pass
    def extraire_informations_tournoi(self):
        pass
class MenuManager:
    pass