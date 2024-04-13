from algorithmes import gauss_seidel, gaussian_elimination
import time
import numpy as np

# Tailles des matrices à générer
matrix_sizes = [100, 400, 500, 700, 1000, 1500, 2000]

# Fonction pour générer une matrice carrée aléatoire de taille n
def generate_random_matrix(n):
    # Génère une matrice n x n avec des valeurs flottantes aléatoires
     return np.random.uniform(-50, 50, (n, n))

# Génération des vecteurs b pour chaque matrice
def generate_random_vector(n):
    return np.random.uniform(-50, 50, n)

# Dictionnaire pour stocker les vecteurs b
vectors_b = {size: generate_random_vector(size) for size in matrix_sizes}


# Dictionnaire pour stocker les matrices générées
matrices = {}

# Génération des matrices pour chaque taille spécifiée
for size in matrix_sizes:
    matrices[size] = generate_random_matrix(size)


# Fonction pour mesurer le temps moyen d'exécution sur plusieurs essais
def measure_performance(method, A, b, trials=5):
    times = []
    for _ in range(trials):
        start_time = time.perf_counter()
        method(A, b)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

# Dictionnaires pour stocker les temps moyens pour chaque taille de matrice
times_gauss = {}
times_gauss_seidel = {}

# Mesure des performances pour chaque algorithme et taille de matrice
for size in matrix_sizes:
    A = matrices[size]
    b = vectors_b[size]
    times_gauss[size] = measure_performance(gaussian_elimination, A, b)
    times_gauss_seidel[size] = measure_performance(gauss_seidel, A, b, trials=5)

# Affichage des temps moyens pour vérification
for size in matrix_sizes:
    print(f"Taille {size}: Temps moyen Gauss = {times_gauss[size]:.5f}s, Temps moyen Gauss-Seidel = {times_gauss_seidel[size]:.5f}s")