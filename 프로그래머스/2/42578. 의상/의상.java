import java.util.*;

class Solution {
    
    static Map<String, ArrayList<String>>  map = new HashMap<>();
    static int n = 0;
    static int answer = 1;

    
    // 조합 변수
    // static ArrayList<String> answer = new ArrayList<>();
    // static ArrayList<String> result = new ArrayList<>();
    
    
    
    public int solution(String[][] clothes) {
        n = clothes.length;
        
        for(int i = 0; i<n; i++){
            map.putIfAbsent(clothes[i][1], new ArrayList<>());
            map.get(clothes[i][1]).add(clothes[i][0]);
        }
        
        
        
        for(String key: map.keySet()){
            ArrayList<String> values = map.get(key);
            answer *= values.size()+1;
            System.out.println(values);
        }


        
        return answer-1;
    }
    
    
    
//     static public backtrack(int dep, ArrayList<String> list, int pre){
        
//         if 
        
        
//     }
    
    
    
    
    
    
    
    
}