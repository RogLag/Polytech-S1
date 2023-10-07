print(f"-------------------\nCC1.py\n-------------------\n")

# Fonction donnée dans l'énoncé

def estPremier(n):
    nb = 0
    for i in range(1, n+1):
        if n % i == 0:
            nb += 1
    if nb == 2:
        return True
    else:
        return False

## Question 1

print(f"-------------------\nQuestion 1\n-------------------\n")

from math import log

def estDeMersenne(n):
    # On vérifie que n est un entier
    if int(n) != n:
        return False
    # On vérifie que n est un nombre de Mersenne
    if log(n+1, 2) != int(log(n+1, 2)):
        return False
    return True

print(f"estDeMersenne(2047) : {estDeMersenne(2047)}")
print(f"estDeMersenne(758) : {estDeMersenne(758)}")

# Fonction assez complexe donc je t'ai fait un résumé en dessous pour tout comprendre ( j'espère :) )

'''
La fonction log est une fonction de la bibliothèque math qui permet de calculer le logarithme népérien d'un nombre.
Elle prend en paramètre le nombre dont on veut calculer le logarithme et la base du logarithme : log(n, base).

Ici, on veut calculer le logarithme en base 2 de n+1 car on cherche une puissance de 2.
On prend n+1 car pour que n soit un nombre de Mersenne, il faut que n+1 soit une puissance de 2.

De manière simple, n doit pouvoir s'écrire sous la forme 2^k - 1.
Donc si on ajoute 1 à n, on obtient une puissance de 2 tel que n+1 = 2^k.
On vérifie ensuite que le logarithme en base 2 est un entier.

Si c'est le cas, alors n est un nombre de Mersenne.
Sinon n n'est pas un nombre de Mersenne.
'''

print(f"\n")

# Voici une autre façon de faire la fonction estDeMersenne en très court :

def estDeMersenneCourt(n):
    return int(log(n+1, 2)) == log(n+1, 2)

print(f"estDeMersenneCourt(2047) : {estDeMersenneCourt(2047)}")
print(f"estDeMersenneCourt(758) : {estDeMersenneCourt(758)}")

# Explication rapide de pourquoi ça marche en une ligne :

'''
Lorsque l'on met une condition dans un return, la fonction va renvoyer True si la condition est vérifiée et False sinon.
Donc ici, on vérifie que le logarithme en base 2 de n+1 est un entier.
Si c'est le cas, alors la fonction renvoie True et donc n est un nombre de Mersenne car n+1 est une puissance de 2.
Sinon, la fonction renvoie False et donc n n'est pas un nombre de Mersenne.
'''

## Question 2

print(f"\n-------------------\nQuestion 2\n-------------------\n")

def listeMersenne(n):
    # On initialise une liste vide et un compteur à 1
    liste = []
    compteur = 1
    # On ajoute à la liste tous les nombres de Mersenne que l'on trouve jusqu'à ce que la liste ait la longueur demandée
    while len(liste) < n:
        if estDeMersenne(compteur):
            liste.append(compteur)
        compteur += 1
    return liste

print(f"listeMersenne(10) : {listeMersenne(10)}")

# Explications

'''
L'objectif de cette fonction est de renvoyer une liste des n premiers nombres de Mersenne.
On initialise donc une liste vide et un compteur à 1. ( On ne commence pas à 0 car 0 n'est pas un nombre de Mersenne alors que 1 est un nombre de Mersenne car 1 = 2^0 - 1 )
Ensuite, on va ajouter à la liste tous les nombres de Mersenne que l'on trouve jusqu'à ce que la liste ait la longueur demandée.
Pour cela, on utilise une boucle while qui s'arrête lorsque la liste a la longueur demandée.
Dans la boucle, on vérifie si le compteur est un nombre de Mersenne, il est donc important de l'incrémenter à la fin de la boucle.
'''

## Question 3

print(f"\n-------------------\nQuestion 3\n-------------------\n")

def listeMersennePremiers(n):
    # On initialise une liste vide et un compteur à 1
    liste = []
    compteur = 1
    # On ajoute à la liste tous les nombres de Mersenne premiers que l'on trouve jusqu'à ce que la liste ait la longueur demandée
    while len(liste) < n:
        if estDeMersenne(compteur) and estPremier(compteur):
            liste.append(compteur)
        compteur += 1
    return liste

print(f"listeMersennePremiers(7) : {listeMersennePremiers(7)}")

# Explications

'''
Cette fonction est très similaire à la fonction précédente.
La seule différence est que l'on vérifie si le compteur est un nombre de Mersenne ET un nombre premier en même temps.
'''

## Question 4

print(f"\n-------------------\nQuestion 4\n-------------------\n")

def test(n):
    # On génère la liste des n premiers nombres de Mersenne premiers
    liste = listeMersennePremiers(n)
    # On initialise une liste vide qui va contenir les exposants des nombres de Mersenne premiers
    listeExposants = []
    # On parcourt la liste des nombres de Mersenne premiers
    for i in range(len(liste)):
        # On calcule l'exposant de chaque nombre de Mersenne premier
        exposant = int(log(liste[i]+1, 2))
        # On ajoute l'exposant à la liste des exposants
        listeExposants.append(exposant)
    tousPremiers = True
    # On test ensuite si les exposants sont premiers
    for i in listeExposants:
        if estPremier(i) == False:
            tousPremiers = False
            # On utilise le break car on a trouvé un contre exemple donc pas besoin de tous les tester, on arrête donc la boucle
            break
    # On initialise une chaîne de caractères vide qui va contenir les exposants de la même manière que dans l'énoncé
    resultat = ""
    # On parcourt la liste des exposants et on ajoute chaque exposant à la chaîne de caractères en ajoutant un point virgule à la fin
    for i in listeExposants:
        resultat += f"{i} ; "
    # On vérifie si tous les exposants sont premiers ou non et on affiche le résultat de la manière demandée
    if tousPremiers:
        print(f"{resultat}  ils sont bien tous premier")
    else:
        print(f"{resultat}  ils ne sont pas tous premier")
    # Comme dans l'énoncé il n'est pas demandé de renvoyer quelque chose, on renvoie None pour éviter d'avoir une erreur quelque part et cela n'a pas d'impact sur le résultat
    return None

test(7) # Ne pas mettre au dessus de 7 car sinon ça prend beaucoup de temps à s'exécuter car la fonction est d'une difficulté exponentielle, c'est à dire qu'elle prend beaucoup de temps à s'exécuter lorsque n augmente, 7 est le dernier nombre résonnable à tester (comme dans l'énoncé)

# Explications

'''
Cette fonction est assez complexe donc je vais essayer de l'expliquer au mieux.

On commence par générer la liste des n premiers nombres de Mersenne premiers grâce à la fonction de la question 3.
Ensuite, on initialise une liste vide qui va contenir les exposants des nombres de Mersenne premiers car on va devoir tester si ces exposants sont premiers.
On parcourt donc la liste des nombres de Mersenne premiers et on calcule l'exposant de chaque nombre de Mersenne premier.

Pour cela, on utilise la fonction log de la bibliothèque math comme dans la question 1.
En effet l'exposant d'un nombre de Mersenne vaut le calcule suivant : log(n+1, 2).

On ajoute ensuite l'exposant à la liste des exposants.
On a donc maintenant une liste des exposants des nombres de Mersenne premiers.

On initialise ensuite une variable booléenne qui va nous permettre de savoir si tous les exposants sont premiers ou non.
On parcourt la liste des exposants et on vérifie si chaque exposant est premier ou non.
Si un des exposants n'est pas premier, on met la variable booléenne à False.
On utilise le break car on a trouvé un contre exemple donc pas besoin de tous les tester, on arrête donc la boucle.

On initialise ensuite une chaîne de caractères vide qui va contenir les exposants de la même manière que dans l'énoncé.
On parcourt la liste des exposants et on ajoute chaque exposant à la chaîne de caractères en ajoutant un point virgule à la fin.

On vérifie si tous les exposants sont premiers ou non et on affiche le résultat de la manière demandée.

Comme dans l'énoncé il n'est pas demandé de renvoyer quelque chose, on renvoie None pour éviter d'avoir une erreur quelque part et cela n'a pas d'impact sur le résultat.
'''

## Question 5

print(f"\n-------------------\nQuestion 5\n-------------------\n")

def testReciproque(n):
    # On initialise une liste vide et un compteur à 1
    listePremiers = []
    compteur = 1
    # On ajoute à la liste tous les nombres premiers que l'on trouve jusqu'à ce que la liste ait la longueur demandée
    while len(listePremiers) < n:
        if estPremier(compteur):
            listePremiers.append(compteur)
        # On incrémente le compteur de 1 à chaque tour de boucle
        compteur += 1
    # On initialise une liste vide qui va contenir les nombres de Mersenne
    listeMersenne = []
    # On parcourt la liste des nombres premiers pour calculer les nombres de Mersenne
    for i in listePremiers:
        listeMersenne.append(2**i - 1)
    # On initialise une liste vide qui va contenir les nombres premiers qui ne génèrent pas de nombres de Mersenne premiers
    nonPremiers = []
    # On test ensuite si les nombres de Mersenne sont premiers
    for i in range(len(listeMersenne)):
        if estPremier(listeMersenne[i]) == False:
            nonPremiers.append(listePremiers[i])
    # On affiche le résultat de la manière demandée
    if len(nonPremiers) == 0:
        print(f"Les 2**i-1 avec i premier sont bien tous premiers jusqu'à i= {listePremiers[-1]}")
    else:
        print(f"Les 2**i-1 avec i premier ne sont pas premiers pour i dans: {nonPremiers}")
    # Comme dans l'énoncé il n'est pas demandé de renvoyer quelque chose, on renvoie None pour éviter d'avoir une erreur quelque part et cela n'a pas d'impact sur le résultat
    return None

testReciproque(4)
testReciproque(9)
        
# Explications

'''
Cette fonction est très complexe mais elle possède beaucoup de similitudes avec la fonction de la question 4.

On commence par générer la liste des n premiers nombres premiers grâce à une boucle while.
Ensuite, on initialise une liste vide qui va contenir les nombres de Mersenne.
On parcourt donc la liste des nombres premiers et on calcule le nombre de Mersenne correspondant à chaque nombre premier.
Pour cela, on utilise la formule suivante : 2^i - 1 où i est le nombre premier.
On ajoute ensuite le nombre de Mersenne à la liste des nombres de Mersenne.
On a donc maintenant une liste des nombres de Mersenne.

On initialise ensuite une liste vide qui va contenir les nombres premiers qui ne génèrent pas de nombres de Mersenne premiers.
On parcourt la liste des nombres de Mersenne et on vérifie si chaque nombre de Mersenne est premier ou non.
Si un des nombres de Mersenne n'est pas premier, on ajoute le nombre premier correspondant à la liste des nombres premiers qui ne génèrent pas de nombres de Mersenne premiers.

On affiche le résultat de la manière demandée.

Comme dans l'énoncé il n'est pas demandé de renvoyer quelque chose, on renvoie None pour éviter d'avoir une erreur quelque part et cela n'a pas d'impact sur le résultat.
'''