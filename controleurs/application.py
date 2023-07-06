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