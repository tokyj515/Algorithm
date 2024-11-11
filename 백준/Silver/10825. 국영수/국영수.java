import java.util.*;
import java.io.*;


public class Main {

    static int N;

    static ArrayList<Element> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            String name = st.nextToken();
            int kor = Integer.parseInt(st.nextToken());
            int eng = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());

            list.add(new Element(name, kor, eng, math));
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for(Element e : list){
            sb.append(e.name + "\n");
        }

        System.out.println(sb.toString());

    }


    static class Element implements Comparable<Element>{
        String name;
        int kor;
        int eng;
        int math;

        public Element(String name, int kor, int eng, int math){
            this.name = name;
            this.kor = kor;
            this.eng = eng;
            this.math = math;
        }

        @Override
        public int compareTo(Element other){

            if(this.kor == other.kor){
                if(this.eng == other.eng){
                    if(this.math == other.math){
                        return this.name.compareTo(other.name);
                    } else {
                        return -Integer.compare(this.math, other.math);
                    }
                } else {
                    return Integer.compare(this.eng, other.eng);
                }
            } else {
                return -Integer.compare(this.kor, other.kor);
            }

        }

    }


}