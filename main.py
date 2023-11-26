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


def max_repeated(president: str) -> None:
    """
    Affiche le(s) mot(s) le(s) plus répété(s) par le président fourni
    :param president: le président à étudier
    """
    infile = ""  # Création d'un grand texte à partir des discours du président
    for file in extract_names(CORPUS_CLEAN)[president]:
        target = open(CORPUS_CLEAN + file, 'r', encoding="utf-8")
        infile += target.read() + " "
        target.close()
    tf = tf_occurences(infile)  # Calcul d'occurrence des mots dans tous les discours du président

    # Recherche du(des) mot(s) le plus occurrences
    occ_max = 0
    list_words = []
    for word in tf:
        if tf[word] > occ_max:
            occ_max = tf[word]
            list_words = [word]
        elif tf[word] == occ_max:
            list_words.append(word)

    print_list("Mot(s) le(s) plus répété(s) par le président Chirac :", list_words)  # Affichage


def lookfor_word(word: str, most: bool) -> None:
    """
    Affiche le nom du (des) président(s) qui ont parlé d'un certain mot
    Avec la possibilité d'afficher celui qui en a parlé le plus
    :param word: le mot à rechercher
    :param most: active l'affichage de celui qui en parle le plus
    """
    tfidf = tf_idf_matrice(CORPUS_CLEAN)

    association = extract_names(CORPUS_CLEAN)  # Récupération d'un dictionnaire président : list[fichier]

    list_president = []
    tfidf_max = 0
    president_max = ""

    for file in tfidf[word]:
        if tfidf[word][file] > 0:  # Signifie que le président en parle 
            for president in association:
                if file in association[president]:  # Récupération du nom du président qui a prononcé le discours
                    list_president.append(president)
                    if tfidf[word][file] > tfidf_max:  # Définition de celui qui en parle le plus
                        tfidf_max = tfidf[word][file]
                        president_max = president

    print_list(f"Président(s) qui a/ont parlés de '{word}' :", set(list_president))  # Affichage
    if most:
        print("Le président qui en a le plus parlé est :", president_max)


def f6(): pass


CORPUS_CLEAN = "./cleaned/"
CORPUS_IN = "./speeches/"
NB_TEXT = len(listdir(CORPUS_IN))
OPTIONS = (
    ("Sortir", exit),
    ("Afficher la liste des mots les moins importants", less_important_words),
    ("Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé", max_tfidf_words),
    ("Afficher le(s) mot(s) le(s) plus répété(s) par Chirac", lambda: max_repeated("Chirac")),
    ("Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et le plus de fois", 
     lambda: lookfor_word("nation", True)),
    ("Recherche le premier président qui a parlé de climat", lambda: lookfor_word("climat", False)),
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