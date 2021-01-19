import numpy as np

def naiveMatrixMult(matrix1, matrix2):
    resMatrix = [[None for col in matrix2[0]] for row in matrix1]
    if len(matrix1[0]) == len(matrix2):
        for row in range(len(matrix1)):
            for col in range(len(matrix2[0])):
                sum = 0
                for k in range(len(matrix2)):
                    sum += matrix1[row][k] * matrix2[k][col]
                resMatrix[row][col] = sum
        
        return resMatrix
    else:
        return "Invalid Matrix Multiplication"


# print(naiveMatrixMult([[1,2],[3,4]], [[5,6],[7,8]]))