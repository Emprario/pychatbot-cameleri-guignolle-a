from functions import *
from tf_idf import *
from os import system, name


def clean() -> None:
    """
    Efface la console (selon OS)
    """
    if name == "nt":
        system("cls")
    else:
        system("clear")


def less_important_words() -> None:
    """
    Affiche les mots avec un score tf-idf inférieur à un certain seuil
    """
    seuil = 0
    while seuil <= 0:
        seuil = float(input("Indiquez le score maximum souhaité : "))

    matrice = tf_idf_matrice(CORPUS_CLEAN)
    tfidf_seuil = []

    for word in matrice:
        score_sum = 0.0
        for text in matrice[word]:
            score_sum += matrice[word][text]
        score = score_sum / NB_TEXT  # Calcul d'un score tf-idf moyen d'un mot sur tous les fichiers
        if score <= seuil:
            tfidf_seuil.append(word)

    print_list("Mots les moins importants (selon seuil) :", tfidf_seuil)  # Affichage


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


def f3(): pass
def f4(): pass
def f5(): pass
def f6(): pass


CORPUS_CLEAN = "./cleaned/"
CORPUS_IN = "./speeches/"
NB_TEXT = len(listdir(CORPUS_IN))
OPTIONS = (
    ("Sortir", exit),
    ("Afficher la liste des mots les moins importants", less_important_words),
    ("Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé", max_tfidf_words),
    ("Afficher le(s) mot(s) le(s) plus répété(s) par Chirac", f3),
    ("Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et le plus de fois", f4),
    ("Recherche le premier président qui a parlé de climat", f5),
    ("Recherche les mots évoqués par tout les présidents", f6)
)

if __name__ == "__main__":
    print("Prétraitement des données ...")
    format_incorpus(CORPUS_IN, CORPUS_CLEAN)

    while True:
        print("Que voulez-vous faire ?")

        # Affiche les options disponibles
        for i in range(len(OPTIONS)):
            print(f"\t{i}. " + OPTIONS[i][0])

        # Récupère la réponse et éxécute la bonne fonction
        reply = input("> ")
        for i in range(len(OPTIONS)):
            if reply == str(i):
                OPTIONS[i][1]()

        input("Passer à la suite ...")
        clean()