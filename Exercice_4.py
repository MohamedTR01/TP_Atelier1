# Fonction qui convertir le nombre decimal en nombre binaire :

def DecimalToBinary(n):
    if n == 0:
        return 0
    else:
         res = ""

         while(n > 0):
            r = n%2
            res = str(r)+res
            n //= 2
         return int(res)
