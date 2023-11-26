from math import log
from os import listdir


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
        if char == " " or char == "\n":
            if word != '':
                if word not in tf:
                    tf[word] = 1
                else:
                    tf[word] += 1
            word = ""
        else:
            word += char
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
        idf[word] = log((nb_file / flat[word]) + 1, 10)
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
                tfidf[word][file] = 0  # Si tf[word] n'éxiste pas alors tf[word] = 0
    return tfidf

if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")