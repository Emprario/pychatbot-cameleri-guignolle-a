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

def f1(): pass
def f2(): pass
def f3(): pass
def f4(): pass
def f5(): pass
def f6(): pass


CORPUS_CLEAN = "./cleaned/"
CORPUS_IN = "./speeches/"
OPTIONS = (
    ("Sortir", exit),
    ("Afficher la liste des mots les moins importants", f1),
    ("Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé", f2),
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