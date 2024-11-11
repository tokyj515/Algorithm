import java.util.*;
import java.io.*;


public class Main {

    static int N;


    static Set<String> set = new HashSet<>();
    static List<Element> list = new ArrayList<>();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){
            set.add(br.readLine());
        }

        for(String s: set){
            list.add(new Element(s));
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();

        for(Element e: list){
            sb.append(e.s + "\n");
        }

        System.out.println(sb.toString());
    }


    static class Element implements Comparable<Element>{
        String s;

        public Element(String s){
            this.s = s;
        }

        @Override
        public int compareTo(Element other){

            if(this.s.length() == other.s.length()){
                return this.s.compareTo(other.s);
            }

            return Integer.compare(this.s.length(), other.s.length());
        }

    }


}