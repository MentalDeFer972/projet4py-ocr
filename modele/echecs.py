from json import JSONEncoder


class Club:
    id_national = ""
    num_joueur = ""
    nom = ""

    def __init__(self, id_national, num_joueur, nom):
        self.id_national = id_national
        self.num_joueur = num_joueur
        self.nom = nom


class Tournoi:
    num_tournoi = ""
    nom = ""
    lieu = ""
    description = ""
    date_debut = ""
    date_fin = ""
    nbre_tours = 0
    liste_joueurs = []
    liste_tours = []

    def __init__(self, num_tournoi, nom, lieu, description, date_debut, date_fin, nbre_tours, liste_joueurs,
                 liste_tours):
        self.num_tournoi = num_tournoi
        self.nom = nom
        self.lieu = lieu
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbre_tours = nbre_tours
        self.liste_joueurs = liste_joueurs
        self.liste_tours = liste_tours


class Joueur:
    num_joueur = ""
    num_club = ""
    nom_famille = ""
    prenom = ""
    date_naissance = ""

    def __init__(self, num_joueur, num_club, nom_famille, prenom, date_naissance):
        self.prenom = prenom
        self.nom_famille = nom_famille
        self.num_club = num_club
        self.date_naissance = date_naissance
        self.num_joueur = num_joueur

class JoueurEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__


class Rapports:
    num_rapports = ""
    num_tournoi = ""
    liste = []

    def __init__(self, num_rapports, num_tournoi, liste):
        self.liste = liste
        self.num_tournoi = num_tournoi
        self.num_rapports = num_rapports


class Tour:
    nom_tour = ""
    liste_match = []
    date_debut = ""
    date_fin = ""

    def __init__(self, nom_tour, liste_match, date_debut, date_fin):
        self.date_fin = date_fin
        self.date_debut = date_debut
        self.liste_match = liste_match
        self.nom_tour = nom_tour


class Match:
    num_match = ""
    nom = ""
    liste_joueurs = []
    liste_match = []
    score = 0
    def __init__(self, num_match, nom, liste_joueurs, score):
        self.score = score
        self.liste_joueurs = liste_joueurs
        self.nom = nom
        self.num_match = num_match
