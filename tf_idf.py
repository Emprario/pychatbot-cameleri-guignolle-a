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