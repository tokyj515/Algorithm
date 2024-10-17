import java.util.*;

class Solution {
    
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int answer = 0;
    static StringBuilder sb = new StringBuilder();

    
    
    public int solution(int n, int[][] computers) {
        
        // [1] 그래프 세팅 
        visited = new boolean[n];
        
        for(int i=0; i<n; i++){
            graph.add(new ArrayList<>());
        }
        
        
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if (i == j) continue;
                
                if (computers[i][j] == 1){
                    graph.get(i).add(j);   
                }
                
            }
        }
        
        
        
        for(int i =0; i<n; i++){
            System.out.println(graph.get(i));
        }
        
        
        
        
        // [2] dfs 실행
        for(int i = 0; i<n; i++){
            if(!visited[i]){
                
                dfs(i);
                answer++;
                
                sb.append("\n");
                    
            }
        }
        
        System.out.println(sb.toString());
        
        return answer;

    
    }
    
    
    static void dfs(int v){
        visited[v] = true;
        sb.append(v).append(" ");
        
        
        for(int next: graph.get(v)){
            if(!visited[next]){
                dfs(next);
            }
            
        }
        
        
        
        
        
        
        
    }
    
    
    
    
}