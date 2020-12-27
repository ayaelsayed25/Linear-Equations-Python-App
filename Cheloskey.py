from array import array
import math


def cheloskeyDecomposition(a, b, n, precision):
    if not isSymmetric(a, n):
        return "Matrix should be symmetric, try again.."
    solution = "The matrix is symmetric; Chelosky applies."
    f = "{0:." + str(precision) + "g}"
    p = 1 - precision
    tolerance = float(f.format(0.5 * 10 ** p))
    L = [[0.0 for j in range(n)] for i in range(n)]
    x = [0.0 for i in range(n)]
    for k in range(n):
        for i in range(0, k):
            sum = 0.0
            for j in range(i):
                sum = float(f.format(sum + float(f.format(L[i][j] * L[k][j]))))
            L[k][i] = float(f.format(float(f.format(a[k][i] - sum)) / L[i][i]))
            solution = solution + "\n" + "L[" + str(k) + "][" + str(i) + "] = " + str(L[k][i])
        sum = 0.0
        for j in range(k):
            sum = float(f.format(sum + float(f.format(L[k][j] ** 2))))
        L[k][k] = float(f.format(math.sqrt(float(f.format(a[k][k] - sum)))))
        solution = solution + "\n" + "L[" + str(k) + "][" + str(k) + "] = " + str(L[k][k])
    return substituteCheloskey(L, b, n, f, x,solution)


def substituteCheloskey(L, b, n, f, x,solution):
    LT = [[0.0 for j in range(n)] for i in range(n)]
    LT = transpose(L, LT, n)
    y = [0.0] * n
    # forward sub
    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum = float(f.format(sum - (float(f.format(L[i][j] * y[j])))))
            print("Sum", sum)
        y[i] = float(f.format(sum / L[i][i]))
    # backward sub
    x[n - 1] = float(f.format(y[n - 1] / LT[n - 1][n - 1]))
    solution = solution + "\n" + "Solution vector x at row " + str(n - 1) + " : " + str(x)
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(f.format(sum + (float(f.format(LT[i][j] * x[j])))))
            print("sum", sum)
        x[i] = float(f.format((float(f.format(float(f.format(y[i] - sum)))) / LT[i][i])))
        solution = solution + "\n" + "Solution vector x at row " + str(i) + " : " + str(x)
    return solution


def transpose(a, tr, n):
    for i in range(n):
        for j in range(n):
            tr[i][j] = a[j][i]
    return tr
    # Returns true if mat[N][N] is symmetric, else false


def isSymmetric(a, n):
    tr = [[0.0 for j in range(n)] for i in range(n)]
    tr = transpose(a, tr, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] != tr[i][j]:
                return False
    return True

#
# n = int(input("Enter the number of rows: "))
# precision = int(input())
# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")
#
# for i in range(n):  # A for loop for row entries
#     a = array('f', [])
#     for j in range(n):  # A for loop for column entries
#         a.append(float(input()))
#     matrix.append(a)
# print("Enter b:")
# b = array('f', [])
# for i in range(n):
#     b.append(float(input()))
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j])
# x = cheloskeyDecomposition(matrix, b, n, precision)
# print(x)
