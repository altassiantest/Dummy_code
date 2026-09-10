def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def multiply_matrices(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == '__main__':
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print('Add:', add_matrices(a, b))
    print('Transpose:', transpose(a))
    print('Multiply:', multiply_matrices(a, b))
