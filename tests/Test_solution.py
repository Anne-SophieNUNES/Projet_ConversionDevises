"""Description.

Tests automatiques de  la librairie lib_solution.py
"""

from itertools import cycle
from final.lib_donnees import Donnees
from final.lib_solution import (
    cherche_cycles, 
    calcule_cycle_rentable, 
    choix_conversion, 
    choix_conversion_frais
)


def test_cherche_cycles():
    donnees = Donnees(
        devise_initiale = 'EUR',
        montant = 2000.0,
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )
    tous_cycles = cherche_cycles(donnees)
    assert tous_cycles == [
        ['EUR', 'USD', 'EUR'],
        ['EUR', 'USD', 'JPY', 'EUR'],
        ['EUR', 'JPY', 'EUR'],
        ['EUR', 'JPY', 'USD', 'EUR']
        ]


def test_cherche_cycles_false():
    donnees = Donnees(
        devise_initiale = 'EUR',
        montant = 2000.0,
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )
    tous_cycles = cherche_cycles(donnees)
    assert tous_cycles != [
        ['EUR', 'USD', 'EUR'],
        ['EUR', 'USD', 'JPY', 'EUR'],
        ['EUR', 'JPY', 'EUR'],
        ]


def test_calcule_cycle_rentable():
    donnees = Donnees(
        devise_initiale = 'EUR',
        montant = 2000.0,
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )
    cycle_rentable = calcule_cycle_rentable(donnees)
    assert cycle_rentable == (2001.3363055400002, ['EUR', 'USD', 'JPY', 'EUR'])
    

def test_calcule_cycle_rentable_false():
    donnees = Donnees(
        devise_initiale = 'EUR',
        montant = 2000.0,
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    )
    cycle_rentable = calcule_cycle_rentable(donnees)
    assert cycle_rentable != (2001.33, ['EUR', 'USD', 'EUR'])


def test_choix_conversion():
    donnees = Donnees(
        devise_initiale = 'EUR', 
        montant = 2000, 
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.1279, 131.0], [0.9192, 1.0, 122], [0.0074, 0.0080, 1.0]]
    )
    choix = choix_conversion(donnees)
    assert choix == (2073.53136, ['EUR', 'USD', 'EUR'])


def test_choix_conversion_si_aucun_chemin_rentable():
    donnees = Donnees(
        devise_initiale = 'EUR', 
        montant = 2000, 
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.002, 135.1710], [0.9192, 1.0, 119.2], [0.004, 0.0080, 1.0]]
    )
    choix = choix_conversion(donnees)
    assert choix == (2000, ['EUR', 'EUR'])


def test_choix_conversion_frais():
    donnees = Donnees(
        devise_initiale = 'EUR', 
        montant = 2000, 
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.1279, 131.0], [0.9192, 1.0, 122], [0.0074, 0.0080, 1.0]]
    )
    choix = choix_conversion_frais(donnees)
    assert choix == (2011.3254192, ['EUR', 'USD', 'EUR'])


def test_choix_conversion_frais_si_aucun_rentable():
    donnees = Donnees(
        devise_initiale = 'EUR', 
        montant = 2000, 
        devises = ('EUR', 'USD', 'JPY'), 
        taux = [[1.0, 1.002, 135.1710], [0.9192, 1.0, 119.2], [0.004, 0.0080, 1.0]]
    )
    choix = choix_conversion_frais(donnees)
    assert choix == (2000, ['EUR', 'EUR'])