import java.util.*;
import java.io.*;


public class Main {

    static int N, S;
    static int[] num;
    static boolean[] visited;

    static ArrayList<Integer> answer = new ArrayList<>();

    static int result = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        num = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i =0; i<N; i++){
            num[i] = Integer.parseInt(st.nextToken());
        }


        for(int len = 1; len<= N; len++){
            visited = new boolean[N];
            backtrack(0, 0, len);
        }


        System.out.println(result);

    }


    static void backtrack(int dep, int pre, int len){
        if(dep == len){
            ArrayList<Integer> temp = new ArrayList<>(answer);

            int sum = 0;
            for(Integer i: temp){
                sum += i;
            }

            if(sum == S){
//                System.out.println(temp);
                result++;
            }
            return;
        }

        for(int i = pre; i<N; i++){
            if(!visited[i]){
                answer.add(num[i]);
                visited[i] = true;

                backtrack(dep+1, i+1, len);

                answer.remove(answer.size()-1);
                visited[i] = false;
            }
        }


    }


}