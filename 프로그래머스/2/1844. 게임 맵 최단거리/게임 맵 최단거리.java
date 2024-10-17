import java.util.*;


class Solution {
    
    static class Position {
        int x;
        int y;

        Position(int x, int y){
            this.x = x;
            this.y = y;
        }
    
    
    }

    
    
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
               
        Deque<Position> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        
        queue.offer(new Position(0, 0));    
        visited[0][0] = true;    
        
        
        while (!queue.isEmpty()){
            Position cur = queue.poll();
            
            int x = cur.x;
            int y = cur.y;
            
            
            for(int i = 0; i<4; i++){
                int nx = x +dx[i];
                int ny = y +dy[i];
                
                if(0<= nx && nx<n && 0<= ny && ny<m && !visited[nx][ny] && maps[nx][ny] == 1){
                    queue.offer(new Position(nx, ny));
                    visited[nx][ny] = true;
                    maps[nx][ny] = maps[x][y] + 1;
                }
            } 
        }
        
        
        
//         for (int i=0; i<n; i++){
//             for(int j=0; j<m; j++){
//                 System.out.print(maps[i][j] + " ");
//             }
//             System.out.println();
//         }
        
        
        if(maps[n-1][m-1] > 1){
            return maps[n-1][m-1];
        }
        
        
        
        return -1;
    }
}