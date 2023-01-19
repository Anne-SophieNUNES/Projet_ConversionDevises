"""Description.

Librairie qui construit un dictionnaire à partir d'une liste de taux et d'un tuple de devises.
"""


class Dictionnaire:
    """Création de l'objet dictionnaire."""
    def __init__(self, devises: tuple[str], taux: list[list[float]]): 
        self.devises = devises
        self.taux = taux
        
    def __repr__(self) -> str:
        """
        >>> repr(Dictionnaire(["EUR", "USD", "JPY"], [[1.0, 1.0879, 135.1710], [0.912, 1.0, 124.29], [0.0074, 0.0080, 1.0]]))
        "Dictionnaire(devises=['EUR', 'USD', 'JPY'], taux=[[1.0, 1.0879, 135.171], [0.912, 1.0, 124.29], [0.0074, 0.008, 1.0]])"
        """
        return f"Dictionnaire(devises={repr(self.devises)}, taux={repr(self.taux)})"


    def creation_dictionnaire(self) -> dict[str, dict[str, float]]:
        """On transforme notre tuple de taux et notre liste de devises en dictionnaire.
        
        Exemple :
        >>> Dictionnaire(('EUR', 'USD'), [[1.0, 1.0879],[0.9192, 1.0]]).creation_dictionnaire()
        {'EUR': {'EUR': 1.0, 'USD': 1.0879}, 'USD': {'EUR': 0.9192, 'USD': 1.0}}
        """
        dico = {}
        for devise, valeur in zip(self.devises, self.taux):
            dico[devise] = dict(zip(self.devises, valeur))
        return dico
