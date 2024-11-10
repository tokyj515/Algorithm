import java.util.*;
import java.io.*;


public class Main {

    static int N, M;
    static int[][] matrix1, matrix2;



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());


        matrix1 = new int[N][M];
        matrix2 = new int[N][M];

        for(int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());

            for(int j=0; j<M; j++){
                matrix1[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());

            for(int j=0; j<M; j++){
                matrix2[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i<N; i++){
            for(int j=0; j<M; j++){
                matrix1[i][j] += matrix2[i][j];
            }
        }


        StringBuilder sb = new StringBuilder();

        for(int i = 0; i<N; i++){
            for(int j=0; j<M; j++){
                sb.append(matrix1[i][j] + " ");
            }
            sb.append("\n");
        }


        System.out.println(sb.toString());


    }


}