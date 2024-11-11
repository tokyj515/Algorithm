

import java.sql.Array;
import java.util.*;
import java.io.*;


public class Main {

    static int N ;
    static String[][] graph;
    static boolean[][] visited;

    static boolean found = false;

    static ArrayList<Pos> teacher = new ArrayList<>();

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};


    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        graph = new String[N][N];

        for(int i = 0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0; j<N; j++){
                graph[i][j] = st.nextToken();

                if(graph[i][j].equals("T")){
                    teacher.add(new Pos(i, j));
                }
            }
        }

        backtrack(0);

        if(found){
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }



    }


    static void backtrack(int dep){
        if(dep == 3){
            if(isSafe()){
                found = true;
            }
            return;
        }

        if(found) return;


        for(int i = 0; i<N; i++){
            for(int j = 0; j<N; j++){
                if(graph[i][j].equals("X")){
                    graph[i][j] = "O";
                    backtrack(dep+1);
                    graph[i][j] = "X";
                }

            }
        }

    }

    // 학생이 생존 가능한지?
    static boolean isSafe(){
        for(Pos p : teacher){
            int x = p.x;
            int y = p.y;

            for(int i = 0; i<4; i++){
                if(!move(x, y, i)){
                    return false;
                }
            }
        }
        return true;
    }

    static boolean move(int x, int y, int i){
        while(true){
            x += dx[i];
            y += dy[i];

            if (x < 0 || y < 0 || x >= N || y >= N) {
                break;
            }

            if(graph[x][y].equals("O")){
                break;
            }

            if(graph[x][y].equals("S")){
                return false;
            }
        }
        return true;
    }


    static public class Pos{
        int x;
        int y;

        public Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }



}