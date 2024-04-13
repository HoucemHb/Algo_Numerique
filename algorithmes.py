import numpy as np
def gaussian_elimination(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    # Phase d'élimination
    for i in range(n):
        # Pivotage partiel pour améliorer la stabilité numérique
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i+1:] = A[j, i+1:] - factor * A[i, i+1:]
            b[j] = b[j] - factor * b[i]

    # Substitution arrière
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = np.zeros(n)
    x_new = np.copy(x)
    for iteration in range(max_iterations):
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        x = np.copy(x_new)
    return x

