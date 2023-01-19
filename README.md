# <span style="color: #663333">Enoncé du problème de conversion de devises</span>

Un arbitrage consiste à utiliser les différences entre les taux de changes pour gagner de l'argent en une monnaie par une série de conversion.
Par exemple :

- 1 euro contre 49 roupies
- 1 roupie contre 2 yen
- 1 yen contre 0.0107 euros

Le chemin total permet de converitir 1 euro en 1.0486 euros. On suppose données $n$ devises et une table $n \times n$ pour les taux de change.
Détermine si des séquences d'arbitrage existent. Lequelles rapportent le plus et lesquelles ont le moins d'étapes.

# <span style="color: #663333">Illustration du problème</span>
Pour permettre de mieux comprendre, voici un exemple simplifié du problème avec résolution.
Supposons qu'un établissement de change, dont la principale activité est l'échange immédiat d'une devise contre une autre, propose la conversion de seulement trois devises : l'euro (EUR), le dollar américain (USD) et la livre sterlling (GBP). Voici le tableau récapitulatif des taux de change :

| devise initiale  | EUR             | USD             | GBP             |
| :--------------- |:---------------:|:---------------:|:---------------:|
| EUR              | 1.0             | 1.0879          | 0.8344          |
| USD              | 0.9192          | 1.0             | 0.7671          |
| GBP              | 1.1983          | 1.3036          |  1.0            |

Admettons maintenant qu'un individu se présente dans cet établissement de change afin de convertir 200 euros. Pour rappel, l'objectif est le gain monétaire après avoir effectuer des séries de conversion dont l'ensemble sera nommé cycle. Il ne faut pas qu'une même devise intervienne deux fois dans les séries de conversion (seule la devise du montant initiale doit être la même que celle du montant final).
Voici maintenant un tableau présentant les cycles possibles dans ce cas (200 euros), le montant des gains, et le montant final à l'issu des séries de conversion :

| cycles possibles            | gain            | montant final   |
| :--------------------------:|:---------------:|:---------------:|
| EUR --> USD --> EUR         | - 0.9999*       | 199.9995**      |
| EUR --> GBP --> EUR         | - 0.9999        | 199.9723        |
| EUR --> USD --> GBP --> EUR | + 1             | 200.0030        |
| EUR --> GBP --> USD --> EUR | - 0.9998        | 199.967         |

*<u>calcul du gain<u\>: $1.0879 \times 0.9192$
**<u>calcul du montant final<u\>: $200 \times 1.0879 \times 0.9192$

Plaçons nous maintenant dans le cas où l'établissement de change mettrait en place des frais de transaction sur les conversions de devises.
On fixera les frais de transaction à 3 % du montant final (après conversions).

| cycles possibles            | gain           | montant final   | frais de transaction    | choix          |
| :--------------------------:|:---------------:|:--------------:|:-----------------------:|:--------------:|
| EUR --> USD --> EUR         | - 0.9999        | 199.9995       | 6*                      | EUR --> EUR**  |
| EUR --> GBP --> EUR         | - 0.9999        | 199.9723       | 6                       | EUR --> EUR    |
| EUR --> USD --> GBP --> EUR | + 1             | 200.0030       | 6                       | EUR --> EUR    |
| EUR --> GBP --> USD --> EUR | - 0.9998        | 199.9670       | 6                       | EUR --> EUR    |

*<u>calcul des frais de transaction<u\>: $199.9995 \times 0.03$
*<u>explication du choix<u\>: si le montant final après déduction des frais de transaction est inférieur au montant initial, il n'est pas rentable d'effectuer la conversion.

# <span style="color: #663333">Méthodologie des librairies</span>
Pour résoudre ce problème de conversion de devises, nous avons créer plusieurs librairies avec leurs tests correspondants.

## <span style="color: #CC9999">Librairie **lib_donnees.py**</span>
Permet d'initiliser les données nécessaires pour résoudre notre problème : la devise à convertir choisie par l'utilisateur, le montant à convertir choisi également par l'utilisateur, ainsi que la liste de devises existantes et les taux de change associés. 

## <span style="color: #CC9999">Librarie **lib_dictionnaire.py**</span>
Permet de transformer nos données en un objet dictionnaire (deux dictionnaires imbriqués faisant référence à une table $n \times n$) que l'on explorera par la suite.

## <span style="color: #CC9999">Librairie **lib_solution.py**</span>
Permet de résoudre notre problème. On cherche dans un premier temps les cycles de conversion possibles. On isole ensuite le cycle le plus rentable d'un point de vue du gain d'argent. Puis, on renvoie le chemin le plus retable avec le montant initial et le montant après conversion. On peut aussi effectuer cette dernière étape dans le cas où des frais de transaction rentreraient en compte.

## <span style="color: #CC9999">Librairie **lib_affichage.py**</span>
Permet de paramétrer l'affichage du résultat obtenue par la résolution du problème.

# <span style="color: #663333">Utilisation de l'application</span>
Les listes de devises et de taux de change sont directement importées d'un fichier `json` nommé **donnees.json**. Il est important pour le bon fonctionnement de l'application que ce fichier `json` contienne la liste de devises existantes nommée ***devises*** ainsi que la liste de taux change nommée ***taux***.
1. <span style="color: #FF99CC">Ouvrir un terminal puis utiliser le package `pip` pour intaller `poetry`, `pyserde`, `typer`, `rich` si cela n'est pas déjà fait :</span>
```bash
pip install poetry
pip install pyserde
pip install typer
pip install rich
```

2. <span style="color: #FF99CC">Exécuter la ligne de commande suivante pour vérifier que l'environnement est activé.</span>
```bash
poetry shell
```
Voici le message qui devrait apparaître à la suite de cela:
```python
virtual environment already activited 
```

3. <span style="color: #FF99CC">Exécuter ensuite la ligne de commande suivante afin de visualiser les commandes possibles de notre application. En l'occurence, ici devront apparaître `fichier`, `calcule` et `calculefrais`.</span>
```bash
poetry run python -m final --help
```
Si tout fonctionne correctement, le message suivant devrait apparaître :
```bash
Usage: python -m final [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  calcule
  calculefrais
  fichier
```

4. <span style="color: #FF99CC">Enfin, exécuter les lignes de commande ci-dessous pour faire fonctionner l'application :</span>
```bash
poetry run python -m final fichier test.json
```
Les messages suivants devraient alors apparaître :
```bash
Quelle devise voulez-vous convertir ? 
Quel est votre montant de départ ?
```
Il suffit alors d'écrire le nom de la devise voulant être convertie (elle doit exister dans la liste de devises du fichier **donnees.json** et être écrite sans guillemets) et le montant à convertir.

```bash
poetry run python -m final calcule test.json
```
Qui doit renvoyer un message de ce type si l'on choisit la devise CAD (dollar canadien) et le montant 1500 :
```bash
Le montant de départ est de : 1500.0 CAD 
Le montant est maintenant de : 1508.06581 CAD
Le chemin sélectionné est : ['CAD', 'JPY', 'GBP', 'EUR', 'CAD']
```

```bash
poetry run python -m final calculefrais test.json
```
Avec pour résultat, si on choisit la devise CAD (dollar canadien) et le montant de départ 1500:
```bash
Le montant de départ est de : 1500.0 CAD 
Avec les conversions, le montant est passé à : 1508.06581 CAD
Les frais s élèvent à : 45.0 CAD
Le montant est maintenant de : 1500.0 CAD
Le chemin sélectionné est : ['CAD', 'CAD']
```
