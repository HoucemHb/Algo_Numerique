from algorithmes import gauss_seidel, gaussian_elimination
import time
import numpy as np

# Fonction pour générer une matrice carrée aléatoire de taille n
def generate_random_matrix(n):
    # Génère une matrice n x n avec des valeurs flottantes aléatoires
     return np.random.uniform(-50, 50, (n, n))


# Fonction pour générer une matrice carrée aléatoire à diagonale dominante de taille n
def generate_diagonally_dominant_matrix(n):
    A = np.random.uniform(-50, 50, (n, n))
    for i in range(n):
        # Set the diagonal element to a large enough value
        A[i, i] = np.sum(np.abs(A[i])) + np.random.uniform(1, 10)
    return A



# Génération des vecteurs b pour chaque matrice
def generate_random_vector(n):
    return np.random.uniform(-50, 50, n)


# Fonction pour mesurer le temps moyen d'exécution sur plusieurs essais
def measure_performance(method, A, b, trials=5):
    times = []
    for _ in range(trials):
        start_time = time.perf_counter()
        method(A, b)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)