
import java.util.*;
import java.io.*;


public class Main {

    static boolean[] visited;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        visited = new boolean[31];

        for(int i=0; i<28; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            visited[Integer.parseInt(st.nextToken())] = true;
        }


        for(int i= 1; i<=30; i++){
            if(!visited[i]){
                System.out.println(i);
            }
        }

    }


}