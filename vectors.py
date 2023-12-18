"""
Projet : pyChatBot
Auteurs : Pierre Cameleri, Raphaël Guignolle
Description : Vectorisation des matrices dans des espaces Nd
"""

from tf_idf import *
from consts import *


def correspondence(format_prompt: list[str]) -> list[str]:
    """
    Renvoie les mots communs au prompt et au corpus
    :param format_prompt: liste de tokens (mots)
    :return: liste de tokens (mots)
    """
    save = []
    for token in format_prompt:
        if token in idf_score(CORPUS_CLEAN):
            save.append(token)
    return save


def inverse_matrix(matrix: dict[str:dict[str:float]]) -> dict[str:dict[str:float]]:
    """
    Inverse une matrice tf-idf
    :param matrix: matrice tf-idf
    :return: matrice tf-idf inversée
    """
    new_matrix = {}
    for word in matrix:
        for document in matrix[word]:
            if document not in new_matrix:
                new_matrix[document] = {}
            new_matrix[document][word] = matrix[word][document]
    return new_matrix


def prod_scale(A: dict[str:float], B: dict[str:float]) -> dict[str:float]:
    """
    Renvoie le produit scalaire entre les vecteurs A et B
    :param A: vecteur A (dictionnnaire mot : score idf)
    :param B: vecteur B (dictionnnaire mot : score idf)
    :return: produit scalaire
    """
    result = 0
    for key in A:  # like for key in B
        result += A[key]*B[key]
    return result


def norm_vector(F: dict[str:float]) -> float:
    """
    Renvoie la norme du vecteur F
    :param F: vecteur (dictionnnaire mot : score idf)
    :return: norme du vecteur
    """
    som = 0
    for key in F:
        som += F[key]**2
    return som**0.5


def calc_similarity(A: dict[str:float], B: dict[str:float]) -> float:
    """Renvoie la similarité cosinus des vecteurs A et B
    :param A: vecteur A (dictionnnaire mot : score idf)
    :param B: vecteur B (dictionnnaire mot : score idf)
    :return: score de similarité
    """
    return prod_scale(A, B)/(norm_vector(A) * norm_vector(B))


def get_similar_text(tfidf_prompt: dict[str:dict[str:float]]) -> str:
    """
    Renvoie le texte le plus similaire au prompt
    :param tfidf_prompt: matrice tf-idf du prompt
    :return: nom du fichier
    """
    best_score = 0
    similar = None
    tfidf_clean = tf_idf_matrice(CORPUS_CLEAN)
    tfidf_corpus_inverted = inverse_matrix(tfidf_clean)
    tfidf_prompt_inverted = inverse_matrix(tfidf_prompt)
    for file in tfidf_corpus_inverted:
        sim = calc_similarity(tfidf_corpus_inverted[file], tfidf_prompt_inverted[PROMPT_TEXT])
        if sim > best_score:
            similar = file
            best_score = sim
    return similar


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")
