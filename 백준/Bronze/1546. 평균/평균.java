import java.util.*;
import java.io.*;


public class Main {

    static ArrayList<Integer> score = new ArrayList<>();
    static int N;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<N; i++){
            score.add(Integer.parseInt(st.nextToken()));
        }


        int maxVal = Collections.max(score);
        double avg = 0;
        for(int i=0; i<N; i++){
            avg += (double)score.get(i)/maxVal*100;
        }

        avg /= N;

//        System.out.printf("%.2f\n",avg);
        System.out.println(avg);


    }


}