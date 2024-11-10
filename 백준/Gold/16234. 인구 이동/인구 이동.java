
import java.util.*; //추가 필수
import java.io.*;


public class Main {

    static int N, L, R;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static int day = 0;
    static boolean moved;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 상수 세팅
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());


        // 그래프 세팅
        graph = new int[N][N];
        visited = new boolean[N][N];
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        

        moved = true; //시작
        
        while(moved){
            moved = false;
            visited = new boolean[N][N];

            for(int i = 0; i<N; i++){
                for(int j = 0; j<N; j++){

                    if(!visited[i][j]){
                        List<Pos> path = bfs(i, j);

                        if(path.size() > 1){
                            moved = true;

                            int people = 0;
                            for(Pos p : path){
                                people += graph[p.x][p.y];
                            }

                            int avg = people / path.size();
                            for(Pos p : path){
                                graph[p.x][p.y] = avg;
                            }
                        }
                    }
                }
            }

            if(!moved){
                break;
            }

            day++;

        }
        System.out.println(day);
    }


    static class Pos{
        int x;
        int y;

        Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }


    static List<Pos> bfs(int x, int y){
        Queue<Pos> q = new ArrayDeque<>();
        List<Pos> path = new ArrayList<>();


        q.offer(new Pos(x, y));
        visited[x][y] = true;
        path.add(new Pos(x, y));


        while(!q.isEmpty()){
            Pos now = q.poll();

            for(int i = 0; i<4; i++){
                int nx = now.x +dx[i];
                int ny = now.y + dy[i];

                if(0<= nx && nx <N && 0<= ny && ny < N && !visited[nx][ny]){

                    int gap = Math.abs(graph[now.x][now.y] - graph[nx][ny]);

                    if (L <= gap && gap <= R){
                        q.offer(new Pos(nx, ny));
                        visited[nx][ny] = true;
                        path.add(new Pos(nx, ny));
                    }
                }

            }
        }


        return path;
    }

}