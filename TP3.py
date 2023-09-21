## Exercice 1

print("\n Exercice 1 \n")

def factoriel(n):
    resu = 1
    for i in range(1,n+1):
        resu = resu * i         # On peut aussi écrire | resu *= i | pour aller plus vite
    return resu

# 1) 

# Pour factoriel(0) on nous retourne 1 car on a un seul tour de boucle et resu = 1*1 = 1

# 2)

def somme(n : int): 
    s = 0
    for i in range(n+1):
        s = s + (1/factoriel(i))         # On peut aussi écrire | s += 1/factoriel(i) | pour aller plus vite
    return s

# 3)

def estimation(delta : float):
    n = 1
    while somme(n) < (2.71828 - delta):
        n += 1
    return n

print("estimation(0.0001) =", estimation(0.0001))

## Exercice 2

print("\n Exercice 2 \n")

def termeSuite1(m : int,n : int):
    u = m
    for i in range(1,n+1):
        u = u**2-5
    return u

# 1)

# m représente le premier terme de la suite et n le nombre de termes a calculer

# 2)

print("termeSuite1(4,3) =", termeSuite1(4,3))

''' 
Changement des variables pour termeSuite1(4,3):

u = 4
i = 1
n = 3

1er tour de boucle:

u = 4**2-5 = 11
i = 2

2ème tour de boucle:

u = 11**2-5 = 116
i = 3

3ème tour de boucle:

u = 116**2-5 = 13451
i = 4

Fin de la boucle car i = 4 > n = 3

On retourne u = 13451
'''

# 3)

n = 5
m = 2
print("termeSuite1(5,2) =", termeSuite1(n,m))

# il y a une erreur car on a inversé les variables, ainsi on calcule le terme 2 de la suite avec 5 comme premier terme

# 4)

def termeSuite2(x : float,n : int):
    u = x
    for i in range(1,n+1):
        u = 3/u
    return u

def sommeTermesSuite(n : int,x : float):
    s = 0
    for i in range(n+1):
        s += termeSuite2(x,i)        # Ici j'ai utilisé la manière raccourcie de faire une somme, cela revient au même que | s = s + termeSuite2(x,i) |
    return round(s, 4)        # J'ai arrondi le résultat à 4 chiffres après la virgule pour obtenir le même résultat que dans l'énoncé, round(x, y) permet d'arrondir x à y chiffres après la virgule

print("sommeTermesSuite(5,3.2) =", sommeTermesSuite(5,3.2))

## Exercice 3

print("\n Exercice 3 \n")

# 0)

def fct(n):
    m = 2*n
    return (n,m)

print("fct(4) =", fct(4))
print("type(fct(4)) =", type(fct(4)))

# Le type du retour de fct(4) est un tuple

# 1)

def division_euclidienne(dividende : int, diviseur : int):
    quotient = 0
    reste = dividende
    while reste >= diviseur:
        reste -= diviseur         # Ici j'ai utilisé la manière raccourcie de faire une soustraction, cela revient au même que | reste = reste - diviseur |
        quotient += 1
    return (quotient, reste)

print("division_euclidienne(19,5) =", division_euclidienne(19,5))

# J'ai fais sans le TD3 mais normalement celui-ci n'aura pas d'erreur quelque soit les valeurs de dividende et diviseur

# 3)

from random import randint

def vérification_automatique():
    for i in range(100):
        
        # On génère des nombres aléatoires pour le quotient, le diviseur et le reste
        
        quotient = randint(0,100)
        diviseur = randint(1,100)
        reste = randint(0,100)
        
        # On vérifie si la fonction division_euclidienne retourne bien le bon quotient et le bon reste
        
        if quotient*diviseur+reste != division_euclidienne(quotient*diviseur+reste,diviseur)[0]*diviseur+division_euclidienne(quotient*diviseur+reste,diviseur)[1]:
            return False
    return True

print("vérification_automatique() =", vérification_automatique())

## Exercice 4

print("\n Exercice 4 \n")

# 1)

def est_premier(n : int):
    
    # On vérifie si n est égal à 0 ou 1, si oui on retourne False car 0 et 1 ne sont pas des nombres premiers
    
    if n == 1 or n == 0:
        return False
    
    # On vérifie si n est divisible par un nombre entre 2 et n-1, si oui on retourne False car n n'est pas un nombre premier
    
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print("est_premier(7) =", est_premier(7))
print("est_premier(8) =", est_premier(8))

# 2)

def crible(maxi : int):
    liste = []
    
    # On vérifie si chaque nombre entre 2 et maxi est premier, si oui on l'ajoute à la liste, sinon on ajoute 0
    
    for i in range(1,maxi+1):
        if est_premier(i):
            liste.append(i)
        else:
            liste.append(0)
    return liste

print("crible(8) =", crible(8))

# 3)

def crible_list(maxi : int):
    liste = []
    
    # On vérifie si chaque nombre entre 2 et maxi est premier, si oui on l'ajoute à la liste
    
    for i in range(1,maxi+1):
        if est_premier(i):
            liste.append(i)
    return liste

print("crible_list(16) =", crible_list(16))

# 4)

def verif_list(liste : list):
        
        # On vérifie si chaque nombre de la liste est premier, si oui on retourne True, sinon on retourne False
        
        for i in liste:
            if not est_premier(i):         # Ici j'ai utilisé la manière raccourcie de faire une négation, cela revient au même que | if est_premier(i) == False: |
                return False
        return True
    
print("verif_list(crible_list(16)) =", verif_list(crible_list(16)))

## Exercice 5

print("\n Exercice 5 \n")

# 1)
    
def euclide(nbr1 : int, nbr2 : int):
    while nbr2 != 0:         # Tant que b est différent de 0 on échange a et b et on calcule le reste de la division euclidienne de a par b
        nbr1, nbr2 = nbr2, nbr1%nbr2         # Ici j'ai utilisé la manière raccourcie de faire un échange, cela revient au même que | a = b | et | b = a%b | mais en une seule ligne
    return nbr1

print("euclide(12,8) =", euclide(12,8))

# 2)

def verif(nbr1 : int, nbr2 : int, pgcd : int):
    if euclide(nbr1,nbr2) == pgcd:
        return True
    return False

print("verif(12,8,4) =", verif(12,8,4))

# 3)

print("-------------------------------")

from random import choice

maListe = [14, 25, 8, -2, 9, 3]

for i in range(1, 10):
    print(f"Choice n°{i} : {choice(maListe)}")        # Ici j'ai utilisé la manière raccourcie de faire un print, cela revient au même que | print("Choice n°",i,":",choice(maListe)) | ou | print("Choice n°"+str(i)+":"+str(choice(maListe))) |. str() permet de convertir un nombre en chaîne de caractères

print("-------------------------------")
    
# La fonction choice() permet de choisir un élément aléatoire dans une liste

# 4)

def verif_automatique():
    liste = crible_list(100)
    for i in range(100):
        nbr1 = choice(liste)
        nbr2 = choice(liste)
        pgcd = euclide(nbr1,nbr2)
        if not verif(nbr1,nbr2,pgcd):
            return False
    return True

print("verif_automatique() =", verif_automatique())

## Exercice 6

print("\n Exercice 6 \n")

# 1)

def cube(x : int):
    return (3*x , x**3)

(a,b) = cube(2)
print("a=",a,"     b=",b)

print(f"Le type du retour de la fonction cube() est {type(cube(2))}")

# Le retour de la fonction cube() est un tuple

# la ligne (a,b) = cube(2) permet de stocker les valeurs du tuple dans les variables a et b tel que a = 3*x et b = x**3 et (a,b) forme un nouveau tuple

# 2)

# Fonction de base :

def euclide(nbr1 : int, nbr2 : int):
    while nbr2 != 0:         
        nbr1, nbr2 = nbr2, nbr1%nbr2
    return nbr1

# Fonction avec modifications :
    
def bezout(a, b):
    # Initialisation des variables
    x0, x1, y0, y1 = 1, 0, 0, 1
    
    while b != 0:
        q, a, b = a // b, b, a % b
        x0 = x1
        x1 = x0 - q * x1
        y0 = y1
        y1 = y0 - q * y1
    
    return a, x0, y0

# Cette fonction prend en paramètre deux nombres entiers et retourne un tuple contenant les coefficients de Bézout de ces deux nombres
# Elle fonctionne de la même manière que la fonction euclide() mais on a ajouté des variables u0, v0, u1 et v1 qui permettent de stocker les coefficients de Bézout
# En effet, on a u0 = 1, v0 = 0, u1 = 0 et v1 = 1 au début de la boucle et à chaque tour de boucle on a u0 = u1, v0 = v1, u1 = u0-q*u1 et v1 = v0-q*v1
# On prend u1 = u0-q*u1 et v1 = v0-q*v1 car il existe deux coefficients de Bézout u et v tel que u*a+v*b = pgcd(a,b) et on a u0*a+v0*b = pgcd(a,b) et u1*a+v1*b = pgcd(a,b)

# 3)

def verif_automatique_bezout():
    for i in range(0,10):
        a = randint(0,1000)
        b = randint(0,1000)
        res = bezout(a,b)
        if(res[0] != a*res[1]+b*res[2]):
            return False
    return True

print("verif_automatique_bezout() =", verif_automatique_bezout())

# Il y a peu de chance d'obtenir True car on doit obtenir deux nombres premiers entre 0 et 1000

## Exercice 7

print("\n Exercice 7 \n")

# 1)

def verification_base(nombre : str, base : int):
    for i in nombre:
        if int(i) >= base:
            return False
    return True

print("verification_base('123',4) =", verification_base('123',4)) #True car 1, 2 et 3 sont inférieurs à 4
print("verification_base('123',2) =", verification_base('123',2)) #False car 3 est supérieurs à 2

# 2)

print("-------------------------------")

lis1 = [12, 5, 48, 9, -5, 25]
print(lis1)
print(lis1.pop())
print(lis1)
print(lis1.pop())
print(lis1)

print("-------------------------------")

# La fonction pop() permet de retourner le dernier élément de la liste et supprimer celui-ci de la liste

# 3)

def str_to_int(nombre : str, base : int):
    res = 0
    for i in nombre:
        res = res*base + int(i) # On multiplie le résultat par la base et on ajoute le nombre à la fin pour obtenir le nombre dans la base demandée
    return res

print("str_to_int('110',2) =", str_to_int('110',2))

def int_to_str(nombre : int, base : int):
    res = ""
    while nombre != 0:
        res = str(nombre%base) + res # On ajoute à la fin du résultat le reste de la division euclidienne du nombre par la base
        nombre = nombre//base # On divise le nombre par la base
    return res

print("int_to_str(6,2) =", int_to_str(6,2))

# 4)

def conversion(nombre : str, base_depart : int, base_arrivee : int):
    if verification_base(nombre,base_depart):                                    # On vérifie si le nombre est bien dans la base de départ
        
        # Tout d'abord on convertit le nombre dans la base de départ en entier en base 10
        
        nombre_base_10 = str_to_int(nombre,base_depart)
        
        # Puis on convertit le nombre dans la base d'arrivée en chaine de caractères
        
        nombre_base_arrivee = int_to_str(nombre_base_10,base_arrivee)
        
        return nombre_base_arrivee
        
        
    return "Erreur"

print("conversion('110',2,10) =", conversion('110',2, 10))
# C'est la fonction la plus simple car elle utilise les fonctions str_to_int() et int_to_str() qui sont déjà faites et doit fonctionner pour toutes les bases (même >= 10)

## Exercice 8

print("\n Exercice 8 \n")

# 1)

def traduction(chaine):
    out = []
    for c in chaine:
        out.append(ord(c))
    return out

print("trad('abc') =", traduction('abc'))

# La fonction ord() permet de retourner le code ASCII d'un caractère

# 2)

def correspondance(chaine):
    l = []
    for c in chaine:
        l.append([f"{c} = {ord(c)}"])
    return l

print(correspondance("bonjour"))

# Exercice 9

print("\n Exercice 9 \n")

# 1)

def reduction(texte: str):
    
    # On garde seulement les caractères alphanumériques
    
    for i in texte:
        if not i.isalnum():
            texte = texte.replace(i,"")
    
    # On met le texte en minuscule
    
    texte = texte.lower()
    
    return texte

# La fonction isalnum() permet de vérifier si un caractère est alphanumérique, c'est une fonction qui se met à la du caractère à vérifier (Tu me demanderas si tu veux comprendre pourquoi on le met a la fin)

# 2)

def verif_manuelle(texte : str, resultat : str):
    texte = reduction(texte)
    if texte == resultat:
        return True
    return False

def verif_automatique():
    for i in range(100):       # On teste 100 fois
        texte = ""
        for j in range(10):
            texte += chr(randint(33,126))      # On ajoute un caractère aléatoire entre ! et ~ (Table ASCII disponible ici : https://fr.wikipedia.org/wiki/Fichier:ASCII-Table.svg)
        if not verif_manuelle(texte, reduction(texte)):
            return False
    return True

print("verif_automatique() =", verif_automatique())
print("verif_manuelle('Bonjour!', 'bonjour') =", verif_manuelle('Bonjour', 'bonjour'))

# 3)

def cesar(s,decalage):
    s = reduction(s)
    out = ""
    for c in s:
        ascii = ord(c)
        if ascii >= 97 and ascii <= 122:
            ascii = (ascii - 97 + decalage)%26 + 97
            # On fait -97 pour avoir un nombre entre 0 et 25, on ajoute le décalage et on fait %26 pour avoir un nombre entre 0 et 25, on ajoute 97 pour avoir un nombre entre 97 et 122, comme ca on a un caractère entre a et z, ce qui permet de rester sur l'alphabet
        out += chr(ascii)
    return out

print("cesar('Bonjour!', 3) =", cesar('Bonjour!', 3))

## Exercice 10

print("\n Exercice 10 \n")

# 1)

def triangle(n : int):
    for i in range(n):
        print(" "*(n-i-1),"X"*(2*i+1),sep="")
        
triangle(3)

'''
Explication du fonctionnement de la ligne print(" "*(n-i-1),"X"*(2*i+1),sep="")

ici notre print est composé de 3 éléments : " "*(n-i-1), "X"*(2*i+1) et sep=""

" "*(n-i-1) permet d'afficher n-i-1 espaces, on a n-i-1 car on veut que le triangle soit centré, ainsi on a n-i-1 espaces avant la première ligne, n-i-2 espaces avant la deuxième ligne, etc...

"X"*(2*i+1) permet d'afficher 2*i+1 X, on a 2*i+1 car on veut que le triangle soit centré, ainsi on a 1 X sur la première ligne, 3 X sur la deuxième ligne, etc...

sep="" permet de ne pas avoir d'espace entre les éléments du print, ainsi on a un triangle centré, exemple print("a","b",sep="") affiche ab et print("a","b") affiche a b


'''


# --------------------------------


'''

Explication des fonctions en python :

def nom_de_la_fonction(paramètre1 : type, paramètre2 : type, ...):
    # Code de la fonction
    return valeur_de_retour
    
Pour déclarer une fonction on utlise le mot clé 'def' suivi du nom de la fonction et des paramètres entre parenthèses, on peut mettre plusieurs paramètres séparés par des virgules

Ensuite on met ':' et on passe à la ligne, on met le code de la fonction en respectant l'indentation (4 espaces ou 1 tabulation)

Pour retourner une valeur on utilise le mot clé 'return' suivi de la valeur à retourner

On peut accesoirement mettre les types des parametres en mettant ': type' après le nom du paramètre, cela permet de vérifier que les paramètres sont bien du bon type (Vraiment pas obligatoire mais c'est mieux de le faire)

'''