def matrix_multiplication(X, Y):
    if len(X[0]) != len(Y):
        print("Kích thước của ma trận không phù hợp.")
        return None

    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result


# Ma trận X có kích thước MxN
X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ma trận Y có kích thước NxP
Y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = matrix_multiplication(X, Y)
if result_matrix:
    for row in result_matrix:
        print(row)
