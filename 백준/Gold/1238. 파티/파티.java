import java.util.*;
import java.io.*;


public class Main {

    static int N, M, X;

    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();

    static int[] dist;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        for(int i = 0; i<N+1;i++){
            graph.add(new ArrayList<>());
        }



        for(int i = 0; i<M; i++){
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph.get(u).add(new Node(v, w));
        }

        int[] answer = dijkstra(X);

        for(int i = 1; i<N+1; i++){
            if(i == X) continue;

            int[] answer2 = dijkstra(i);
            answer[i] += answer2[X];
        }

        int maxVal = 0;
        for(int i = 1; i<N+1; i++){
            if(maxVal < answer[i])
                maxVal = answer[i];
        }

        System.out.println(maxVal);

    }


    static int[] dijkstra(int start){
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<Node> pq = new PriorityQueue<>();

        dist[start] = 0;
        pq.offer(new Node(start, 0));


        while(!pq.isEmpty()){
            Node now = pq.poll();
            int v = now.v;
            int w = now.w;

            if(w > dist[v]){
                continue;
            }


            for(Node next : graph.get(v)){
                int newDist = dist[v] + next.w;

                if(newDist < dist[next.v]){
                    dist[next.v] = newDist;
                    pq.offer(new Node(next.v, newDist));
                }
            }
        }

        return dist;

    }



    static class Node implements Comparable<Node>{
        int v;
        int w;

        public Node(int v, int w){
           this.v = v;
           this.w = w;
        }

        @Override
        public int compareTo(Node other){
            return Integer.compare(this.w, other.w);
        }


    }




}