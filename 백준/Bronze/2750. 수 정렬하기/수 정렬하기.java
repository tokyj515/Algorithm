import java.util.*;
import java.io.*;


public class Main {
    
    static int N;
    static ArrayList<Integer> list = new ArrayList<>();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        
        for(int i=0; i<N; i++){
             list.add(Integer.parseInt(br.readLine()));
        }
        
        Collections.sort(list);
                
        
        for(Integer i : list){
            System.out.println(i);
        }
        
    }


}