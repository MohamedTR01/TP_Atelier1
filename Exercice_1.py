# Fonction qui renvoie la puissance d'un nombre Xn :

def puissance(X,n) :
    power = 1
    for i in range (n) :
        power = power * X
    return power 

# Or

def Puissance(x,n):
    return x**n