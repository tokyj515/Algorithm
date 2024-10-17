import java.util.*;


class Solution {
    
    static int cnt = 100000;
    static ArrayList<String> wordList = new ArrayList<>();
    
    
    static ArrayList<String> answer = new ArrayList<>();
    static ArrayList<ArrayList<String>> result = new ArrayList<>();
    static boolean[] visited;
    
    // static int n = words.length;
    
    
    
    public int solution(String begin, String target, String[] words) {
        int n = words.length;
        wordList = new ArrayList<>(Arrays.asList(words));
        visited = new boolean[n+1];
        
        
        // 타겟이 존재하지 않으면 0
        if(!wordList.contains(target)){
            return 0;
        }
        
  
        backtrack(begin, target, 0, n);
        
        for(ArrayList<String> res: result){
            System.out.println(res);
        }
        
        
        return cnt;
    }
    
    
    static void backtrack(String word, String target, int dep, int n){
        
        if (word.equals(target)){
            ArrayList<String> temp = new ArrayList<>(answer);
            result.add(temp);
            cnt = Math.min(cnt, dep);
            return;
        }
        
        
        for(int i=0; i<n; i++){
            if (!visited[i] && canChange(word, wordList.get(i))){
                
                answer.add(wordList.get(i));
                visited[i] = true;
                
                backtrack(wordList.get(i), target, dep+1, n);
                
                answer.remove(answer.size()-1);
                visited[i] = false;

                
            }
        }
        
        
        
        
        
        
        
        
    }
    
    
    static boolean canChange(String word, String next){
        int diff = 0;
            
        for(int i=0; i<word.length(); i++){
            if (word.charAt(i) != next.charAt(i)) {
                 diff++;
            }
        }
        
        
        if(diff==1){
            return true;
        }
        return false;
    }
    
    
}