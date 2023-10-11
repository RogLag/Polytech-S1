# Q1

def Q1_total(n):
    somme = 0
    for k in range(1, n+1):
        somme += 1/(5*(k**2)+4)
    return somme

print(Q1_total(3))

# Q2

def Q2_addition(x):
    # x est une liste dont on veut calculer la somme de toutes les données à la suite
    somme = 0
    for k in range(len(x)-1):
        somme += (4*k - 5)*((x[k])**2)
    return somme

print(Q2_addition([1,5,3]))

# Q3

def Q3_suite(n):
    liste = []
    for i in range(n+1):
        if (i%4 == 0) or (i%5 != 0):
            liste.append(i)
    return liste

print(Q3_suite(20))

# Q4

def Q4_liste(x,n):
    liste = [x]
    for i in range(n):
        un = 9*liste[-1] + 6
        liste.append(un)
    return liste

print(Q4_liste(1,8))

# Q5

def Q5_somme(x,n):
    liste = Q4_liste(x,n)
    somme = 0
    for i in liste:
        somme += i
    return somme

print(Q5_somme(1,8))

# Q6

def Q6_premier(x,y):
    un = x
    n = 0
    while un < y:
        un = 9*un + 6
        n += 1
    return n

print(Q6_premier(1,399999))

# Q7

def Q7_enumerer(x,n):
    liste = Q4_liste(x,n)
    for i in liste:
        print(i)
    return None

Q7_enumerer(1,8)

# Q8

def Q8_formule(x,n):
    liste = Q4_liste(x,n)
    return liste[-1]

print(Q8_formule(1,8))

# Q9

def Q9_affiche(u):
    resultat = ""
    for i in u:
        resultat += "{"+str(i)+"}"
    print(resultat)
    return None

Q9_affiche(Q4_liste(1,8))

# Q10

def Q10_calcul(u,v):
    if u != (v**3):
        return (7*u*v)/(u-(v**3))
    else:
        return (3*u)+(4*v)

u = 3

print(Q10_calcul(u,u**3))

v = 10

print(Q10_calcul(u,10))
