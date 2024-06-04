import os
import datetime
import random
import shutil
import re
import argparse

def lister_dossiers():
    chemin = "C:\\vvsTestor\\conf_sit"
    dossiers = []
    listdir = os.listdir(chemin)
    for dossier in listdir:
        if dossier.startswith('test-case_'):
            dossiers.append(dossier)

    dossiers.sort()

    for dossier in dossiers:
        print(dossier)

def main():
    parser = argparse.ArgumentParser()

    #creation  des paramètres attendu
    parser.add_argument("-l", "--lister", help="Afficher la liste des dossiers", action="store_true")
    parser.add_argument("-C", "--Create", help="Afficher la liste des dossiers", action="store_true")

    #analyse des paramètre trouvé
    args = parser.parse_args()

    if args.lister:
        lister_dossiers()

    if args.Create:
        print("print")

if __name__ == "__main__":
    main()


print("dko")