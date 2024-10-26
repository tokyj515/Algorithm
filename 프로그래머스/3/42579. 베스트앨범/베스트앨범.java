import java.util.*;


class Solution {
    // 인덱스: 고유번호
    

    static Map<String, PriorityQueue<Element>> playMap = new HashMap<>();
    static PriorityQueue<Element> pq = new PriorityQueue<>();
    
    
    static ArrayList<Integer> answer = new ArrayList<>();
    
    
    
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        int n = genres.length;
    
            
        // 장르 : [인덱스, 재생횟수  => 내림차순]
        for(int i=0; i<n; i++){
            playMap.putIfAbsent(genres[i], new PriorityQueue<>());
            playMap.get(genres[i]).offer(new Element(genres[i], i, plays[i]));
        }
        
        // for(String key: playMap.keySet()){
        //     System.out.println(key +" " + playMap.get(key));
        // }
        
        // 장르: 총 재생횟수 => 내림차순
        for(String key: playMap.keySet()){
            PriorityQueue<Element> temp = playMap.get(key);
            
            int result = 0;
           
            for(Element e : temp){
                result += e.playCnt;
            }
            
            
            Element ele = new Element(key, 0, result);
            pq.offer(ele);
            
        }
        
        while(!pq.isEmpty()){
            String gerne = pq.poll().gerne;
            
            PriorityQueue<Element> eList = playMap.get(gerne);
            
            int cnt = 0;
            
            while(!eList.isEmpty() && cnt < 2){
                Element e = eList.poll();
                answer.add(e.idx);
                cnt++;
            }
            
            
        }
        
        
        
        
        return answer;
    }
    
    
    
    static public class Element implements Comparable<Element>{
        String gerne;
        int idx;
        int playCnt;
        
        public Element(String gerne, int idx, int playCnt){
            this.gerne = gerne;
            this.idx = idx;
            this.playCnt = playCnt;
        }
        
        
        @Override
        public int compareTo(Element other){
            return -Integer.compare(this.playCnt, other.playCnt);
        }
        
    }
    
}