def saisie():
    y = float(input("entrer un réel y tq 0<y<2: "))
    while y<=0 or y>=2:
        y = float(input("non, y tq 0<y<2: "))
    return y

import math

def suitesConjointes(x,y,n):
    u = x
    v = y
    for i in range(n):
        u1 = abs(u + math.log(abs(v)))
        v1 = (u + v)/2
        u = u1
        v = v1
    return (u,v)

def listeU(x,y,n):
    liste_de_u = [x]
    v = y
    for i in range(n):
        u1 = abs(liste_de_u[-1] + math.log(abs(v)))
        v1 = (liste_de_u[-1] + v)/2
        liste_de_u.append(u1)
        v = v1
        print(liste_de_u[-1],v)
    return liste_de_u

print(listeU(3,1.1,4))

# Probleme dans le sujet, on ne peut pas obtenir la meme chose, les données sont fausses

import random

def test(n):
    print("Test :")
    for i in range(10):
        u0 = random.randint(1,10)
        v0 = random.uniform(0,2)
        print(listeU(u0,v0,n))
    return None

def rangcroissant(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return i
    return False

# La question 6 est infaisable car les deux suites sont strictements croissantes car dès que Un > 2, Vn > 1 et donc Un+1 > Un
