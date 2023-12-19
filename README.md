# PyChatBot

---

###### Projet proposé par Pierre CAMELERI & Raphaël GUIGNOLLE

## Dépendances

Ce programme est indépendant de l'OS (windows, mac, linux)

Modules natifs utilisés:
* `math` pour le calcul du logarithme décimal
* `os` pour lister les fichiers et effacer la console

Ce programme fournit un corpus de document dans `/speeches`. On peut les remplacer ou en ajouter d'autres, ils doivent juste avoir la syntaxe suivante : `/speeches/Nomination_*.txt` <br> * nom de président que l'on peut trouver dans les cleés du dictionnaire `NOM_PRENOM` du module `/consts.py`.


> [!WARNING]
> La version de Python doit être au-dessus ou égale à 3.11.0

## Guide de démarrage

* Cloner le repo via `git clone https://github.com/Emprario/pychatbot-cameleri-guignolle-a`
* Se déplacer dans le **dossier courant du projet** `cd pychatbot-cameleri-guignolle-a`
* Executer avec python `py main.py`

Le programme se décompose en deux parties : Chatbot et menu rapide, pour répondre aux menus, vous devez entrer le numéro du choix sélectionné.

> [!TIP]
> Vous pouvez executer plusieurs fois le programme après appuie sur `Entrée` pour effacer la console
> <br>Vous pouvez également retourner au menu principal en utilisant le choix 0

## Bugs connus

Il n'existe pas de bug majeur connu.
Toutes les saisies sont sécurisées sauf celle de la saisie du nombre à virgule flottante dans le choix du seuil pour le score TF-IDF.
Si vous en trouvez, n'hésitez pas à les reporter via [issues](https://github.com/Emprario/pychatbot-cameleri-guignolle-a/issues)