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


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")
