import java.util.*;
import java.io.*;


public class Main {

//    static Map<String, Integer> map = new HashMap<>();

    static Set<String> set = new HashSet<>();
    static int N, M;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for(int i = 0; i<N; i++){
            String name = br.readLine();
            set.add(name);
        }

        List<String> list = new ArrayList<>();

        for(int i=0; i<M; i++){
            String name = br.readLine();
            if (set.contains(name)){
                list.add(name);
            }
        }
        
        Collections.sort(list);


        StringBuilder sb = new StringBuilder();
        sb.append(list.size() + "\n");
        for(String s : list){
            sb.append(s+"\n");
        }

        System.out.println(sb.toString());

    }






}