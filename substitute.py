import numpy


def substitute(L, U, b, n, output):
    # print(numpy.linalg.det(L))
    # print(numpy.linalg.det(U))

    y = [0.0] * n
    # forward sub
    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum = float(sum - (float(L[i][j] * y[j])))
        if(L[i][i]==0):
            return "division by zero!"
        y[i] = float(sum / L[i][i])
        output = output + "\ny :" + str(y) + "\n"
    # backward sub
    x = [0.0] * n
    if (U[n - 1][n - 1] == 0):
        return "division by zero!"
    x[n - 1] = float(y[n - 1] / U[n - 1][n - 1])
    output = output + "\n" + "Solution vector x at row " + str(n - 1) + " : " + str(x)

    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(sum + (float(U[i][j] * x[j])))
        if (U[i][i]==0):
            return "division by zero!"
        x[i] = float((float(float(y[i] - sum))) / U[i][i])
        output = output + "\n" + "Solution vector x at row " + str(i) + " : " + str(x)
    return output


# def check(n, matrix):
#     rank1 = n  # calculating coeffients matrix rank
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] != 0:
#                 break
#         else:
#             rank1 = rank1 - 1
#
#     rank2 = n  # calculating aug. matrix rank
#     for i in range(n):
#         for j in range(n + 1):
#             if matrix[i][j] != 0:
#                 break
#         else:
#             rank2 = rank2 - 1
#
#     if rank1 == rank2 == n:  # case1: unique solution
#         return ""
#     elif rank1 < rank2:  # cas2: no solution
#         return "\nsystem has no solution" + '\n'
#     else:  # case3: multisoltion
#         return "\nsystem has infinite solutions\n"
