class State:
    def __init__(self):
        pass

    def display_menu(self):
        if self == 1:
            print("MENU PRINCIPAL/n1-Gérer les Joueurs/n2-Gérer les tournois/n3-Gérer Tours et Matchs/n4-Faire des Rapports")
            saisie = int(input())
            return saisie
        if self == 2:
            print("GERER UN JOUEUR/n1-Ajouter un joueur/n2-Supprimer un joueur/n3-Modifier un joueur/n4-Retour")
            saisie = int(input())
            return saisie
        if self == 3:
            print("GERER UN TOURNOI/n1-Ajouter un tournoi/n2-Supprimer un tournoi/n3-Modifier un tournoi/n4-Retour")
            saisie = int(input())
            return saisie
        if self == 4:
            print("GERER UN TOUR/MATCH/n1-Ajouter un tour/n2-Supprimer un tour/n3-Modifier un tour/n4-Retour")
            saisie = int(input())
            return saisie
        if self == 5:
            print("FAIRE DES RAPPORTS/n"
                    "1-liste de tous les joueurs par ordre alphabétique/n"
                    "2-liste de tous les tournois/n"
                    "3-nom et dates d’un tournoi donné/n"
                    "4-liste des joueurs du tournoi par ordre alphabétique/n"
                    "5-liste de tous les tours du tournoi et de tous les matchs du tour/n"
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
            pass
        elif saisie == 2:
            pass
        elif saisie == 3:
            pass
        elif saisie == 4 :
            pass
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
            pass
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
            pass
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
            pass
        else:
            self.gerer_rapports()












