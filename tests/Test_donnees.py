"""Description.

Tests automatiques de la librairie lib_donnees.py"""

import pytest
from final.lib_donnees import(
    Donnees,
    _devise_valide,
    _longueur_valide
)


def test_devise_valide():
    assert _devise_valide("JPY")
    assert _devise_valide("FVG")
    assert not _devise_valide("MMLJ")


def test_longueur_valide():
    assert _longueur_valide(
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )


def test_longueur_valide_false():
    assert not _longueur_valide(
        devises = ('EUR', 'USD', 'JPY', 'GBP', 'CHF'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )


def test_donnees_initialisation():
    donnees = Donnees(
        devise_initiale = 'EUR',
        montant = 2000,
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
        )
    isinstance(donnees, Donnees)


def test_donnees_initialisation_devise_initiale_valide():
    with pytest.raises(ValueError):
        Donnees(
            devise_initiale = 'EU',
            montant = 2000,
            devises = ('EUR', 'USD', 'JPY'), 
            taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
        )


def test_donnees_initialisation_devises_valides():
    with pytest.raises(ValueError):
        Donnees(
            devise_initiale = 'EUR',
            montant = 2000,
            devises = ('ER', 'USDH', 'JPYGG'), 
            taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
        )


def test_donnees_initialisation_devises_contient_devise_initiale():
    with pytest.raises(ValueError):
        Donnees(
            devise_initiale = 'EUR',
            montant = 2000,
            devises = ('CDF', 'USD', 'JPY'), 
            taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
        ) 


def test_donnees_initialisation_longueur_valide():
    with pytest.raises(ValueError):
        Donnees(
            devise_initiale = 'EUR',
            montant = 2000,
            devises = ('CDF', 'USD', 'JPY'), 
            taux = [[0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
        )