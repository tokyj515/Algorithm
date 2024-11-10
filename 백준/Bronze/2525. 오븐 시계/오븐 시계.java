import java.util.*;
import java.io.*;


public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(st.nextToken());
        int min = Integer.parseInt(st.nextToken());

        int during = Integer.parseInt(br.readLine());

        min += during;

        hour += min / 60;
        min %= 60;
        hour %= 24;


        StringBuilder sb = new StringBuilder();
        sb.append(hour);
        sb.append(" ");
        sb.append(min);

        System.out.println(sb.toString());


    }


}