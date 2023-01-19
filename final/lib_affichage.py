""""Description.

Librairie qui met en forme notre résultat.
"""

from .lib_solution import choix_conversion, choix_conversion_frais
from .lib_donnees import Donnees


def affichage(donnees: Donnees):
    """
    Fonction qui permet d'afficher le résultat.
     
    Exemple : 
    >>> affichage(Donnees("EUR", 1.0, ["EUR", "USD", "JPY"], [[1.0, 1.0879, 135.1710], [0.912, 1.0, 124.29], [0.0074, 0.0080, 1.0]]))
    Le montant de départ est de : 1.0 EUR 
    Le montant est maintenant de : 1.00059 EUR
    Le chemin sélectionné est : ['EUR', 'USD', 'JPY', 'EUR']
    """
    somme = choix_conversion(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[0]
    chemin = choix_conversion(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[1]
    print(
        f"Le montant de départ est de : {donnees.montant} {donnees.devise_initiale} \n"
        f"Le montant est maintenant de : {round(somme,5)} {donnees.devise_initiale} \n"
        f"Le chemin sélectionné est : {chemin}")


def affichage_frais(donnees: Donnees):
    """
    Fonction qui affiche le résultat avec frais de transaction.
    
    Exemple : 
    >>> affichage_frais(Donnees("EUR", 1.0, ["EUR", "USD", "JPY"], [[1.0, 1.0879, 135.1710], [0.912, 1.0, 124.29], [0.0074, 0.0080, 1.0]]))
    Le montant de départ est de : 1.0 EUR 
    Avec les conversions, le montant est passé à : 1.00059 EUR
    Les frais s'élèvent à : 0.03 EUR
    Le montant est maintenant de : 1.0 EUR
    Le chemin sélectionné est : ['EUR', 'EUR'] 
    """
    somme = choix_conversion_frais(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[0]
    chemin = choix_conversion_frais(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[1]
    somme_converti = choix_conversion_frais(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[2]
    print(
        f"Le montant de départ est de : {donnees.montant} {donnees.devise_initiale} \n"
        f"Avec les conversions, le montant est passé à : {round(somme_converti,5)} {donnees.devise_initiale} \n"
        f"Les frais s'élèvent à : {round(somme*0.03, 4)} {donnees.devise_initiale} \n"
        f"Le montant est maintenant de : {round(somme, 5)} {donnees.devise_initiale} \n"
        f"Le chemin sélectionné est : {chemin}")
    