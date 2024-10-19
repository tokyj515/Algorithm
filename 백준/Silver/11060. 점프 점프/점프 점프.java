
import java.util.*;
import java.io.*;

public class Main {

    static int[] arr;
    static Deque<Element> queue = new ArrayDeque<>();
    static int[] visited;

    public static class Element{
        int x;
        int dep;

        Element(int x, int dep){
            this.x = x;
            this.dep = dep;
        }
    }

    public static void main(String[] args) throws IOException {
        //입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }


        visited = new int[n+1];
        for(int i=0; i<n; i++){
            visited[i] = -1;
        }


        queue.offer(new Element(0, 0));
        visited[0] = 0;


        while(!queue.isEmpty()){
            Element cur = queue.poll();

            int x = cur.x;
            int dep = cur.dep;
            int dist = arr[x];


            if (x == n-1){
                System.out.println(dep);
                return;
            }



            for(int i=x+1; i<=x+dist; i++){
                if (i < n && visited[i] == -1){
                    queue.offer(new Element(i, dep+1));
                    visited[i] = dep+1;
                }
            }

        }


        System.out.println(-1);

    }
}
