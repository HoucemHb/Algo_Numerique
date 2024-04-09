public class GaussElimination {
    public static void solve(double[][] matrix, double[] vector) {
        int n = vector.length;

        for (int pivot = 0; pivot < n; pivot++) {
            // Normaliser la ligne du pivot
            double pivotValue = matrix[pivot][pivot];
            for (int col = 0; col < n; col++) {
                matrix[pivot][col] /= pivotValue;
            }
            vector[pivot] /= pivotValue;

            // Éliminer les valeurs ci-dessous le pivot
            for (int row = pivot + 1; row < n; row++) {
                double factor = matrix[row][pivot];
                for (int col = 0; col < n; col++) {
                    matrix[row][col] -= factor * matrix[pivot][col];
                }
                vector[row] -= factor * vector[pivot];
            }
        }

        // Résolution récursive
        double[] solution = new double[n];
        for (int row = n - 1; row >= 0; row--) {
            double sum = vector[row];
            for (int col = row + 1; col < n; col++) {
                sum -= matrix[row][col] * solution[col];
            }
            solution[row] = sum;
        }

        // Affichage de la solution
        for (int i = 0; i < n; i++) {
            System.out.println("Variable " + (i + 1) + " = " + solution[i]);
        }
    }
}


