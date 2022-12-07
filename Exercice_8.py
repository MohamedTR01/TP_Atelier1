# Fonction qui cherche un element dans une matrice puis renvoi sa position «« i,j »» :

def searchElementInMatrix(matrix,num):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == num):
                return "la position de %d est <<"%(num,i,j)
        return "le nombre %d n'existe pas dans cette matrice"%(num)        
matri = [[1,23,3],[5,6,8],[9,3,56]]
print(searchElementInMatrix(3,1,3))