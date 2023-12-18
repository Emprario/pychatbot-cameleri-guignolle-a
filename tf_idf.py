"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : La méthode TF-IDF
"""

from math import log10
from os import listdir
from consts import *


def tf_occurences(speech: str) -> dict[str:int]:  # Matrice TF d'un fichier
    """
    Calcul le nombre d'occurrences de chaque mot dans le texte fourni
    :param speech: contenu du fichier
    :return: dictionnaire associant mot : occurrence du mot dans le texte
    """

    tf = {}
    word = ""
    # Réécriture de split() selon nos besoins
    for char in speech:
        if char == " ":
            if word not in tf:
                tf[word] = 1
            else:
                tf[word] += 1
            word = ""
        else:
            word += char

    # Pour le mot de la fin
    if word not in tf:
        tf[word] = 1
    else:
        tf[word] += 1
    return tf


def idf_score(corpus: str) -> dict[str:float]:
    """
    Calcul le score idf de tous les mots dans les textes d'un répertoire
    :param corpus: chemin du dossier où se trouvent les fichiers à traiter
    :return: dictionnaire associant mot : score idf du mot dans le corpus
    """

    flat: dict[str:int] = {}  # Dictionnaire de la présence des mots dans le corpus
    nb_file = 0

    # Calcul le nombre de documents contenant chaque mot
    for file in listdir(corpus):
        with open(corpus + file, 'r', encoding='utf-8') as target:
            for word in tf_occurences(target.read()):
                if word not in flat:
                    flat[word] = 1
                else:
                    flat[word] += 1
        nb_file += 1

    # Calcul du score idf pour chaque mot du corpus
    idf = {}
    for word in flat:
        idf[word] = log10(nb_file / flat[word])
    return idf


def tf_idf_matrice(corpus: str) -> dict[str:dict[str:float]]:
    """
    Calcul de la matrice tf-idf au sein d'un corpus à l'aide du
    :param corpus: chemin du dossier où se trouvent les fichiers à traiter
    :return: matrice tf-idf avec les mots en ligne et les fichiers en colonne
    """

    idf_global: dict[str:float] = idf_score(corpus)  # Calcul du score idf pour chaque mot du corpus
    tfidf = {}

    # Associe à chaque fichier son tf
    all_files = {}
    for file in listdir(corpus):
        with open(corpus + file, 'r', encoding='utf-8') as target:
            all_files[file] = tf_occurences(target.read())

    for word in idf_global:
        tfidf[word] = {}  # Création d'une nouvelle ligne dans la matrice
        for file in all_files:
            tf = all_files[file]  # Récupère le tf du fichier
            if word in tf:
                tfidf[word][file] = tf[word] * idf_global[word]
            else:
                tfidf[word][file] = 0.0  # Si tf[word] n'éxiste pas alors tf[word] = 0
    return tfidf


def get_prompt_tfidf(format_prompt: list[str]) -> dict[str:dict[str:float]]:
    """
    Calcul du score tf-idf du prompt fourni
    :param format_prompt: prompt tokenisé
    :return: matrice tf-idf
    """
    tfidf = {}
    IDF = idf_score(CORPUS_CLEAN)
    TF = tf_occurences(" ".join(format_prompt))
    for word in IDF:
        if word not in TF:
            tfidf[word] = {PROMPT_TEXT: 0.0}
        else:
            tfidf[word] = {PROMPT_TEXT: TF[word] * IDF[word]}
    return tfidf


def get_tfidf_max_from_text(tfidf: dict[str:dict[str:float]], text: str) -> str:
    """
    Renvoie le mot avec le plus grand score tf-idf dans le texte de la matrice fourni
    :param tfidf: matrice tf-idf
    :param text: nom du texte
    :return: mot avec le tf-idf le plus élevé
    """
    maxy = -1
    better = ""
    for word in tfidf:
        if tfidf[word][text] > maxy:
            maxy = tfidf[word][text]
            better = word
    return better


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")
