## Exercice 5:

def nettoie_chaine(chaine: str) -> list:
    
    result = "" # On initialise une chaine vide pour stocker les chiffres
    
    for i in range(0, len(chaine)): # On parcourt la chaine
        if chaine[i].isdigit() or chaine[i] == ';': # On ne garde que les chiffres et les points-virgules
            result += chaine[i] # On ajoute le chiffre ou le point-virgule à la chaine
            
    result = result.split(';') # On sépare les chiffres par les points-virgules
    
    for i in range(0, len(result)): # On parcourt la liste
        result[i] = int(result[i]) # On transforme les chiffres en entiers

    return result # On retourne la liste

print(nettoie_chaine("44RRR5T;6555;HHS79")) 



## Exercice 6:

def est_palindrome(chaine: str) -> bool:
    
    return chaine == chaine[::-1] # On retourne True si la chaine est égale à sa version inversée, sinon False

print(est_palindrome("kayak"))
print(est_palindrome("radar"))
print(est_palindrome("raddar"))
print(est_palindrome("test"))



## Exercice 7:

def code(chaine: str, cle: str) -> str:
    
    result = "" # On initialise une chaine vide pour stocker la chaine codée

    alphabet = "abcdefghijklmnopqrstuvwxyz" # On initialise l'alphabet
    
    dic = {} # On initialise un dictionnaire vide
    
    for i in range(0, len(cle)): # On parcourt la cle
        dic[alphabet[i]] = cle[i] # On ajoute la lettre de la cle au dictionnaire avec la lettre de l'alphabet

    for i in range(0, len(chaine)): # On parcourt la chaine
        result += dic[chaine[i]] # On ajoute la lettre de la chaine correspondante à la cle dans le dictionnaire
    
    return result # On retourne la chaine codé

def code2(chaine: str, cle: str) -> str:
    
    result = "" # On initialise une chaine vide pour stocker la chaine codée

    for i in range(0, len(chaine)): # On parcourt la chaine
        result += cle[ord(chaine[i])-97] # On ajoute la lettre de la chaine codée à la chaine, ici on utilise ord pour avoir le code ASCII de la lettre et on retire 97 pour avoir la position de la lettre dans l'alphabet

    return result # On retourne la chaine codée
        

print(code("bonjour", "azertyuiopqsdfghjklmwxcvbn"))
print(code2("bonjour", "azertyuiopqsdfghjklmwxcvbn"))

def decode(chaine: str, cle: str) -> str:
    
    result = "" # On initialise une chaine vide pour stocker la chaine décodée

    alphabet = "abcdefghijklmnopqrstuvwxyz" # On initialise l'alphabet
    
    dic = {} # On initialise un dictionnaire vide
    
    for i in range(0, len(cle)): # On parcourt la cle
        dic[cle[i]] = alphabet[i] # On ajoute la lettre de la cle au dictionnaire avec la lettre de l'alphabet

    for i in range(0, len(chaine)): # On parcourt la chaine
        result += dic[chaine[i]] # On ajoute la lettre de la chaine correspondante à la cle dans le dictionnaire

    return result # On retourne la chaine décodée

def decode2(chaine: str, cle: str) -> str:
    
    result = "" # On initialise une chaine vide pour stocker la chaine décodée

    for i in range(0, len(chaine)): # On parcourt la chaine
        result += chr(cle.index(chaine[i])+97) # On ajoute la lettre de la chaine codée à la chaine, ici on utilise chr pour avoir le charactère correspondant au code ASCII au quel on a ajouté 97 pour avoir la position de la lettre dans l'alphabet

    return result # On retourne la chaine décodée


print(decode(code("bonjour", "azertyuiopqsdfghjklmwxcvbn"), "azertyuiopqsdfghjklmwxcvbn"))
print(decode2(code2("bonjour", "azertyuiopqsdfghjklmwxcvbn"), "azertyuiopqsdfghjklmwxcvbn"))



## Exercice 8:

def calcul_crc1(chaine: str, cle: int) -> int:

    result = 0 # On initialise un entier à 0 pour stocker la somme des codes
    
    for i in range(0, len(chaine)): # On parcourt la chaine
        result += ord(chaine[i]) # On ajoute le code ASCII de la lettre de la chaine à la somme

    return result % cle # On retourne la somme modulo la cle

print(calcul_crc1("bonjour", 256))

def calcul_crc2(chaine: str, cle: int) -> int:
    result = 0 # On initialise un entier à 0 pour stocker la somme des codes
    
    for i in range(0, len(chaine)): # On parcourt la chaine
        result += ord(chaine[i]) % cle # On ajoute le code ASCII de la lettre de la chaine multiplie par la cle à la somme
    
    return result # On retourne la somme

print(calcul_crc2("bonjour", 256))
