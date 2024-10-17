import java.util.*;
import java.io.*;


public class Main {


    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder(); //정답을 담을 sb



    public static void main(String[] args) throws IOException {
        //입력 => 여긴 몰라도 됨
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 정점의 개수
        int m = Integer.parseInt(st.nextToken()); // 간선의 개수
        int start = Integer.parseInt(st.nextToken()); // 시작 정점


        //구현

        //그래프 간선 저장 + 정렬
        for(int i = 0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }


        // 간선 정보 저장
        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        // 작은 것부터 방문하려면
        for(int i=0; i<=n; i++){
            Collections.sort(graph.get(i));
        }


        // dfs
        visited = new boolean[n+1];
        dfs(start);
        sb.append("\n");


        // bfs
        visited = new boolean[n+1];
        bfs(start);


        System.out.print(sb.toString());
    }


    // 함수 구현부
    static void dfs(int v){
        visited[v] = true;
        sb.append(v).append(" ");


        for(int i: graph.get(v)){
            if (!visited[i]) {
                dfs(i);
            }
        }
    }


    static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();

        visited[start] = true;
        queue.add(start);


        while (!queue.isEmpty()){
            Integer v = queue.poll();
            sb.append(v).append(" ");

            for(int i: graph.get(v)){
                if (!visited[i]){
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }




}

