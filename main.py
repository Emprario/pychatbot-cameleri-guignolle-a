"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Programme d'initialisation du chatbot
"""

from semantics import *
from vectors import *
from consts import *
from menu import *


def ask_chatbot() -> None:
    """
    Permet d'interpréter une question de l'utilisateur et de renvoyer la réponse la plus probante
    """
    prompt = ""
    while prompt == "":
        prompt = input("Entrer votre demande : ")

    # Traite le prompt
    format_prompt = tokenization(prompt)
    matched = correspondence(format_prompt)

    # Vérifie que les mots de la question en commun avec le corpus ne soit pas uniquement des mots non importants
    if matched == [] or set(matched).issubset(set(less_important_words(False, 0))):
        print("Le corpus fourni ne permet pas au chatbot de répondre à la question posée.")
        return

    # Récupère la matrice tf-idf du prompt
    tfidf_prompt = get_prompt_tfidf(matched)

    # Récupère le texte le plus similaire
    simi_text = get_similar_text(tfidf_prompt)

    # Récupère le mot avec le plus grand score tf-idf du prompt
    better_prompt_word = get_tfidf_max_from_text(tfidf_prompt, PROMPT_TEXT)

    # Récupère la première phrase ou le mot avec le plus grand score tf-idf apparait
    with open(CORPUS_IN + '/' + simi_text, 'r', encoding="utf-8") as simi:
        sentence = get_sentence_from_word(simi.read(), better_prompt_word)

    # Ajoute un préfix à la réponse
    answer = precise_answer(prompt, sentence)

    # Fin et affichage
    print("Réponse : ")
    print("\t" + answer)


OPTIONS_MAIN = (
    ("Sortir", exit),
    ("Ouvrir le menu dans le programme", lambda: do_menu(OPTIONS_MENU, False)),
    ("Demander quelque chose au chatbot", ask_chatbot)
)

if __name__ == "__main__":
    print("Prétraitement des données ...")
    format_incorpus(CORPUS_IN, CORPUS_CLEAN)
    while True:
        do_menu(OPTIONS_MAIN, True)
