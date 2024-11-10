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
            int num = Integer.parseInt(st.nextToken());

            sb.append(upperBound(num) - lowerBound(num) + " ");

        }

        System.out.println(sb.toString());
    }



    public static int lowerBound(int target){
        int left = 0;
        int right = card.length;

        while(left < right){
            int mid = (left+right)/2;

            if(card[mid] >= target) {
                right = mid;
            }
            else{
                left = mid + 1;
            }

        }

        return left;
    }

    public static int upperBound(int target){
        int left = 0;
        int right = card.length;

        while(left < right){
            int mid = (left+right)/2;

            if(card[mid] > target) {
                right = mid;
            }
            else{
                left = mid + 1;
            }

        }

        return left;
    }




}