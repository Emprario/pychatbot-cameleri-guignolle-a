"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Gestion de menus
"""

from functions import *
from tf_idf import *
from consts import *
from os import listdir


def less_important_words(verbose: bool, seuil: int = -1) -> list[str]:
    """
    Renvoie les mots avec un score tf-idf inférieur ou égale à un seuil (zéro compris)
    :param verbose: permet l'affichage ou non du résultat
    :param seuil: indique le seuil minimum (optionnel)
    """
    while seuil < 0:
        seuil = float(input("Indiquez le score maximum souhaité (0 pour les mots \"non-importants\") : "))

    matrice = tf_idf_matrice(CORPUS_CLEAN)
    tfidf_seuil = []

    for word in matrice:
        score_sum = 0.0
        for text in matrice[word]:
            score_sum += matrice[word][text]
        score = score_sum / NB_TEXT  # Calcul d'un score tf-idf moyen d'un mot sur tous les fichiers
        if score <= seuil:
            tfidf_seuil.append(word)

    if verbose:
        print_list("Mots les moins importants (selon seuil) :", tfidf_seuil)  # Affichage
    return tfidf_seuil


def max_tfidf_words() -> None:
    """
    Affiche le(s) mot(s) avec le score tf-idf le plus élevé
    """
    matrice = tf_idf_matrice(CORPUS_CLEAN)
    score_max = 0.0
    list_words = []

    for word in matrice:
        for text in matrice[word]:
            score = matrice[word][text]
            if score > score_max:  # Si le nouveau score est plus élevé alors, on change le mot
                score_max = score
                list_words = [word]
            elif score == score_max:  # Si le nouveau score est égal alors, on rajoute le mot
                list_words.append(word)

    print_list("Mot(s) ayant le score TF-IDF le plus élevé :", list_words)  # Affichage


def max_repeated() -> None:
    """
    Affiche le(s) mot(s) le(s) plus répété(s) par le président fourni hormis mot non important
    """
    lst_president = list(NOM_PRENOM.keys())
    choice = choose_among("Choisir un président", lst_president)
    president = lst_president[choice]

    infile = ""  # Création d'un grand texte à partir des discours du président
    for file in extract_names(CORPUS_CLEAN)[president]:
        target = open(CORPUS_CLEAN + file, 'r', encoding="utf-8")
        infile += target.read() + " "
        target.close()
    tf = tf_occurences(infile)  # Calcul d'occurrence des mots dans tous les discours du président

    # Recherche du(des) mot(s) avec le plus occurrences
    occ_max = 0
    list_words = []
    not_important = less_important_words(False, 0)
    for word in tf:
        if tf[word] > occ_max and word not in not_important:
            occ_max = tf[word]
            list_words = [word]
        elif tf[word] == occ_max and word not in not_important:
            list_words.append(word)

    print_list("Mot(s) le(s) plus répété(s) par le président " + president + " :", list_words)  # Affichage


def lookfor_word(most: bool) -> None:
    """
    Affiche le nom du (des) président(s) qui ont parlé d'un certain mot
    Avec la possibilité d'afficher celui qui en a parlé le plus
    :param most: active l'affichage de celui qui en parle le plus
    """

    word = ""
    while word == "":
        word = input("Entrer un mot simple : ")
    word = format_text(word)

    tfmatrice = {}
    for file in listdir(CORPUS_CLEAN):
        with open(CORPUS_CLEAN + file, 'r', encoding='utf-8') as speech:
            tfmatrice[file] = tf_occurences(speech.read())

    association = extract_names(CORPUS_CLEAN)  # Récupération d'un dictionnaire président : list[fichier]

    list_president = []
    tf_max = 0
    president_max = ""

    for file in tfmatrice:
        if word in tfmatrice[file]:  # Signifie que le président en parle
            for president in association:
                if file in association[president]:  # Récupération du nom du président qui a prononcé le discours
                    list_president.append(president)
                    if tfmatrice[file][word] > tf_max:  # Définition de celui qui en parle le plus
                        tf_max = tfmatrice[file][word]
                        president_max = president

    print_list(f"Président(s) qui a/ont parlés de '{word}' :", set(list_president))  # Affichage
    if most:
        print(f"Le président qui en a le plus parlé est {president_max} avec {tf_max} occurences")


OPTIONS_MENU = (
    ("Sortir", exit),
    ("Afficher la liste des mots les moins importants", lambda: less_important_words(True)),
    ("Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé", max_tfidf_words),
    ("Afficher le(s) mot(s) le(s) plus répété(s) par un président", max_repeated),
    ("Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé d'un mot et le plus de fois", lambda: lookfor_word(True)),
    ("Recherche le(s) président(s) qui a/ont parlé d'un mot", lambda: lookfor_word(False)),
)


def do_menu(options: tuple[str, None], real_exit: bool) -> None:
    """
    Affiche un menu de sélection et gère son éxécution
    :param options: tuple de combinaison description et action
    :param real_exit: indique si la fonction doit réellement quitter le programme
    """
    while True:
        choice = choose_among("Que voulez-vous faire ?", [option[0] for option in options])
        if choice == 0 and not real_exit:
            clean()
            break
        options[choice][1]()

        input("Passer à la suite ...")
        clean()


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")