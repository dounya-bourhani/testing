def diag(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if i == j: 
                tableau[i][j] = "diag"
    return tableau
    
tableau = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diag(tableau))