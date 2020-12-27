# swaping rows if the pivot is zero
def swaprows(matrix_A, i, numberofequ):
    for s in range(i + 1, numberofequ):  # looping on the rest column elements
        if matrix_A[s][i] != 0:
            matrix_A[i], matrix_A[s] = matrix_A[s], matrix_A[i]
            break
    else:  # if all elements are zeros, pass this operation
        pass


# getting the greater element in column as a pivot
def pivoting(matrix, i, numberofequ):
    for s in range(i + 1, numberofequ):
        if matrix[s][i] > matrix[i][i]:
            matrix[i], matrix[s] = matrix[s], matrix[i]
    else:
        pass


# gauss elimimnation method
def gauss(matrix, numberofequ):
    for i in range(numberofequ):
        print(matrix)
        if matrix[i][i] == 0:  # sawping if pivot is zero
            swaprows(matrix, i, numberofequ)
        if matrix[i][i] != 0:  # case1: nonzero pivot
            for j in range(i + 1, numberofequ):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(numberofequ + 1):
                    matrix[j][k] = matrix[j][k] - factor * matrix[i][k]

        else:  # case2: zero pivot then shiftting to following column
            for j in range(i + 1, numberofequ):
                factor = matrix[j][j] / matrix[i][j]
                for k in range(numberofequ + 1):
                    matrix[j][k] = matrix[j][k] - factor * matrix[i][k]

    solvable(matrix, numberofequ)  # determine solution type


# gauss elimination with pivoting method
def gausswithpivoting(matrix, numberofequ):
    for i in range(numberofequ):
        print(matrix)
        pivoting(matrix, i, numberofequ)  # pivoting in each new row
        if matrix[i][i] != 0:  # case1: nonzero pivot
            for j in range(i + 1, numberofequ):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(numberofequ + 1):
                    matrix[j][k] = matrix[j][k] - factor * matrix[i][k]
        else:  # case2: zero pivot then shiftting to following column
            for j in range(i + 1, numberofequ):
                factor = matrix[j][j] / matrix[i][j]
                for k in range(numberofequ + 1):
                    matrix[j][k] = matrix[j][k] - factor * matrix[i][k]

    solvable(matrix, numberofequ)  # determine solution type


# gauss jorgan elimination method
def jordanelimination(matrix, numberofequ):
    for i in range(numberofequ):
        print(matrix)
        if matrix[i][i] == 0:
            swaprows(matrix, i, numberofequ)  # sawping if pivot is zero
        if matrix[i][i] != 0:
            for j in range(numberofequ):
                if i != j:
                    factor = matrix[j][i] / matrix[i][i]
                    for k in range(numberofequ + 1):
                        matrix[j][k] = matrix[j][k] - factor * matrix[i][k]

    for i in range(numberofequ):  # dividing rows by pivot
        if matrix[i][i] != 0:
            temp = matrix[i][i]
            for k in range(numberofequ + 1):
                matrix[i][k] = matrix[i][k] / temp
    print(matrix)  # printing eliminated matrix
    solvable(matrix, numberofequ)  # determine solution type


# determining solution type
def solvable(matrix, numberofequ):
    rank1 = numberofequ  # calculating coeffients matrix rank
    for i in range(numberofequ):
        for j in range(numberofequ):
            if matrix[i][j] != 0:
                break
        else:
            rank1 = rank1 - 1

    rank2 = numberofequ  # calculating aug. matrix rank
    for i in range(numberofequ):
        for j in range(numberofequ + 1):
            if matrix[i][j] != 0:
                break
        else:
            rank2 = rank2 - 1

    if rank1 == rank2 == numberofequ:  # case1: unique solution
        results = subistitution(matrix, numberofequ)
        print('solution =', results, '\n')
    elif rank1 < rank2:  # cas2: no solution
        print("system has no solution", '\n')
    else:  # case3: multisoltion
        results = multisolution(matrix, numberofequ, rank1)
        print('solution =', results, '\n')


# case1: unique solution system
def subistitution(matrix_A, numberofequ):
    x = ["null"] * numberofequ  # declaring solution vector
    x[numberofequ - 1] = matrix_A[numberofequ - 1][numberofequ] / matrix_A[numberofequ - 1][
        numberofequ - 1]  # getting X(n)
    for i in range(numberofequ - 2, -1, -1):  # getting the rest of xs
        x[i] = matrix_A[i][numberofequ]
        for j in range(i + 1, numberofequ):
            x[i] = x[i] - matrix_A[i][j] * x[j]
        x[i] = x[i] / matrix_A[i][i]
    return x


# case2: multisolution system
def multisolution(matrix, numberofequ, rank):
    x = ["null"] * numberofequ  # declaring solution vector
    freevariable = numberofequ - rank
    for i in range(numberofequ):  # determine free variables
        for j in range(numberofequ + 1):
            if matrix[i][j] != 0:
                break
        else:
            x[i] = "free variable x" + str(i)
            del matrix[i]

    for i in range(rank - 1, -1, -1):  # loopinb on nonzero rows
        x[i] = matrix[i][numberofequ]
        for j in range(i + 1, numberofequ):
            if type(x[j]) == str:  # case: nonfree variable is function of freevariable
                x[i] = str(x[i]) + "-" + str(matrix[i][j]) + '*' + x[j]
            else:  # case: nonfree variable isnot function of freevariable
                x[i] = x[i] - matrix[i][j] * x[j]
        if type(x[i]) == str:
            x[i] = '(' + x[i] + ')/' + str(matrix[i][i])
        else:
            x[i] = x[i] / matrix[i][i]
    return x


# s = 3
# matrix = [[2, 3, 4, 1], [1, 0, 3, 1.5], [4, 5, 2, 2]]
# matrix1 = [[2, 0, 4, 1], [1, 0, 3, 1.5], [4, -0, 2, 2]]
# matrix2 = [[2, 3, 5], [4, 6, 10]]
# gauss(matrix, s)
# gauss(matrix1, s)
# gauss(matrix2, 2)
#
# s = 3
# matrix = [[2, 3, 4, 1], [1, 0, 3, 1.5], [4, 5, 2, 2]]
# matrix1 = [[2, 0, 4, 1], [1, 0, 3, 1.5], [4, -0, 2, 2]]
# matrix2 = [[2, 3, 5], [4, 6, 10]]
# gausswithpivoting(matrix, s)
# gausswithpivoting(matrix1, s)
# gausswithpivoting(matrix2, 2)
#
# s = 3
# matrix = [[2, 3, 4, 1], [1, 0, 3, 1.5], [4, 5, 2, 2]]
# matrix1 = [[2, 0, 4, 1], [1, 0, 3, 1.5], [4, -0, 2, 2]]
# matrix2 = [[2, 3, 5], [4, 6, 10]]
# jordanelimination(matrix, s)
# jordanelimination(matrix1, s)
# jordanelimination(matrix2, 2)
