class Reservoir():
    # Un dictionnaire pour stocker tous les réservoirs créés
    lesReservoirs = {}

    # Le constructeur de la classe Reservoir
    def __init__(self, id, analyses, capacite = 0):
        # Initialisation des attributs de l'instance
        self.id = id
        self.analyses = analyses
        self.capacite = capacite

        # Calcul du pH moyen à partir des analyses
        phMoyen = self.moyenne(analyses)[0]

        # Ajout du réservoir au dictionnaire des réservoirs
        Reservoir.lesReservoirs[id] = (capacite, phMoyen)

    # Méthode pour afficher les informations du réservoir
    def affiche(self):
        print(f"*** Réservoir {self.id.split('-')[0]} situé à {self.id.split('-')[1]} ***")
        print(f"Capacité : {self.capacite} m3")
        print(f"Analyses :")
        for a in self.analyses:
            print(f"  pH: {a[0]} - En mg/l: Sulfates: {a[1]} , Chlorures: {a[2]} , Nitrates: {a[3]}")

    # Méthode statique pour vérifier si le pH est acceptable
    @staticmethod
    def phOK(ph):
        return 6.5 <= ph <= 8

    # Méthode pour calculer la moyenne des analyses
    def moyenne(self, analyses):
        moyenne = [0, 0, 0, 0]
        for analyse in analyses:
            for i in range(4):
                moyenne[i] += analyse[i]
        for i in range(4):
            moyenne[i] = round(moyenne[i]/len(analyses), 2)
        return moyenne

    # Méthode appelée lorsque l'objet est détruit
    def __del__(self):
        del Reservoir.lesReservoirs[self.id]

    # Méthode pour obtenir tous les réservoirs avec un pH acceptable
    def reservoirsOK(self):
        reservoirsOK = {}
        for id in Reservoir.lesReservoirs:
            if self.phOK(Reservoir.lesReservoirs[id][1]) == True:
                reservoirsOK[id] = Reservoir.lesReservoirs[id]
        return reservoirsOK
    
# La classe ChateauDEau hérite de la classe Reservoir
class ChateauDEau(Reservoir):
        
    # Le constructeur de la classe ChateauDEau
    def __init__(self, id, analyses, capacite = 0, hauteur = 0, pression = 0, contenu = 0, consommations = []):
        # On appelle le constructeur de la classe parente Reservoir
        super().__init__(id, analyses, capacite)
        # Initialisation des attributs spécifiques à la classe ChateauDEau
        self.hauteur = hauteur
        self.pression = pression
        self.contenu = contenu
        self.consommations = consommations
        
    # Méthode pour afficher les informations du château d'eau
    def affiche(self):
        print(f"*** Chateau d'eau {self.id} ***")
        print(f"Hauteur : {self.hauteur} m, pression : {self.pression} bars, capacité : {self.capacite} m3")
        print(f"Analyses")
        for a in self.analyses:
            print(f"  pH: {a[0]} - En mg/l: Sulfates: {a[1]} , Chlorures: {a[2]} , Nitrates: {a[3]}")
    
    # Méthode pour remplir le château d'eau avec un certain débit
    def remplit(self, debit):
        # Si le contenu actuel plus le débit est inférieur ou égal à la capacité
        if self.contenu + debit <= self.capacite:
            # On ajoute le débit au contenu
            self.contenu += debit
        else:
            # Sinon, on remplit le château d'eau à sa capacité maximale
            self.contenu = self.capacite
        return None
    
    # Méthode pour distribuer de l'eau à partir du château d'eau avec un certain débit
    def distribue(self, debit):
        # Si le contenu actuel moins le débit est supérieur ou égal à zéro
        if self.contenu - debit >= 0:
            # On ajoute le débit aux consommations et on soustrait le débit du contenu
            self.consommations.append(debit)
            self.contenu -= debit
        else:
            # Sinon, on ajoute le contenu restant aux consommations et on vide le château d'eau
            self.consommations.append(self.contenu)
            self.contenu = 0
        return None
    
    # Méthode pour afficher les consommations d'eau du château d'eau
    def afficheConsommations(self):
        print(f"--- Chateau d'eau {self.id} ---")
        print(f"Hauteur de la cuve : {self.hauteur} m, pression : {self.pression} bar")
        print(f"Capacité : {self.capacite} m3, contenu : {self.contenu} m3")
        print(f"Analyses")
        for a in self.analyses:
            print(f"  pH: {a[0]} - En mg/l: Sulfates: {a[1]} , Chlorures: {a[2]} , Nitrates: {a[3]}")
        print(f"Consommations :")
        for c in self.consommations:
            print(f"{c} {"* " * round(c/100*13)}")
        return None

"""
Pour faire mes tests je vais utiliser les asserts, qui permettent de vérifier que les valeurs renvoyées par les méthodes sont bien celles attendues.

En Python, le mot-clé assert est utilisé pour le débogage et le test de code. 
Il permet de vérifier si une certaine condition est vraie. Si la condition est vraie, le programme continue de s'exécuter normalement. 
Cependant, si la condition est fausse, le programme arrête son exécution et génère une exception AssertionError. 
Les assertions sont généralement utilisées pour vérifier l'intégrité des données ou la validité des états du programme. 
Elles sont très utiles pour attraper les bugs tôt dans le cycle de développement, 
car elles permettent de détecter les erreurs de logique et les conditions qui ne devraient jamais se produire.

Celà permet de ne pas avoir à vérifier manuellement les valeurs renvoyées par les méthodes et de ne pas remplir le terminal de print().
On ne print que les tests qui ne peuvent pas être vérifiés par les asserts, comme les affichages des méthodes affiche() et afficheConsommations().

Pour ton partiel, je te conseil de ne pas utiliser les asserts, mais de vérifier manuellement les valeurs renvoyées par les méthodes.
Comme sa si une méthode ne renvoie pas la bonne valeur, tu pourras quand même continuer à tester les autres méthodes et comprendre d'où vient l'erreur visuellement.

Là, je l'ai utilisé pour gagner du temps et ne pas avoir à vérifier manuellement les valeurs renvoyées par les méthodes.

La syntaxe des asserts est la suivante :
assert <condition>

Exemple :
<conditon> : a == b

assert a == b

Si la condition est vraie, le programme continue de s'exécuter normalement.
Si la condition est fausse, le programme arrête son exécution et génère une erreur et te retourne la ligne de l'assert qui a échoué.
"""
    
    
    
    
## Code permettant de tester pour la 1ere partie



# On crée un objet Reservoir appelé "test" avec des paramètres spécifiques
test = Reservoir("451-Montjoyeux", [(7.4, 20.8, 24.9, 0.01), (7.5, 25, 20, 0.02), (7.3, 27, 22.9, 0.01)], capacite=50000)

print("\n")  # On imprime une ligne vide pour séparer les sections du code

test.affiche()  # On appelle la méthode affiche() sur l'objet test pour afficher ses informations

# On vérifie que la méthode phOK() renvoie False quand le pH est 5
assert test.phOK(5) == False
# On vérifie que la méthode phOK() renvoie True quand le pH est 7.2
assert test.phOK(7.2) == True

# On vérifie que la méthode moyenne() renvoie la moyenne correcte pour une liste d'analyses
assert test.moyenne([(7.4, 20.8, 24.9, 0.01), (7.5, 25, 20, 0.02), (7.3, 27, 22.9, 0.01)]) == [7.4, 24.27, 22.6, 0.01]


## --------------------------------------------------------------------------------------------------------------------------------------------------


## Code permettant de tester pour la 2eme partie



# On crée deux autres objets Reservoir appelés "test2" et "test3" avec des paramètres spécifiques
test2 = Reservoir("338-Abilly", [(7, 19, 24.9, 0.01), (5, 21.5, 22.3, 0.02), (5.1, 29.2, 22.7, 0.01)], capacite=450)
test3 = Reservoir("548-Villaines", [(7.4, 20.8, 24.9, 0.01), (7.2, 25, 20, 0.02), (7.0, 27, 22.9, 0.01)], capacite=1000)

# On vérifie que la méthode reservoirsOK() renvoie les bons réservoirs avec un pH acceptable
assert test2.reservoirsOK() == {'451-Montjoyeux': (50000, 7.4), '548-Villaines': (1000, 7.2)}

# On vérifie que le dictionnaire lesReservoirs contient bien tous les réservoirs créés
assert Reservoir.lesReservoirs == {'451-Montjoyeux': (50000, 7.4), '338-Abilly': (450, 5.7), '548-Villaines': (1000, 7.2)}

# On supprime l'objet test2
del test2

# On vérifie que le dictionnaire lesReservoirs ne contient plus le réservoir supprimé
assert Reservoir.lesReservoirs == {'451-Montjoyeux': (50000, 7.4), '548-Villaines': (1000, 7.2)}


## --------------------------------------------------------------------------------------------------------------------------------------------------


## Code permettant de tester pour la 3eme partie



# On crée un nouvel objet ChateauDEau appelé "test4" avec des paramètres spécifiques
test4 = ChateauDEau("751-Veretz", [(7, 19.1, 24.6, 0.02), (7.8, 27.1, 18.5, 0.02)], capacite=600, hauteur=38, pression=3)

print("\n")  # On imprime une ligne vide pour séparer les sections du code

# On appelle la méthode affiche() sur l'objet test4 pour afficher ses informations
test4.affiche()

# On supprime l'objet test4
del test4


## --------------------------------------------------------------------------------------------------------------------------------------------------


## Code permettant de tester pour la 4eme partie



# On crée un nouvel objet ChateauDEau appelé "test5" avec des paramètres spécifiques
test5 = ChateauDEau("751-Veretz", [(7, 19.1, 24.6, 0.02), (7.8, 27.1, 18.5, 0.02)], capacite=1500, hauteur=38, pression=4)

# On remplit le château d'eau avec 1500 unités d'eau
test5.remplit(1500)

# On distribue de l'eau à partir du château d'eau avec différents débits
test5.distribue(100)
test5.distribue(15)
test5.distribue(148)
test5.distribue(300)

print("\n")  # On imprime une ligne vide pour séparer les sections du code

# On appelle la méthode afficheConsommations() sur l'objet test5 pour afficher ses consommations d'eau
test5.afficheConsommations()