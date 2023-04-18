class Club:
    id_national = ""
    num_joueur = ""
    nom = ""

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

class Joueur:
    num_joueur = ""
    num_club = ""
    nom_famille = ""
    prenom = ""
    date_naissance = ""

class Rapports:
    num_rapports = ""
    num_tournoi = ""
    liste = []

class Tour:
    nom_tour = ""
    liste_match = []
    date_debut = ""
    date_fin = ""

class Match:
    num_match = ""
    nom = ""
    liste_joueurs = []
    liste_match = []
    score = 0
