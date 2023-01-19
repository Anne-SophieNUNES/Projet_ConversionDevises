"""Description.

Application ligne de commande pour la librairie affichage de notre problématique.
"""

from .lib_donnees import Donnees
from .lib_affichage import affichage, affichage_frais
from serde.json import from_json, to_json
import typer
from rich import print
import json


application = typer.Typer()


@application.command()
def fichier(nom_fichier: str):
    with open('donnees.json') as mon_fichier:
        data = json.load(mon_fichier)

    exemple_donnees = Donnees(
        devise_initiale = str(input("Quelle devise voulez-vous convertir ? ")),
        montant = float(input("Quel est votre montant de départ: ")),
        devises = data['devises'],
        taux = data['taux']
    )
    code = to_json(exemple_donnees)

    with open(nom_fichier, "w") as fichier_data:
        fichier_data.write(code)


@application.command()
def calcule(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()
        
    donnees = from_json(Donnees, code)
    solution = affichage(donnees)
    return solution
 

@application.command()   
def calculefrais(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()
        
    donnees = from_json(Donnees, code)
    solution = affichage_frais(donnees)
    return solution
    
    
        
if __name__ == "__main__":
    application()