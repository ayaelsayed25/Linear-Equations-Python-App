def substitute(L, U, b, n, f, output):
    y = [0.0] * n
    # forward sub
    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum = float(sum - (float(L[i][j] * y[j])))
            output = output + "\nSum =" + str(sum)+"\n"
        y[i] = float(sum / L[i][i])
        output = output + "\ny after " + str(y)+"\n"
    # backward sub
    x = [0.0] * n
    x[n - 1] = float(y[n - 1] / U[n - 1][n - 1])
    output = output + "x" + str(x)
    for i in range(n - 2, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum = float(sum + (float(U[i][j] * x[j])))
            output = output + "\nsum =" + str(sum)+"\n"
        x[i] = float((float(float(y[i] - sum))) / U[i][i])
        output = output + "x" + str(x)
    return output
