import numpy as np
def gaussian_elimination(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    # Phase d'élimination
    for k in range(n):
        # Pivotage partiel pour améliorer la stabilité numérique
        max_row = np.argmax(np.abs(A[k:n, k])) + k
        A[[k, max_row]] = A[[max_row, k]]
        b[[k, max_row]] = b[[max_row, k]]

        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k+1:] = A[i, k+1:] - factor * A[k, k+1:]
            b[i] = b[i] - factor * b[k]

    # Remontée
    x = np.zeros(n)
    x[n-1]=b[n-1]/A[n-1,n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = np.zeros(n)
    # x_new = np.copy(x)
    for k in range(max_iterations):
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x - x, ord=np.inf) < tolerance:
            return x
    return x

