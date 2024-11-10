import java.util.*;
import java.io.*;


public class Main {

    static int N;
    static ArrayList<Member> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            Member m = new Member(Integer.parseInt(st.nextToken()), st.nextToken(), i);

            list.add(m);
        }

        Collections.sort(list);


        StringBuilder sb = new StringBuilder();

        for(Member m: list){
            sb.append(m.age + " " + m.name + "\n");
        }

        System.out.println(sb.toString());

    }


    static class Member implements Comparable<Member>{
        int age;
        String name;
        int order;

        public Member(int age, String name, int order){
            this.age = age;
            this.name = name;
            this.order = order;
        }

        @Override
        public int compareTo(Member other){
            if(this.age == other.age){
                return Integer.compare(this.order, other.order);
            }
            return Integer.compare(this.age, other.age);
        }


    }

}