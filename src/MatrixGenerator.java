import java.util.Random;

public class MatrixGenerator {
    public static double[][] generateRandomMatrix(int n) {
        Random random = new Random();
        double[][] matrix = new double[n][n]; // Matrice carrée n x n
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = -50 + (100) * random.nextDouble(); // Nombres entre -50 et 50
            }
        }
        return matrix;
    }
    public static double[] generateRandomVector(int n) {
        Random random = new Random();
        double[] vector = new double[n];
        for (int i = 0; i < n; i++) {
            vector[i] = -50 + (100) * random.nextDouble(); // Nombres entre -50 et 50
        }
        return vector;
    }

}
