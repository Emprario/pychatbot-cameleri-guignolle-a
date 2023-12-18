"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Gère la sémantique
"""

from functions import *
from consts import *


def tokenization(prompt: str) -> list[str]:
    """
    Renvoie la liste des mots formatés du prompt
    :param prompt: question saisie par l'utilisateur
    :return: liste des mots
    """
    return format_text(prompt).split(' ')


def get_sentence_from_word(paragraphe: str, word: str) -> str:
    """
    Renvoie la première phrase avec le mot fourni apparant
    :param paragraphe: texte non traité
    :param word: mot à chercher
    :return: première phrase
    """
    sentences = splitter(END_OF_SENTENCE, paragraphe)
    for i in range(len(sentences)):
        treated_statement = format_text(sentences[i]).split(' ')
        if word in treated_statement:  # Evite de confondre
            if sentences[i][0] == '\n':
                first_idx = 1
            else:
                first_idx = 0
            if "A" <= sentences[i][first_idx] <= "Z":
                return chr(ord(sentences[i][first_idx]) + 32) + sentences[i][first_idx + 1:]
            else:
                return sentences[i][first_idx:]


def precise_answer(prompt: str, answer: str) -> str:
    """
    Ajoute un préfix de liaison à la réponse fournie
    :param prompt: question d'entrée
    :param answer: réponse fournie
    :return: réponse complétée
    """
    for starter in STARTERS:
        if prompt[:len(starter)] == starter:
            start = STARTERS[starter]
            break
    else:
        start = "En effet,"
    while answer[0] == ' ':
        answer = answer[1:]

    answer = start + ' ' + answer + '.'

    while answer[-2] == ' ':
        answer = answer[:-2] + '.'

    return answer


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")
