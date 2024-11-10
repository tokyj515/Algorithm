import java.util.*;
import java.io.*;


public class Main {

    static int N;
    static Set<String> set = new TreeSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            String name = st.nextToken();

            if(set.contains(name)){
                set.remove(name);
            }
            else{
                set.add(name);
            }
        }

        List<String> list = new ArrayList<>(set);
        Collections.reverse(list);

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<list.size(); i++){
            sb.append(list.get(i) + "\n");
        }

        System.out.println(sb.toString());
    }




}