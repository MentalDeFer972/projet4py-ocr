from controleurs.application import *


class State:
    def __init__(self):
        pass

    def display_menu(self, nombre):
        if nombre == 1:
            print(
                "MENU PRINCIPAL\n "
                "1-Gérer les Joueurs \n "
                "2-Gérer les tournois \n "
                "3-Gérer Tours et Matchs \n "
                "4-Faire des Rapports")
            saisie = int(input())
            return saisie
        if nombre == 2:
            print("GERER UN JOUEUR \n "
                  "1-Ajouter un joueur \n "
                  "2-Supprimer un joueur \n "
                  "3-Modifier un joueur \n "
                  "4-Retour")
            saisie = int(input())
            return saisie
        if nombre == 3:
            print(
                "GERER UN TOURNOI \n "
                "1-Ajouter un tournoi \n "
                "2-Supprimer un tournoi \n "
                "3-Modifier un tournoi \n "
                "4-Retour")
            saisie = int(input())
            return saisie
        if nombre == 4:
            print("GERER UN TOUR/MATCH \n "
                  "1-Ajouter un tour \n "
                  "2-Supprimer un tour \n "
                  "3-Modifier un tour \n "
                  "4-Retour")
            saisie = int(input())
            return saisie
        if nombre == 5:
            print("FAIRE DES RAPPORTS \n "
                  "1-liste de tous les joueurs par ordre alphabétique \n "
                  "2-liste de tous les tournois \n "
                  "3-nom et dates d’un tournoi donné \n "
                  "4-liste des joueurs du tournoi par ordre alphabétique \n "
                  "5-liste de tous les tours du tournoi et de tous les matchs du tour \n "
                  "6-Retour")
            saisie = int(input())
            return saisie

    def gestion_menu(self):
        saisie = self.display_menu(1)
        if saisie == 1:
            self.gerer_joueur()
        elif saisie == 2:
            self.gerer_tournoi()
        elif saisie == 3:
            self.gerer_tour_match()
        elif saisie == 4:
            self.gerer_rapports()
        else:
            self.gestion_menu()

    def gerer_joueur(self):
        saisie = self.display_menu(2)
        if saisie == 1:
            print("AJOUT D'UN JOUEUR \n ")
            print("Veuillez saisir le nom de famille du joueur : \n")
            nom_famille = input()
            print("Veuillez saisir le prénom du joueur : \n ")
            prenom = input()
            print("Veuillez saisir la date de naissance du joueur : \n")
            date_naissance = input()
            UserManager.ajouter_joueur(nom_famille, prenom, date_naissance)
            print("Joueur ajouté!")
            self.gerer_joueur()
        elif saisie == 2:
            UserManager.supprimer_joueur()
        elif saisie == 3:
            pass
        elif saisie == 4:
            self.gestion_menu()
        else:
            self.gerer_joueur()

    def gerer_tournoi(self):
        saisie = self.display_menu(3)
        if saisie == 1:
            pass
        elif saisie == 2:
            pass
        elif saisie == 3:
            pass
        elif saisie == 4:
            self.gestion_menu()
        else:
            self.gerer_tournoi()

    def gerer_tour_match(self):
        saisie = self.display_menu(4)
        if saisie == 1:
            pass
        elif saisie == 2:
            pass
        elif saisie == 3:
            pass
        elif saisie == 4:
            self.gestion_menu()
        else:
            self.gerer_tour_match()

    def gerer_rapports(self):
        saisie = self.display_menu(5)
        if saisie == 1:
            pass
        elif saisie == 2:
            pass
        elif saisie == 3:
            pass
        elif saisie == 4:
            pass
        elif saisie == 5:
            pass
        elif saisie == 6:
            self.gestion_menu()
        else:
            self.gerer_rapports()
