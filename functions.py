"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Les fonctions de base
"""

from os import listdir, mkdir, name, system
from os.path import exists
from consts import *


def extract_names(speeches: str) -> dict[str:list[str]]:
    """
    Extrait le nom des présidents des noms des fichiers du dossier fourni
    :param speeches: chemin du dossier où se trouvent les fichiers à traiter
    :return: Un dictionnaire entre président et liste des fichiers associés
    """

    association = dict()
    for speech in listdir(speeches):
        if speech[:11] == "Nomination_" and speech[-4:] == ".txt":
            name = speech[11:-4]
            if name[-1] in "0123456789":
                name = name[:-1]
            if name not in association:
                association[name] = []
            association[name].append(speech)

    return association


def print_president_fullname(corpus: str) -> None:
    """
    Affiche les prénoms et noms des présidents
    :param corpus: chemin du dossier où se trouve les fichiers à traiter
    """
    for name in extract_names(corpus):
        print(NOM_PRENOM[name] + ' ' + name)


def format_text(text: str) -> str:
    """
    Formate le fichier fourni
    :param text: contenu textuel à traiter
    :return: texte formatté
    """

    buffer = ""  # Stockage du texte post-traitement

    pre_reduced = True
    for char in text:
        reduced = False

        for transformation in TRANSFORMATIONS:
            if char == transformation:
                char = TRANSFORMATIONS[transformation]  # Remplacement des accents

        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)  # Passage en minuscule

        for parasite, equal in PARASITE.items():
            for sub in parasite:
                if (len(sub) + 1 <= len(buffer) and buffer[-len(sub):] == sub and char in REDUCTION_SYNTAX and
                        buffer[-len(sub) - 1] in REDUCTION_SYNTAX):
                    buffer = buffer[:-len(sub)] + equal  # Remplacement du mot parasite par son équivalent
                    char = " "
                    pre_reduced = False

        if char in REDUCTION_SYNTAX:  # Suppression de caratères spéciaux en tenant compte du caractère précédent
            if pre_reduced:     # Si le tour précédent déjà réduit alors on réduit
                char = ''
            else:               # Sinon on laisse un espace pour séparer
                char = ' '
            reduced = True

        buffer += char          # Ajout du caractère
        pre_reduced = reduced

    if buffer[-1] == ' ':
        return buffer[:-1]
    else:
        return buffer


def format_incorpus(corpus_in: str, corpus_clean: str) -> None:
    """
    Formate tous les fichiers fournis
    :param corpus_in: chemin du dossier où se trouvent les fichiers
    :param corpus_clean: chemin du dossier où stocker les fichiers formattés
    """
    if not exists(corpus_clean): mkdir(corpus_clean)
    for file in listdir(corpus_in):
        new_file = corpus_clean + file.split('/')[-1]  # Chemin du nouveau fichier
        with open(corpus_in + file, 'r', encoding='utf-8') as entry, open(new_file, 'w', encoding='utf-8') as target:
            target.write(format_text(entry.read()))


def print_list(titre: str, lst: list | set | tuple):
    """
    Permet l'affichage d'une liste avec son titre
    :param titre: le titre de la liste
    :param lst: la liste à afficher
    """
    print(titre)
    for e in lst:
        print("\t- ", e)


def splitter(separator: str, prompt: str) -> list[str]:
    """
    Sépare un texte fourni selon les différents séparateurs fourni
    :param separator: chaine de caractère séparateurs
    :param prompt: texte à séparer
    :return: liste du prompt séparé
    """
    lst = []
    buffer = ""
    for char in prompt:
        if char in separator:
            lst += [buffer]
            buffer = ""
        else:
            buffer += char
    if buffer != "" and buffer not in separator:
        lst += [buffer]
    return lst


def choose_among(header: str, lst: list[str]) -> int:
    """
    Renvoie le numéro de l'option choisie par l'utilisateur parmi la liste des options affichées
    :param header: tête d'affichage
    :param lst: liste des options
    :return: numéro de l'option choisie
    """
    print(header)

    # Affiche les options disponibles avec un numéro associé
    for i in range(len(lst)):
        print(f"\t{i}. " + lst[i])

    number = ""
    while type(number) != int:
        reply = input("> ")
        number = ""
        i = 0
        while i < len(reply):   # Transforme si possible la réponse de l'utilisateur en un nombre
            if reply[i] in "0123456789":
                number += reply[i]
            else:
                number = ""
                break
            i += 1

        if number != "" and 0 <= int(number) < len(lst):    # Transforme le nombre en un entier
            number = int(number)

        if type(number) != int:
            print(f"Veuillez rentrer un nombre entre 0 et {len(lst) - 1}")

    return number


def clean() -> None:
    """
    Efface la console (selon OS)
    """
    if name == "nt":
        system("cls")
    else:
        system("clear")


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")