import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

       double[][] A =  MatrixGenerator.generateRandomMatrix(100);
       double[] b = MatrixGenerator.generateRandomVector(100);
       GaussElimination.solve(A,b);
       double[] x0 = new double[100];
       GaussSeidelElimination.solve(A,b,x0,100,0.001);
    }
}