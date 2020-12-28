padding = 20
formatting = '{:' + str(padding) + '}'
import math
from array import array


def downLittleDecomposition(a, b, n, precision):
    solution = ""
    scalingFactors = [0.0 for i in range(n)]
    index = [0] * n
    f = "{0:." + str(precision) + "g}"
    p = 1 - precision
    tolerance = float(f.format(0.5 * 10**p))
    x = [0.0 for i in range(n)] #array of solution
    print("tolerance = ", tolerance)
    #get scaling factors and indecies
    for i in range(0, n):
        index[i] = i
        scalingFactors[i] = float(f.format(abs(a[i][0])))
        for j in range(1, n):
            if abs(a[i][j]) > scalingFactors[i]:
                scalingFactors[i] = float(f.format(abs(a[i][j])))
    solution = solution + "/n" + "Vector of scalars : " + str(scalingFactors)
    solution =solution + "/n" + "Vector on indices before pivoting : " + str(index)
    #perform pivoting on a then decompose :
    for k in range(0, n-1):
        index = pivot(a, index, scalingFactors, n, k, f)
        solution = solution + "/n" + "Vector of indices after pivoting at column " + str(k) + " : " + str(index)
        if float(f.format(abs(a[index[k]][k]) / scalingFactors[index[k]])) < tolerance:
            solution = solution + "/n" + "The System is inconsistent"
            return solution
        for i in range(k+1, n):
            factor = float(f.format(a[index[i]][k] / a[index[k]][k]))
            solution = solution + "/n" + "factor at row " + str(i) + " : " + str(factor)
            a[index[i]][k] = float(f.format(factor))
            solution = solution + "/n" + "Matrix A[ " + str(index[i]) + " ][ " + str(k) +" ] = " +  str(a[index[i]][k])
            for j in range(k+1, n):
                a[index[i]][j] = float(f.format(a[index[i]][j] - float(f.format(factor*a[index[k]][j]))))
                solution = solution + "/n" + "Matrix A[ " + str(index[i]) + " ][ " + str(j) + " ] = " + str(a[index[i]][j])

    if float(f.format(abs(a[index[n-1]][n-1]) / scalingFactors[index[n-1]])) < tolerance:
        solution = solution + "/n" + "The System is inconsistent"
        return solution
    return substitute(a, index, n, b, x, f , solution)



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

def substitute(a, index, n, b, x, f, solution):
    #forward sub
    solution = ""
    y =[0.0]*n
    y[index[0]] = b[index[0]]
    print("y before ",y)
    for i in range(1, n):
        sum = b[index[i]]
        for j in range(0, i):
            sum =float(f.format(sum - (float(f.format(a[index[i]][j] * y[index[j]])))))
            print("Sum", sum)
        y[index[i]] = sum
    #backward sub
    x[n-1] = float(f.format(y[index[n-1]] / a[index[n-1]][n-1]))
    solution = solution + "/n" + "Solution vector x at row " + str(n-1) + " : " + str(x)
    for i in range(n-2, -1, -1):
        sum = 0.0
        for j in range(i+1, n):
            sum = float(f.format(sum + (float(f.format(a[index[i]][j] * x[j])))))
            print("sum", sum)
        x[i] = float(f.format((float(f.format( float(f.format(y[index[i]] - sum ))))/ a[index[i]][i])))
        solution = solution + "/n" + "Solution vector x at row " + str(i) + " : " + str(x)
    L = [[0.0 for j in range(n)] for i in range(n)]
    U = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            L[i][j] = a[i][j]
        L[i][i] = 1
    print_Matrix(L, "L")
    for i in range(n):
        for j in range(i, n):
            U[i][j] = a[i][j]
    print_Matrix(U, "U")
    return solution

def print_Matrix(matrix, matrix_name):
    return f'\n{matrix_name} :\n' + '\n'.join([''.join([formatting.format(str(item)) for item in row])
                                               for row in matrix])



