"""Description.

Tests automatiques de la librairie lib_dico.py.
"""

from final.lib_dico import Dictionnaire


def test_dictionnaire_initialisation():
    dictionnaire = Dictionnaire(
        devises = ('EUR', 'USD', 'JPY', 'GBP', 'CHF', 'CAD'), 
        taux = [
            [1.0, 1.0879, 135.1710, 0.8344, 1.0162, 1.3682],
            [0.9192, 1.0, 124.2995, 0.7671, 0.9345, 1.2566],
            [0.0074, 0.0080, 1.0, 0.0062, 0.0075, 0.0101],
            [1.1983, 1.3036, 162.0800, 1.0, 1.2177, 1.6324],
            [0.9827, 1.0703, 133.0050, 0.8201, 1.0, 1.3435],
            [0.7315, 0.7957, 98.9059, 0.6104, 0.7434, 1.0],
            ]
            )
    assert isinstance(dictionnaire, Dictionnaire)


def test_repr():
    resultat = Dictionnaire(devises=('EUR', 'USD', 'JPY'),taux=[[1.0, 1.0879, 135.1710],[0.9192, 1.0, 124.2995],[0.0074, 0.0080, 1.0]])
    assert repr(resultat) ==  "Dictionnaire(devises=('EUR', 'USD', 'JPY'), taux=[[1.0, 1.0879, 135.171], [0.9192, 1.0, 124.2995], [0.0074, 0.008, 1.0]])"


def test_creation_dictionnaire():
    Attributs = Dictionnaire(
        ('EUR', 'USD', 'JPY', 'GBP', 'CHF', 'CAD'), 
        [
            [1.0, 1.0879, 135.1710, 0.8344, 1.0162, 1.3682],
            [0.9192, 1.0, 124.2995, 0.7671, 0.9345, 1.2566],
            [0.0074, 0.0080, 1.0, 0.0062, 0.0075, 0.0101],
            [1.1983, 1.3036, 162.0800, 1.0, 1.2177, 1.6324],
            [0.9827, 1.0703, 133.0050, 0.8201, 1.0, 1.3435],
            [0.7315, 0.7957, 98.9059, 0.6104, 0.7434, 1.0],
        ],
        )
    test_dictionnaire = Attributs.creation_dictionnaire() 
    assert test_dictionnaire == {
        'EUR': {'EUR': 1.0,'USD': 1.0879,'JPY': 135.171,'GBP': 0.8344,'CHF': 1.0162,'CAD': 1.3682},
        'USD': {'EUR': 0.9192,'USD': 1.0,'JPY': 124.2995,'GBP': 0.7671,'CHF': 0.9345,'CAD': 1.2566},
        'JPY': {'EUR': 0.0074,'USD': 0.008,'JPY': 1.0,'GBP': 0.0062,'CHF': 0.0075,'CAD': 0.0101},
        'GBP': {'EUR': 1.1983,'USD': 1.3036,'JPY': 162.08,'GBP': 1.0,'CHF': 1.2177,'CAD': 1.6324},
        'CHF': {'EUR': 0.9827,'USD': 1.0703,'JPY': 133.005,'GBP': 0.8201,'CHF': 1.0,'CAD': 1.3435},
        'CAD': {'EUR': 0.7315,'USD': 0.7957,'JPY': 98.9059,'GBP': 0.6104,'CHF': 0.7434,'CAD': 1.0}}