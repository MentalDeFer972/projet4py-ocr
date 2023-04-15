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
    num_joueurs = ""
    num_tours = ""

class Joueur:
    num_joueur = ""
    num_club = ""
    nom_famille = ""
    prenom = ""
    date_naissance = ""

class Rapports:
    num_joueur = ""
    num_tournois = ""

class Tours:
    num_tours = ""
    nom = ""
    liste_score = ""
    num_joueur = ""
    liste_match = ""

class Match:
    num_match = ""
    liste_joueurs = ""
    liste_match = ""
    score = 0
