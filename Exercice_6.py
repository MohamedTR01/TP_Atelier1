# La foncion pour compter les chiffre d'un nombre donne

def chiffreNombre(n):
    if n == 0:
        return 1
    else:
        count = 0
        while(n > 0):
            count += 1
            n//=10
        return count    

