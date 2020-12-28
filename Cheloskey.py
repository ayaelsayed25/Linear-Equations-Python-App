padding = 20
formatting = '{:' + str(padding) + '}'
from array import array
import math
def cheloskeyDecomposition(a, b, n, precision):
    if isSymmetric(a,n) == False:
        return "Matrix should be symmetric, try again.."
    solution = "The matrix is symmetric; Chelosky applies."
    f = "{0:." + str(precision) + "g}"
    p = 1 - precision
    tolerance = float(f.format(0.5 * 10 ** p))
    scalingFactors = [0.0 for i in range(n)]
    index = [0] * n
    L = [[0.0 for j in range(n)] for i in range(n)]
    x = [0.0 for i in range(n)]
    for i in range(0, n): #scaling factors and index array :
        index[i] = i
        scalingFactors[i] = float(f.format(abs(a[i][0])))
        for j in range(1, n):
            if abs(a[i][j]) > scalingFactors[i]:
                scalingFactors[i] = float(f.format(abs(a[i][j])))
    for k in range (n):
        index = pivot(a, index, scalingFactors, n, k, f) #performing pivoting
        if float(f.format(abs(a[index[k]][k]) / scalingFactors[index[k]])) < tolerance:
            solution = solution + "/n" + "The System is inconsistent"
            return solution
        for i in range(0, k):
            sum = 0.0
            for j in range(i):
                sum = float(f.format(sum + float(f.format(L[index[i]][j] * L[index[k]][j]))))
            L[index[k]][i] = float(f.format(float(f.format(a[index[k]][i] - sum)) / L[index[i]][i]))
            solution = solution + "/n" + "L[" + str(index[k]) + "]["+ str(i)+ "] = " +  str(L[index[k]][i])
        sum = 0.0
        for j in range(k):
            sum = float(f.format(sum + float(f.format(L[index[k]][j] ** 2))))
        if float(f.format(a[index[k]][k] - sum)) < 0 :
            solution = solution + "/n" + "The system cannot be solved by Chelosky method!"
            return solution
        L[index[k]][k] = float(f.format(math.sqrt(float(f.format(a[index[k]][k] - sum)))))
        solution = solution + "/n" + "L[" + str(index[k]) + "][" + str(k) + "] = " + str(L[index[k]][k])
    if float(f.format(abs(a[index[n-1]][n-1]) / scalingFactors[index[n-1]])) < tolerance:
        solution = solution + "/n" + "The System is inconsistent"
        return solution
    return substituteCheloskey(L, b, n, f, x, solution)

def substituteCheloskey(L, b, n, f, x, solution):
    print_Matrix(L,"L")
    LT = [[0.0 for j in range(n)] for i in range(n)]
    LT = transpose(L, LT, n)
    print_Matrix(LT, "U")
    y =[0.0]*n
    #forward sub
    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum =float(f.format(sum - (float(f.format(L[i][j] * y[j])))))
        y[i] = float(f.format(sum / L[i][i]))
    #backward sub
    x[n - 1] = float(f.format(y[n-1] / LT[n-1][n-1]))
    solution = solution + "/n" + "Solution vector x at row " + str(n-1) + " : " + str(x)
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(f.format(sum + (float(f.format(LT[i][j] * x[j])))))
            print("sum", sum)
        x[i] = float(f.format((float(f.format(float(f.format(y[i] - sum)))) / LT[i][i])))
        solution = solution + "/n" + "Solution vector x at row " + str(i) + " : " + str(x)
    return solution


def pivot(a, index, scalingFactors, n, k, f):
    p = k
    big =float(f.format(abs(a[index[k]][k]) / scalingFactors[index[k]]))
    for i in range(k+1, n):
        dummy =float(f.format(abs(a[index[i]][k] / scalingFactors[index[i]])))
        if(dummy > big):
            big = dummy
            p = i
    dummy = index[p]
    index[p] = index[k]
    index[k] = dummy
    return index

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
            if (a[i][j] != tr[i][j]):
                return False
    return True

def print_Matrix(matrix, matrix_name):
    return f'\n{matrix_name} :\n' + '\n'.join([''.join([formatting.format(str(item)) for item in row])
                                               for row in matrix])


