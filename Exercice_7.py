# Fonction qui trouve la frequence d'un caractere dans une chaîne :

def FrequenceChar(str1, char):
    count = 0
    for i in str1:
        if(i == char):
            count += 1
    return count        