public class GaussSeidelElimination {
    public static void solve(double[][] matrix, double[] vector, double[] initialGuess, int maxIterations, double tolerance) {
        int n = vector.length;
        double[] previous = new double[n];
        System.arraycopy(initialGuess, 0, previous, 0, n);

        for (int iteration = 0; iteration < maxIterations; iteration++) {
            for (int i = 0; i < n; i++) {
                double sum = vector[i];
                for (int j = 0; j < n; j++) {
                    if (i != j) {
                        sum -= matrix[i][j] * previous[j];
                    }
                }
                previous[i] = 1/matrix[i][i] * sum;
            }

            // Vérification de la convergence
            boolean converged = true;
            for (int i = 0; i < n && converged; i++) {
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += matrix[i][j] * previous[j];
                }
                if (Math.abs(sum - vector[i]) > tolerance) {
                    converged = false;
                }
            }
            if (converged) {
                break;
            }
        }

        // Affichage de la solution
        for (int i = 0; i < n; i++) {
            System.out.println("Variable " + (i + 1) + " = " + previous[i]);
        }
    }
}


