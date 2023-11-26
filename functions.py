from os import listdir


NOM_PRENOM = {
    "Hollande": "François",
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}


def extract_names(speeches: str) -> dict[str:list[str]]:
    """
    Extrait le nom des présidents des noms des fichiers du dossier fourni
    :param speeches: chemin du dossier où se trouvent les fichiers à traiter
    :return: Un dictionnaire entre président (clées) et fichier (liste, valeurs)
    """

    association = {}
    for speech in listdir(speeches):
        if speech[:11] == "Nomination_" and speech[-4:] == ".txt":
            name = speech[11:-4]
            if name[-1] in "0123456789":
                name = name[:-1]
            if name not in association:
                association[name] = []
            association[name].append(speech)

    return association


def print_president_fullname(corpus: str) -> None:
    """
    Affiche les prénoms et noms des présidents
    :param corpus: chemin du dossier où se trouve les fichiers à traiter
    """
    for name in extract_names(corpus):
        print(NOM_PRENOM[name] + ' ' + name)

