""""Description.

Fonctionnalités de conversion du problème brute vers un cylce en utilisant un dictionnaire.
"""

from .lib_dico import Dictionnaire
from .lib_donnees import Donnees


def cherche_cycles(donnees: Donnees) -> list[list[str]]:
    """Fonction qui cherche tous les cycles possibles sans répéter deux fois les devises
    et qui commence par la devise initiale. 
    
    Exemple : 
    >>> cherche_cycles(Donnees(
    ...         devise_initiale = 'EUR',
    ...         montant = 2000.0,       
    ...         devises = ('EUR', 'USD', 'JPY'), 
    ...         taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]))
    [['EUR', 'USD', 'EUR'], ['EUR', 'USD', 'JPY', 'EUR'], ['EUR', 'JPY', 'EUR'], ['EUR', 'JPY', 'USD', 'EUR']]
    """
    dictionnaire = Dictionnaire(donnees.devises, donnees.taux).creation_dictionnaire()
    all_cycles = []
    for devise_voisine in dictionnaire[donnees.devise_initiale]:
        cycles = []
        depart = [(devise_voisine, [devise_voisine])]
        chemin = []
        while len(depart) != 0:
            sommet, chemin = depart.pop()
            liste_nouveaux_sommets_voisins = [voisin for voisin in dictionnaire[sommet] if not(voisin in chemin)]
            for devise_voisine in liste_nouveaux_sommets_voisins:
                if devise_voisine == donnees.devise_initiale:
                    cycles.append(chemin + [donnees.devise_initiale])
                depart.append((devise_voisine, chemin + [devise_voisine]))
        for chemin in cycles:
            all_cycles.append([donnees.devise_initiale] + chemin)
    return all_cycles


def calcule_cycle_rentable(donnees: Donnees) -> tuple[float, list[str]]:
    """
    La fonction permet de calculer la somme pour tous les cycles et sélectionne le cycle le plus rentable.
    
    Exemple :
    >>> calcule_cycle_rentable(Donnees(
    ...         devise_initiale = 'EUR',
    ...         montant = 2000.0,
    ...         devises = ('EUR', 'USD', 'JPY'),
    ...         taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]))
    (2001.3363055400002, ['EUR', 'USD', 'JPY', 'EUR'])
    """
    chemins = cherche_cycles(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))
    dictionnaire = Dictionnaire(donnees.devises, donnees.taux).creation_dictionnaire()
    liste = []
    for chemin in chemins:
        n = len(chemin)-1
        somme = donnees.montant * dictionnaire[chemin[0]][chemin[1]] 
        for i in list(range(1,n)):
            somme = somme * dictionnaire[chemin[i]][chemin[i+1]]
        liste.append(somme)
    somme = max(liste)
    chemin_selectionne = chemins[liste.index(somme)]
    return somme, chemin_selectionne


def choix_conversion(donnees: Donnees) -> tuple[float, list[str]]:
    """
    La fonction vérifie s'il est avantageux de faire une conversion ou non.
    La fonction renvoie le montant final et le cycle sélectionné ou 
    la non conversion ([devise_initiale, devise_initiale]). 
    
    Exemple 1: 
    >>> choix_conversion(Donnees(
    ...         devise_initiale = 'EUR',
    ...         montant = 2000.0,
    ...         devises = ('EUR', 'USD', 'JPY'), 
    ...         taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]))
    (2001.3363055400002, ['EUR', 'USD', 'JPY', 'EUR'])
    
    Exemple 2 : 
    >>> choix_conversion(Donnees(
    ...         devise_initiale = 'EUR', 
    ...         montant = 2000,
    ...         devises = ('EUR', 'USD', 'JPY'), 
    ...         taux = [[1.0, 1.002, 135.1710], [0.9192, 1.0, 119.2], [0.004, 0.0080, 1.0]]))
    (2000, ['EUR', 'EUR'])
    """
    somme_converti = calcule_cycle_rentable(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[0]
    if somme_converti <= donnees.montant:
        somme_final = donnees.montant
        chemin_selectionne = [donnees.devise_initiale, donnees.devise_initiale]
    else:
        somme_final = somme_converti
        chemin_selectionne = calcule_cycle_rentable(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[1]
    return somme_final, chemin_selectionne


def choix_conversion_frais(donnees: Donnees) -> tuple[float, list[str]]:
    """
    La fonction vérifie s'il est avantageux de faire une conversion ou non 
    avec des frais de transactions. La fonction renvoie le montant final, le cycle sélectionné
    ou la non conversion ([devise_initiale, devise_initiale]) et le montant si nous faisons la conversion. 
    
    Exemple 1 : 
    >>> choix_conversion_frais(Donnees(
    ...         devise_initiale = 'EUR', 
    ...         montant = 2000,
    ...         devises = ('EUR', 'USD', 'JPY'), 
    ...         taux = [[1.0, 1.1279, 131.0], [0.9192, 1.0, 122], [0.0074, 0.0080, 1.0]]))
    (2011.3254192, ['EUR', 'USD', 'EUR'], 2073.53136)
    
    Exemple 2 :
    >>> choix_conversion_frais(Donnees(
    ...         devise_initiale = 'EUR', 
    ...         montant = 2000,
    ...         devises = ('EUR', 'USD', 'JPY'), 
    ...         taux = [[1.0, 1.002, 135.1710], [0.9192, 1.0, 119.2], [0.004, 0.0080, 1.0]]))
    (2000, ['EUR', 'EUR'], 1987.9869311999998)
    """
    somme_converti = calcule_cycle_rentable(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[0]
    somme_converti_avec_frais = somme_converti - somme_converti * 0.03
    if somme_converti_avec_frais <= donnees.montant:
        somme_final = donnees.montant
        chemin_selectionne = [donnees.devise_initiale, donnees.devise_initiale]
    else:
        somme_final = somme_converti_avec_frais
        chemin_selectionne = calcule_cycle_rentable(Donnees(donnees.devise_initiale, donnees.montant, donnees.devises, donnees.taux))[1]
    return somme_final, chemin_selectionne, somme_converti