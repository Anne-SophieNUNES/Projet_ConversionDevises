"""Description.

Données du problème.
"""

from serde import serde


def _devise_valide(valeur: str) -> bool: 
    """Vérifie que l'on prend une devise qui existe (avec trois lettres).
    
    Exemple :
    >>> _devise_valide('JPY')
    True
    >>> _devise_valide('MMLJ')
    False
    """
    if len(valeur) == 3:
        return True
    return False


def _longueur_valide(devises: tuple[str], taux: list[list[float]]) -> bool:
    """Vérifie que la longueur du tuple des taux de devises est de la même longueur que la liste des devises.
    
    Exemple :
    >>> _longueur_valide(devises = ('EUR', 'USD'), taux = [[1.0, 1.0879],[0.9192, 1.0]])
    True
    >>> _longueur_valide(devises = ('EUR', 'USD', 'FRR'), taux = [[1.0, 1.0879],[0.9192, 1.0]])
    False
    """
    if len(taux) == len(devises):
        boolean = []
        for i in taux:
            if len(i) == len(devises):
                boolean.append(True)
        if len(boolean) == len(devises):
            return True
    return False


@serde
class Donnees:
    """Représente les données d'un problème de conversion de devises.
    
    devise_initiale: correspond à la devise initiale choisie par l'utilisateur. 
    montant: correspond au montant que l'utilisateur souhaite convertir.
    devises: une liste des devises existantes de la base de données.
    taux: une liste des taux de changes correspondants.
    
    On vérifie certaines conditions de validité :
     - le nombre de lettre de l'abréviation de la devise initiale doit être égal à trois,
     - la devise initiale doit appartenir à la liste des devises existantes.
     - le nombre de lettre de l'abréviation des devises doit être égal à trois,
     - la longueur de la liste des taux doit être compatible à la longueur de la liste des devises
     afin que la construction d'un tableau de taille n x n soit possible.
     
    Dans un premier temps, nous importons notre base de données qui contient la liste des taux de changes 
    et le tuple de devises :
    donnees : 
    {   
        "devises": ["EUR", "USD", "JPY"],
        "taux": [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    }
    
    Ensuite, on laisse le choix à l'utilisateur de choisir sa devise initiale et son montant. Nous pouvons
    alors utiliser notre dataclass Donnees dans son intégralié :
    Exemple:
    >>> essai = Donnees(
    ...    devise_initiale = 'EUR',
    ...    montant = 2000.0,
    ...    devises = ["EUR", "USD", "JPY"],
    ...    taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]]
    ... )
    >>> essai
    Donnees(devise_initiale = 'EUR', montant = 2000.0, devises = ["EUR", "USD", "JPY"],
    taux = [[1.0, 1.0879, 135.1710], [0.9192, 1.0, 124.2995], [0.0074, 0.0080, 1.0]])
    
    Une fois tous les attributs nécessaires pour notre dataclass, nous pouvons créer un nouveau fichier json
    qui présente nos données comme ceci : 
    >>> from serde.json import to_json
    >>> code = to_json(essai)
    >>> code
    '{"devise_initiale": "EUR", "montant": 2000.0, "devises": ["EUR", "USD", "JPY"], "taux": [[1.0, 1.0879, 135.171], 
    [0.9192, 1.0, 124.2995], [0.0074, 0.008, 1.0]]}'
    """
    devise_initiale: str
    montant: int
    devises: list[str]
    taux: list[list[float]]


    def __post_init__(self):
        if _devise_valide(self.devise_initiale) == False:
            raise ValueError("L'abréviation d'une devise comporte trois lettres.")
        if self.devise_initiale not in self.devises:
            raise ValueError("La devise initiale doit faire parti de la liste des devises")
        if any(not _devise_valide(devise) for devise in self.devises):
            raise ValueError("L'abréviation d'une devise comporte trois lettres.")
        if _longueur_valide(self.devises, self.taux) == False:
            raise ValueError("Le tuple des taux de devises et la liste des devises doivent être de même longueur.")
