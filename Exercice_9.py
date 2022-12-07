# Fonction de puissance :
def puissance(X,n):
    power = 1
    for i in range(n):
        power = power * X
    return power

# Fonction de la somme des elements :
def SumOfElements(list):
    sum = 0
    for i in list:
     sum += i
       
# Fonction qui renvoie une list triee :
def bubbleSort(list):
    for i in range(len(list) -1):
        for j in range(len(list) -1):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list           

# Fonction qui envoi la valeur moyenne d’une liste :
def moyenne(list):
    sum = 0
    for i in list:
     sum += i
    return sum / len(list)

# Fonction qui renvoie min ou max selon le choix de l'utilisateur :
def max0rmin(liste,choix):
    if(choix == "min"):
        min = list[0]
        for i in range(1,len(list)):
            if(min > list[i]):
                min = list[i]
        return min
    elif(choix == "max"):
        max = list[0]
        for i in range(1,len(list)):
            if(max < list[i]):
                max = list[i]
        return max
    else:
        return "le choix n'est pas correcte" 

# Fonction qui renvoie qui renvoie la median d'une liste :
def median(list):
    sort = bubbleSort(list)  

    if(len(list)%2 == 0):
        res1 = sort[len(sort)//2-1]
        res2 = sort[len(sort)//2]
        return (res1 + res2) / 2
    else:
        return sort[len(sort)//2]

# Fonction qui renvoie le mode d'une list :
def mode(list):
    return max0rmin(list,"max")

# Fonction qui renvoie la variance d'une list:
def variance(list):
    sum = 0
    for i in list: 
        sum += puissance(i,2)  
    return sum/len(list) - puissance(moyenne(list),2)                    