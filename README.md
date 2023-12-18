# PyChatBot

---

###### Projet proposé par Pierre CAMELERI Raphaël Guignolle

## Dependencies

Ce programme utilise uniquement python 3
Ce programme est indépendant de l'OS (windows, mac, linux)
Modules natifs utilisés:
* `math` pour le calcul du logarithme décimal
* `os` pour lister les fichiers et effacer la console

Ce programme fourni un corpus de document dans `/speeches`. On peut les remplacer ou en ajouter d'autres, ils doivents juste avoir la syntaxe suivante : `/speeches/Nomination_*.txt` avec la partie à compléter un nom de président que l'on peut retrouver dans les cleés du dictionnaire `NOM_PRENOM` dans le module `/consts.py`.


> [!WARNING]
> La version de Python doit être au-dessus ou égale 3.11.0

## Getting started

* Cloner le repo via `git clone https://github.com/Emprario/pychatbot-cameleri-guignolle-a`
* Se déplacer dans le **dossier courant du projet** `cd pychatbot-cameleri-guignolle-a`
* Executer avec python `py main.py`

Le programme se décompose en deux parties : Chatbot et menu rapide, pour répondre aux menus, vous devez entrer le numéro du choix sélectionné.

> [!TIP]
> Vous pouvez executer plusieurs fois le programme après appuye de `Entrée` pour effacer la console
> Vous pouvez également retourner au menu principal en utilisant le choix 0 dans le sous menu des accès rapides

## Known bugs

Il n'existe pas de bug majeur connu.
Toutes les saisies sont sécurisées sauf celui de la saisie du nombre à virgule flotante dans le choix du seuil pour le score TF-IDF.
Si vous en trouvez, n'hésitez pas à les reporter via [issues](https://github.com/Emprario/pychatbot-cameleri-guignolle-a/issues)