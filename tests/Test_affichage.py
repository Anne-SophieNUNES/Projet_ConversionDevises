"""DESCRIPTION.

Tests automatiques pour l'affichage. 
"""
from final.lib_donnees import Donnees
from final.lib_affichage import affichage, affichage_frais


def test_affichage():
    essai = Donnees(
        devise_initiale="EUR",
        montant=1.0,
        devises=["EUR", "USD", "JPY", "GBP", "CHF", "CAD"],
        taux=[
            [1.0, 1.0879, 135.1710, 0.8344, 1.0162, 1.3682],
            [0.9192, 1.0, 124.2995, 0.7671, 0.9345, 1.2566],
            [0.0074, 0.0080, 1.0, 0.0062, 0.0075, 0.0101],
            [1.1983, 1.3036, 162.0800, 1.0, 1.2177, 1.6324],
            [0.9827, 1.0703, 133.0050, 0.8201, 1.0, 1.3435],
            [0.7315, 0.7957, 98.9059, 0.6104, 0.7434, 1.0],
        ],
    )
    return affichage(essai) == print(
        f"Le montant de départ est de : 2000 EUR\n"
        f"Le montant est maintenant de : 2010.75441 EUR\n"
        f"Le chemin sélectionné est : ['EUR', 'CAD', 'JPY', 'GBP', 'EUR']"
    )

def test_affichage_false():
    essai = Donnees(
        devise_initiale="EUR",
        montant=1.0,
        devises=["EUR", "USD", "JPY"],
        taux=[[1.0, 1.0879, 135.1710],
              [0.9192, 1.0, 124.2995],
              [0.0074, 0.0080, 1.0]]
    )
    return affichage(essai) != print(
        f"Le montant de départ est de : 3000 EUR\n"
        f"Le montant est maintenant de : 2010.75441 EUR\n"
        f"Le chemin sélectionné est : ['EUR', 'CAD', 'JPY', 'GBP', 'EUR']"
    )


def test_affichage_frais():
    essai = Donnees(
        devise_initiale="EUR",
        montant=1.0,
        devises=["EUR", "USD", "JPY", "GBP", "CHF", "CAD"],
        taux=[
            [1.0, 1.0879, 135.1710, 0.8344, 1.0162, 1.3682],
            [0.9192, 1.0, 124.2995, 0.7671, 0.9345, 1.2566],
            [0.0074, 0.0080, 1.0, 0.0062, 0.0075, 0.0101],
            [1.1983, 1.3036, 162.0800, 1.0, 1.2177, 1.6324],
            [0.9827, 1.0703, 133.0050, 0.8201, 1.0, 1.3435],
            [0.7315, 0.7957, 98.9059, 0.6104, 0.7434, 1.0],
        ],
    )
    return affichage_frais(essai) == print(
        f"Le montant de départ est de : 2000 EUR\n"
        f"Avec les conversions, le montant est passé à : 2000 EUR\n"
        f"Les frais s'élèvent à : 60.0 EUR\n"
        f"Le montant est maintenant de : 2000 EUR\n"
        f"Le chemin sélectionné est : ['EUR', 'EUR']"
    )
    
def test_affichage_frais_false():
    essai = Donnees(
        devise_initiale="EUR",
        montant=1.0,
        devises=["EUR", "USD", "JPY"],
        taux=[[1.0, 1.0879, 135.1710],
              [0.9192, 1.0, 124.2995],
              [0.0074, 0.0080, 1.0]]
    )
    return affichage_frais(essai) != print(
        f"Le montant de départ est de : 2000 EUR\n"
        f"Avec les conversions, le montant est passé à : 2000 EUR\n"
        f"Les frais s'élèvent à : 60.0 EUR\n"
        f"Le montant est maintenant de : 2000 EUR\n"
        f"Le chemin sélectionné est : ['EUR', 'EUR']"
    )
    