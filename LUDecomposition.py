def downLittleDecomposition(a, b, n, precision):
    solution = ""
    scalingFactors = [0.0 for i in range(n)]
    index = [0] * n
    f = "{0:." + str(precision) + "g}"
    p = 1 - precision
    tolerance = float(f.format(0.5 * 10 ** p))
    x = [0.0 for i in range(n)]  # array of solution
    print("tolerance = ", tolerance)
    # get scaling factors and indecies
    for i in range(0, n):
        index[i] = i
        scalingFactors[i] = float(f.format(abs(a[i][0])))
        for j in range(1, n):
            if abs(a[i][j]) > scalingFactors[i]:
                scalingFactors[i] = float(f.format(abs(a[i][j])))
    solution = solution + "\n" + "Vector of scalars : " + str(scalingFactors)
    solution = solution + "\n" + "Vector on indices before pivoting : " + str(index)
    # perform pivoting on a then decompose :
    for k in range(0, n - 1):
        index = pivot(a, index, scalingFactors, n, k, f)
        solution = solution + "\n" + "Vector of indices after pivoting at column " + str(k) + " : " + str(index)
        if float(f.format(abs(a[index[k]][k]) / scalingFactors[index[k]])) < tolerance:
            solution = solution + "\n" + "The System is inconsistent"
            return solution
        for i in range(k + 1, n):
            factor = float(f.format(a[index[i]][k] / a[index[k]][k]))
            solution = solution + "\n" + "factor at row " + str(i) + " : " + str(factor)
            a[index[i]][k] = float(f.format(factor))
            solution = solution + "\n" + "Matrix A[ " + str(index[i]) + " ][ " + str(k) + " ] = " + str(a[index[i]][k])
            for j in range(k + 1, n):
                a[index[i]][j] = float(f.format(a[index[i]][j] - float(f.format(factor * a[index[k]][j]))))
                solution = solution + "\n" + "Matrix A[ " + str(index[i]) + " ][ " + str(j) + " ] = " + str(
                    a[index[i]][j])

    if float(f.format(abs(a[index[n - 1]][n - 1]) / scalingFactors[index[n - 1]])) < tolerance:
        solution = solution + "\n" + "The System is inconsistent"
        return solution
    print(a)
    return substitute(a, index, n, b, x, f,solution)



def pivot(a, index, scalingFactors, n, k, f):
    p = k
    big = float(f.format(abs(a[index[k]][k]) / scalingFactors[index[k]]))
    for i in range(k + 1, n):
        dummy = float(f.format(abs(a[index[i]][k] / scalingFactors[index[i]])))
        if dummy > big:
            big = dummy
            p = i
    dummy = index[p]
    index[p] = index[k]
    index[k] = dummy
    return index


def substitute(a, index, n, b, x, f,solution):
    # forward sub
    y = [0.0] * n
    y[index[0]] = b[index[0]]
    print("y before ", y)
    for i in range(1, n):
        sum = b[index[i]]
        for j in range(0, i):
            sum = float(f.format(sum - (float(f.format(a[index[i]][j] * y[index[j]])))))
            print("Sum", sum)
        y[index[i]] = sum
    # backward sub
    x[n - 1] = float(f.format(y[index[n - 1]] / a[index[n - 1]][n - 1]))
    solution = solution + "\n" + "Solution vector x at row " + str(n - 1) + " : " + str(x)
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(f.format(sum + (float(f.format(a[index[i]][j] * x[j])))))
            print("sum", sum)
        x[i] = float(f.format((float(f.format(float(f.format(y[index[i]] - sum)))) / a[index[i]][i])))
        solution = solution + "\n" + "Solution vector x at row " + str(i) + " : " + str(x)
    return solution

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
# x = downLittleDecomposition(matrix, b, n, precision);
# print(x)
