import java.util.*;
import java.io.*;


public class Main {

    static int N;

    static Map<String, Integer> map = new TreeMap<>();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){

            String[] s = br.readLine().split("\\."); //이스케이프 필요

            map.put(s[1], map.getOrDefault(s[1], 0)+1);
        }

        StringBuilder sb = new StringBuilder();

        for(String key : map.keySet()){
            sb.append(key + " ").append(map.get(key) + "\n");
        }

        System.out.println(sb.toString());
    }


}