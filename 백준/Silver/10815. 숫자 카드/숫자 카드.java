import java.util.*;
import java.io.*;


public class Main {

    static int N, M;
    static int[] card;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        card = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            card[i] = Integer.parseInt(st.nextToken());
        }


        Arrays.sort(card);


        StringBuilder sb = new StringBuilder();


        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++){
            int num =  Integer.parseInt(st.nextToken());

            if(binarySearch(num)){
                sb.append("1 ");
            }
            else {
                sb.append("0 ");
            }
        }

        System.out.println(sb.toString());
    }


    public static boolean binarySearch(int target){
        int left = 0;
        int right = card.length - 1;

        while(left <= right){
            int mid = (left+right) / 2;

            if(card[mid] == target){
                return true;
            }
            else if(card[mid] < target){
                left = mid + 1;
            }
            else {
                right = mid -1;
            }
        }
        return false;
    }


}