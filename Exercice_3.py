# Fonction qui calcul la factorielle d'un nombre donne :
def factorielle(n):
    if(n > 0):
        F = 1
        for i in range(1,n+1):
            F = F * i
        return F
    return 1

# Fonction pour trouver la somme des series 1!/1 + 2!/2 + 3!/3 + 4!/4 + 5!/5 :

def sommeSerie(n):
    if(n <= 0):
        return "le nombre doit etre strictement positif"
    else:
        sum = 0
        for i in range(1,n+1):
            sum = 0
        for i in range(1,n+1):
            sum = sum +factorielle(i-1)
        return sum           