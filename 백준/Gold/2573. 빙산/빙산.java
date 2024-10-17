

import java.util.*;
import java.io.*;

public class Main {

    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int time = 0;

    static class Pos {
        int x;
        int y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 행의 개수
        int m = Integer.parseInt(st.nextToken()); // 열의 개수

        graph = new int[n][m];

        // 배열 요소 입력
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            time++;
            int[][] tempGraph = new int[n][m];

            // 빙하 녹이기
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int cnt = melt(i, j, n, m);
                    tempGraph[i][j] = Math.max(0, graph[i][j] - cnt);
                }
            }

            // 그래프 업데이트
            graph = tempGraph;

            // 덩어리 개수 확인
            int cnt = 0;
            visited = new boolean[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] > 0 && !visited[i][j]) {
                        bfs(new Pos(i, j), n, m);
                        cnt++;
                    }
                }
            }

            // 빙하가 2덩어리 이상인 경우
            if (cnt >= 2) {
                System.out.println(time);
                break;
            }

            // 빙하가 모두 녹은 경우
            if (cnt == 0) {
                System.out.println(0);
                break;
            }
        }
    }

    static int melt(int x, int y, int n, int m) {
        int cnt = 0;

        Pos[] posArr = {new Pos(x - 1, y), new Pos(x + 1, y), new Pos(x, y - 1), new Pos(x, y + 1)};

        for (Pos pos : posArr) {
            int i = pos.x;
            int j = pos.y;

            if (0 <= i && i < n && 0 <= j && j < m && graph[i][j] == 0) cnt++;
        }

        return cnt;
    }

    static void bfs(Pos pos, int n, int m) {
        Deque<Pos> queue = new ArrayDeque<>();
        queue.offer(pos);
        visited[pos.x][pos.y] = true;

        while (!queue.isEmpty()) {
            Pos cur = queue.poll();
            int x = cur.x;
            int y = cur.y;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && graph[nx][ny] > 0) {
                    queue.offer(new Pos(nx, ny));
                    visited[nx][ny] = true;
                }
            }
        }
    }
}
