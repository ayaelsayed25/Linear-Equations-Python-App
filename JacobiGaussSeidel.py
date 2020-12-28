import math
import numpy as np

b_input = [5, 2, 3]
x_input = [1, 1, 1]
iterations = []
data = []
matrix_input = [[1, 2, 3],
                [2, 4, 5],
                [3, 4, 2]]
result = []
nOfSignificantBits = 3


# Method used to calculate sum of matrix's raw
def raw_sum(raw):
    summation = 0
    for i in range(len(raw)):
        summation = raw[i] + summation
    return summation


# Method used to determine whether matrix is diagonally dominant or not
def diagonally_dominant(matrix, n):
    if matrix[0][0] > raw_sum(matrix[0]):
        for i in range(n - 1):
            if matrix[i + 1][i + 1] < raw_sum(matrix[i + 1]):
                return False
        return True
    else:
        return False


def d_matrix(matrix, n):
    d = [0, 0, 0]
    for i in range(n):
        if matrix[i][i] == 0 :
          return False, 0
        d[i] = matrix[i][i]
        matrix[i][i] = 0
    return d, matrix


# Method used to copy matrix
def matrix_equality(matrix1, matrix2):
    for i in range(len(matrix1)):
        matrix1[i] = matrix2[i]
    return matrix1, matrix2


def gauss_seidel(n: int, n_iterations: int, matrix: list, b: list, initial_x: list, n_sig_fig: int):
    # Check convergence
    converges = diagonally_dominant(matrix, n)
    output = ""
    if converges:
        output = output + "Matrix is diagonally dominant , Solution must converge \n"
    new_x = []
    for i in range(n):
        new_x.append(0)
    d, matrix = d_matrix(matrix, n)
    if d == False:
        output = output + "Diagonal Elements Can't Be Zero!"
        return output
    for i in range(n_iterations):
        # Printing Steps
        output = output + "Iteration " + str(i + 1) + " :\n"
        output = output + "steps : \n"
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]
            if new_x[j] != 0:
                new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
                nan = np.isnan(new_x[j])
                infinity = np.isinf(new_x[j])
                if nan or infinity:
                    output = output + "Can't reach this number of iterations \n"
                    return test(output, i - 1,n)
                if new_x[j] != 0:
                    new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
                    initial_x[j] = new_x[j]
            # Steps formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(initial_x[j])
            output = output + new + "\n"
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)
    return test(output, n_iterations,n)


def maximum_error(initial_x, new_x):
    maximum = -1
    for i in range(len(initial_x)):
        if new_x[i] == 0:
            error = 100
        else:
            error = abs((new_x[i] - initial_x[i]) / new_x[i]) * 100
        if error > maximum:
            maximum = error
    return maximum


def gauss_seidel_absolute_error(n: int, error: float, matrix: list, b: list, initial_x: list, n_sig_fig: int):
    output = ""
    # Check convergence
    converges = diagonally_dominant(matrix, n)
    if converges:
        output = output + "Matrix is diagonally dominant , Solution must converge \n"
    last_x = []
    new_x = []
    for i in range(n):
        new_x.append(0)
        last_x.append(0)
    last_x, initial_x = matrix_equality(last_x, initial_x)
    d, matrix = d_matrix(matrix, n)
    if d == False:
        output = output + "Diagonal Elements Can't Be Zero!"
        return output
    i = 0
    while True:
        # Printing Steps
        output = output + "Iteration " + str(i + 1) + " :\n"
        output = output + "steps : \n"
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]
            if new_x[j] != 0:
                new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
                nan = np.isnan(new_x[j])
                infinity = np.isinf(new_x[j])
                if nan or infinity:
                    output = output + "Can't reach this relative error \n"
                    return test(output, i - 1,n)
                if new_x[j] != 0:
                    new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            initial_x[j] = new_x[j]
            # Steps formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(initial_x[j])
            output = output + new + "\n"
        absolute_error = maximum_error(last_x, new_x)
        last_x, new_x = matrix_equality(last_x, new_x)
        nan = any(np.isnan(new_x[:]))
        infinity = any(np.isinf(new_x[:]))
        if nan or infinity:
            output = output + "It can't reach this absolute relative error \n"
            return test(output, i,n)
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)
        i = i + 1
        if absolute_error <= error:
            break
    return test(output, i,n)


def jacobi(n: int, n_iterations: int, matrix: list, b: list, initial_x: list, n_sig_fig: int):
    new_x = []
    for i in range(n):
        new_x.append(0)

    d, matrix = d_matrix(matrix, n)
    output = ""
    if d == False:
        output = output + "Diagonal Elements Can't Be Zero!"
        return output
    for i in range(n_iterations):
        # Printing Steps
        output = output + "Iteration " + str(i + 1) + " :\n"
        output = output + "steps : \n"
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]
            if new_x[j] != 0:
                new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
                nan = np.isnan(new_x[j])
                infinity = np.isinf(new_x[j])
                if nan or infinity:
                    output = output + "Can't reach this number of iterations \n"
                    return test(output, i - 1,n)
                if new_x[j] != 0:
                    new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            # Steps Formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(new_x[j])
            output = output + new + "\n"
        initial_x, new_x = matrix_equality(initial_x, new_x)
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)
    return test(output, n_iterations,n)


def jacobi_absolute_error(n: int, error: float, matrix: list, b: list, initial_x: list, n_sig_fig: int):
    new_x = []
    for i in range(n):
        new_x.append(0)
    d, matrix = d_matrix(matrix, n)
    if d == False:
        output = "Diagonal Elements Can't Be Zero!"
        return output
    i = 0
    while True:
        # Printing Steps
        output = "Iteration " + str(i + 1) + " :\n"
        output = output + "steps : \n"
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]
            if new_x[j] != 0:
                new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
                nan = np.isnan(new_x[j])
                infinity = np.isinf(new_x[j])
                if nan or infinity:
                    output = output + "Can't reach this relative error \n"
                    return test(output, i - 1,n)
                if new_x[j] != 0:
                    new_x[j] = round(new_x[j], n_sig_fig - int(math.floor(math.log10(abs(new_x[j])))) - 1)
            # Steps Formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(new_x[j])
            output = output + new + "\n"
        initial_x, new_x = matrix_equality(initial_x, new_x)
        absolute_error = maximum_error(initial_x, new_x)
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)
        i = i + 1
        if absolute_error <= error:
            break
    return test(output, i,n)


# Method Used for Output Table's data creation
def string_format(n, n_iterations):
    for i in range(n_iterations):
        iterations.append("iteration " + str(i + 1))
    for i in range(n):
        data.append("X" + str(i))


# Method to formal resultant Table
def show_result(n_iterations: int, n: int, output: str):
    string_format(n, n_iterations)
    result_matrix = np.reshape(result, (n_iterations, n))
    row_format = "{:>30}" * (len(data) + 1)
    output = output + row_format.format("", *data) + "\n"
    for iteration, row in zip(iterations, result_matrix):
        output = output + row_format.format(iteration, *row) + "\n"
    return output


def test(output, nOfIterations,dimesion):
    global result
    result = result[0:dimesion * nOfIterations]
    return show_result(nOfIterations, dimesion, output)
