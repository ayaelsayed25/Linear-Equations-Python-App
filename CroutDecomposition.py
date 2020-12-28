import math
from copy import deepcopy
from substitute import *

padding = 20
formatting = '{:' + str(padding) + '}'


def crout(matrix, b, dimension, number_of_significant_figures):
    answer = ''
    L = [[0 for x in range(dimension)] for y in range(dimension)]
    U = [[0 for x in range(dimension)] for y in range(dimension)]
    answer = answer + "A :\n"
    answer = answer + print_Matrix(matrix)
    answer = answer + "\n\nA = L * U\n"
    # Substituting 1s in the diagonal of [U] :
    for i in range(0, dimension):
        U[i][i] = 1

    #  Calculating the first column of [L]:
    for i in range(0, dimension):
        L[i][0] = roundNumber(matrix[i][0], number_of_significant_figures)

    samlpleL = deepcopy(L)
    for i in range(1, dimension):
        for j in range(0, i):
            samlpleL[i][j] = f"L{i}{j}"
    answer = answer + "\n\nL :\n"
    answer = answer + print_Matrix(samlpleL)
    sampleU = deepcopy(U)
    for i in range(dimension, 0, -1):
        for j in range(i, dimension):
            sampleU[i][j] = f"U{i}{j}"
    answer = answer + "\n\nU :\n"
    answer = answer + print_Matrix(sampleU)
    answer = answer + "\n\n"
    #  Calculating the elements in the first row of [U] (except U11 which was already calculated)
    for i in range(1, dimension):
        U[0][i] = matrix[0][i] / L[0][0]
        U[0][i] = roundNumber(U[0][i], number_of_significant_figures)
    # Calculating the rest of the elements row after row
    for i in range(1, dimension):
        for j in range(1, i + 1):
            sigma_sum = 0
            # The elements of [L] are calculated first because they are used for calculating the elements of [U]
            answer = answer + f"L{i}{j} = A{i}{j} − \u03A3 L{i}k * Uk{j} where k is 0 :  {j - 1}\n\u03A3 = "
            for k in range(0, j):
                if k == j - 1:
                    answer = answer + f"{L[i][k]} * {U[k][j]} = "
                else:
                    answer = answer + f"{L[i][k]} * {U[k][j]} + "
                sigma_sum += roundNumber(roundNumber(L[i][k], number_of_significant_figures) *
                                         roundNumber(U[k][j], number_of_significant_figures),
                                         number_of_significant_figures)
            L[i][j] = matrix[i][j] - sigma_sum
            answer = answer + str(sigma_sum)
            answer = answer + f"\nL{i}{j} = {matrix[i][j]} - {sigma_sum} = {L[i][j]}\n\n"
            L[i][j] = roundNumber(L[i][j], number_of_significant_figures)
        for j in range(i + 1, dimension):
            sigma_sum = 0
            answer = answer + f"U{i}{j} = ( A{i}{j} − \u03A3 L{i}k * Uk{j} ) / L{i}{i} where k is 0 :  {i - 1}\n\u03A3 = "
            for k in range(0, i):
                if k == i - 1:
                    answer = answer + f"{L[i][k]} * {U[k][j]} = "
                else:
                    answer = answer + f"{L[i][k]} * {U[k][j]} + "
                sigma_sum += roundNumber(roundNumber(L[i][k], number_of_significant_figures) *
                                         roundNumber(U[k][j], number_of_significant_figures),
                                         number_of_significant_figures)
            U[i][j] = roundNumber((matrix[i][j] - sigma_sum) / L[i][i], number_of_significant_figures)
            answer = answer + str(sigma_sum)
            answer = answer + f"\nU{i}{j} =( {matrix[i][j]} - {sigma_sum} ) / {L[i][i]} = {U[i][j]}\n\n"
            U[i][j] = roundNumber(U[i][j], number_of_significant_figures)

    answer = answer + "L Matrix :\n"
    answer = answer + print_Matrix(L)
    answer = answer + "\nU Matrix :\n"
    answer = answer + print_Matrix(U)

    return substitute(L, U, b, dimension, answer)


def roundNumber(number, number_of_significant_figures):
    if number == 0:
        return number
    else:
        return round(number, number_of_significant_figures - int(math.floor(math.log10(abs(number)))) - 1)


def print_Matrix(matrix):
    return ('\n'.join([''.join([formatting.format(str(item)) for item in row])
                       for row in matrix]))

# matrix_input = [[1, 2, 3],
#                 [2, 20, 26],
#                 [3, 26, 70]]
# b = [1, 2, 88]
# print(crout(matrix_input, b, 3, 3))
