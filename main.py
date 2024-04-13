from algorithmes import gauss_seidel, gaussian_elimination
import time
import numpy as np

# Tailles des matrices à générer
matrix_sizes = [100, 400, 500, 700, 1000, 1500, 2000]

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

# Dictionnaire pour stocker les vecteurs b
vectors_b = {size: generate_random_vector(size) for size in matrix_sizes}


# Dictionnaire pour stocker les matrices générées
matrices = {}

# Génération des matrices pour chaque taille spécifiée
for size in matrix_sizes:
    matrices[size] = generate_diagonally_dominant_matrix(size)


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

print('calculating .. ')
# Mesure des performances pour chaque algorithme et taille de matrice
for size in matrix_sizes:
    A = matrices[size]
    b = vectors_b[size]
    times_gauss[size] = measure_performance(gaussian_elimination, A, b)
    times_gauss_seidel[size] = measure_performance(gauss_seidel, A, b, trials=5)

# Affichage des temps moyens pour vérification
for size in matrix_sizes:
    print(f"Taille {size}: Temps moyen Gauss = {times_gauss[size]:.5f}s, Temps moyen Gauss-Seidel = {times_gauss_seidel[size]:.5f}s")

import pandas as pd
import matplotlib.pyplot as plt

# Création d'un DataFrame pour les données
data = {
    "Matrix Size": matrix_sizes,
    "Gauss Time (s)": [times_gauss[size] for size in matrix_sizes],
    "Gauss-Seidel Time (s)": [times_gauss_seidel[size] for size in matrix_sizes]
}
df = pd.DataFrame(data)

# Affichage du DataFrame
print(df)



# Tracé des graphiques
plt.figure(figsize=(12, 8))
plt.plot(df["Matrix Size"], df["Gauss Time (s)"], 'b-o', label="Gauss")
plt.plot(df["Matrix Size"], df["Gauss-Seidel Time (s)"], 'r-o', label="Gauss-Seidel")
plt.plot(df["Matrix Size"], df['Gauss Time (s)'].ewm(span=2).mean(), 'b-', lw=2, label="Gauss Smoothed")
plt.plot(df["Matrix Size"], df['Gauss-Seidel Time (s)'].ewm(span=2).mean(), 'r-', lw=2, label="Gauss-Seidel Smoothed")

plt.title("Comparison of Execution Times for Gaussian and Gauss-Seidel Methods")
plt.xlabel("Matrix Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()



