import java.util.*;
import java.io.*;


public class Main {

//    static Deque<String> stack = new ArrayDeque<>();
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i<N; i++){
            String s = br.readLine();
            int cnt = 0;
            boolean possible = true;

            for(int j=0; j<s.length(); j++){

                if(s.charAt(j) == '('){
                    cnt ++;
                } else if(s.charAt(j) == ')'){
                    cnt --;
                }
                
                if(cnt < 0){
                    possible = false;
                    break;
                }

            }

            if(possible&&cnt == 0){
                sb.append("YES\n");
            }else{
                sb.append("NO\n");
            }


        }

        System.out.println(sb.toString());

    }



}