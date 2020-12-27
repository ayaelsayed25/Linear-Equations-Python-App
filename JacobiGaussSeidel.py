import numpy as np

size = 3
numberOfIterations = 4
b_input = [5, 2, 3]
x_input = [1, 1, 1]
iterations = []
data = []
matrix_input = [[1, 2, 3],
                [2, 4, 5],
                [3, 4, 2]]
result = []


# Method Used for Output Table's data creation
def string_format(n, n_iterations):
    for i in range(n_iterations):
        iterations.append("iteration " + str(i + 1))
    for i in range(n):
        data.append("X" + str(i))


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
        d[i] = matrix[i][i]
        matrix[i][i] = 0
    return d, matrix


# Method used to copy matrix
def matrix_equality(matrix1, matrix2):
    for i in range(len(matrix1)):
        matrix1[i] = matrix2[i]
    return matrix1, matrix2


def gauss_seidel(n: int, n_iterations: int, matrix: list, b: list, initial_x: list):
    # Check convergence
    converges = diagonally_dominant(matrix, n)
    if converges:
        print("Matrix is diagonally dominant , Solution must converge ")
    new_x = [0, 0, 0]
    string_format(n, n_iterations)
    d, matrix = d_matrix(matrix, n)

    for i in range(n_iterations):
        # Printing Steps
        print("Iteration " + str(i + 1) + " :")
        print("steps : ")
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]

            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
            initial_x[j] = new_x[j]
            # Steps formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(initial_x[j])
            print(new)
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)


def jacobi(n: int, n_iterations: int, matrix: list, b: list, initial_x: list):
    new_x = [0, 0, 0]
    d, matrix = d_matrix(matrix, n)
    string_format(n, n_iterations)

    for i in range(n_iterations):
        # Printing Steps
        print("Iteration " + str(i + 1) + " :")
        print("steps : ")
        for j in range(n):
            new = "X" + str(j) + " = 1/" + str(d[j]) + " [ "
            new_x[j] = b[j] / d[j]
            for k in range(n):
                new = new + str(matrix[j][k]) + "*" + str(initial_x[k]) + " - "
                new_x[j] = new_x[j] - matrix[j][k] * initial_x[k] / d[j]
            # Steps Formatting
            new = new[0:len(new) - 2]
            new = new + "] = " + str(new_x[j])
            print(new)
        initial_x, new_x = matrix_equality(initial_x, new_x)
        # Adding results of each iteration
        for item in initial_x:
            result.append(item)


# Method to formal resultant Table
def show_result(n_iterations: int, n: int):
    result_matrix = np.reshape(result, (n_iterations, n))
    row_format = "{:>15}" * (len(data) + 1)
    print(row_format.format("", *data))
    for iteration, row in zip(iterations, result_matrix):
        print(row_format.format(iteration, *row))


gauss_seidel(size, numberOfIterations, matrix_input, b_input, x_input)
show_result(numberOfIterations, size)
