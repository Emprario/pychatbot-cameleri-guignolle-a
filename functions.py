from os import listdir, mkdir
from os.path import exists


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


def format_file(file: str, output_dir: str) -> None:
    """
    Formate le fichier fourni
    :param file: chemin du fichier à traiter
    :param output_dir: chemin du dossier où stocker le fichier traité
    """
    if not exists(output_dir): mkdir(output_dir)

    new_file = output_dir + file.split('/')[-1]  # Chemin du nouveau fichier

    # Création du nouveau fichier
    with open(file, 'r', encoding='utf-8') as entry, open(new_file, 'w', encoding='utf-8') as target:
        pre_char = ""
        for char in entry.read():
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)      # Passage en minuscule
            elif char == "'" or char == "`":
                char = ' '                      # Conversion des apostrophes en espace
            elif char in ".,;!\"?_":
                char = ''                       # Suppression de la ponctuation
            elif char == '-' or char == ':':
                if pre_char != ' ' and pre_char != '\n':
                    char = ' '
                else:
                    char = ''
            elif char == ' ' and (pre_char == ' ' or pre_char == '\n'):
                char = ''                       # Suppression des doubles espaces
            target.write(char)
            pre_char = char


def format_incorpus(corpus_in: str, corpus_clean: str) -> None:
    """
    Formate tous les fichiers fournis
    :param corpus_in: chemin du dossier où se trouvent les fichiers
    :param corpus_clean: chemin du dossier où stocker les fichiers formattés
    """
    for file in listdir(corpus_in):
        format_file(corpus_in + file, corpus_clean)



def print_list(titre: str, lst: list | set | tuple):
    """
    Permet l'affichage d'une liste avec son titre
    :param titre: le titre de la liste
    :param lst: la liste à afficher
    """
    print(titre)
    for e in lst:
        print("\t- ", e)

if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py instead")

