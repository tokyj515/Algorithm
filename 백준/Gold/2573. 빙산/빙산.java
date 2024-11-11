

import java.util.*;
import java.io.*;


public class Main {

    static int N, M;
    static int[][] graph;
    static boolean[][] visited;


    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static int time = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

//        visited = new boolean[N][M];
        graph = new int[N][M];
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j =0; j<M; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }




        while(true){
            time++;

            graph = melt();

            int area = 0;
            visited = new boolean[N][M];

            for(int i = 0; i<N; i++){
                for(int j=0; j<M; j++){
                    if(graph[i][j] > 0 && !visited[i][j]){
                        bfs(i, j);
                        area++;
                    }
                }
            }


            if(area >= 2 ){
                System.out.println(time);
                break;
            }


            if(area ==0){
                System.out.println(0);
                break;
            }
        }




    }


    static int[][] melt(){
        int[][] temp = new int[N][M];

        for(int i = 0; i<N; i++){
            for(int j = 0; j<M; j++){
                int cnt = 0;

                if(graph[i][j] > 0){
                    for(int k = 0; k<4; k++){
                        int nx = i + dx[k];
                        int ny = j + dy[k];

                        if(0<=nx && nx <N && 0<= ny && ny<M && graph[nx][ny] == 0){
                            cnt++;
                        }
                    }
                }

                temp[i][j] = Math.max(graph[i][j] - cnt, 0);
            }
        }

        return temp;
    }


    static void bfs(int startX, int startY){
        Deque<Pos> q = new ArrayDeque<>();
        q.offer(new Pos(startX, startY));
        visited[startX][startY] = true;


        while(!q.isEmpty()){
            Pos p = q.poll();
            int x = p.x;
            int y = p.y;

            for(int i = 0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0<= nx && nx<N && 0<=ny && ny<M && !visited[nx][ny] && graph[nx][ny] > 0){
                    q.offer(new Pos(nx, ny));
                    visited[nx][ny] = true;
                }

            }


        }




    }


    static class Pos{
        int x;
        int y;

        Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

}