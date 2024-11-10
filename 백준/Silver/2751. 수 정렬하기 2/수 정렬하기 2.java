import java.util.*;
import java.io.*;


public class Main {

    static int N;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            pq.offer(Integer.parseInt(br.readLine()));
        }

        StringBuilder sb = new StringBuilder();
        
        while(!pq.isEmpty()){
            sb.append(pq.poll()+"\n");
        }

        System.out.println(sb.toString());
        
    }


}