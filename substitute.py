def substitute(L, U, b, n, f):
    y = [0.0] * n
    # forward sub
    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum = float(sum - (float(L[i][j] * y[j])))
            print("Sum", sum)
        y[i] = float(sum / L[i][i])
        print("y after ", y)
    # backward sub
    x = [0.0] * n
    x[n - 1] = float(y[n - 1] / U[n - 1][n - 1])
    print("x", x)
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(sum + (float(U[i][j] * x[j])))
            print("sum", sum)
        x[i] = float((float(float(y[i] - sum))) / U[i][i])
        print("x", x)
    return x
