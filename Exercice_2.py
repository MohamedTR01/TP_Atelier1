# Fonction qui calcul la factorielle d'un nombre donne :
def factorielle(n):
    if(n > 0):
        F = 1
        for i in range (1,n+1):
            F = F * i
        return F
    return 1
