
import java.util.*;
import java.io.*;


public class Main {

    static int N;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();
    static ArrayList<Element> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            list.add(new Element(start, end));
        }

        Collections.sort(list);

        pq.offer(list.get(0).end);

        for(int i = 1; i<N; i++){
            if(pq.peek() <= list.get(i).start) {
                pq.poll();
            }
            pq.offer(list.get(i).end);
        }

        System.out.println(pq.size());
    }


    static class Element implements Comparable<Element>{
        int start;
        int end;

        public Element(int start, int end){
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Element other){
            return Integer.compare(this.start, other.start);
        }
    }

}