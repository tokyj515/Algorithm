import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        ArrayList<String> participantList = new ArrayList<>(Arrays.asList(participant));
        ArrayList<String> completionList = new ArrayList<>(Arrays.asList(completion));
        
        Collections.sort(participantList);
        Collections.sort(completionList);
        
//         System.out.println(participantList);
//         System.out.println(completionList);
        
        int n = Math.min(participantList.size(), completionList.size());
        
        for(int i=0; i<n; i++){
            if (!participantList.get(i).equals(completionList.get(i))) {
                return participantList.get(i);
            }
        }
        
        
        
        return participantList.get(participantList.size()-1);
    }
}