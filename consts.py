"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Définition des constantes essentielles
"""

from os import listdir

# Noms et prénoms des présidents
NOM_PRENOM = {
    "Hollande": "François",
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}

# Dictionnaires pour les transformations
TRANSFORMATIONS = {
    'À': 'a',
    'à': 'a',
    'ç': 'c',
    'é': 'e',
    'è': 'e',
    'ê': 'e',
    'ë': 'e',
    'ù': 'u',
    'û': 'u',
    'Î': 'i',
    'î': 'i',
    'ï': 'i',
}

# Mot parasite
PARASITE = {
    ("le", "la", "l", "les"): "le",
    ("un", "une"): "un",
    ("d", "du", "de", "des"): "de",
    ("ce", "cette", "cet", "ces", "cettes"): "ce",
    ("mon", "ton", "son", "ma", "ta", "sa", "notre", "votre", "leur", "nos", "vos", "leurs"): "mon",
    ("que", "quel", "quels", "quelle", "quelles"): "que",
    ("j", "je"): "je",
    ("n", "ne"): "ne"
}

# Synatx à réduire
REDUCTION_SYNTAX = ".,;!'`\"?_-:\n "

# Répertoire des CORPUS
CORPUS_CLEAN = "./cleaned/"
CORPUS_IN = "./speeches/"

NB_TEXT = len(listdir(CORPUS_IN))
PROMPT_TEXT = "prompt"
STARTERS = {
    "Est-ce que": "Oui, en effet,",
    "Comment": "Après analyse,",
    "Pourquoi": "Parce que,",
    "Peux-tu": "Oui bien sûr,"
}
END_OF_SENTENCE = "?.!"

if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")