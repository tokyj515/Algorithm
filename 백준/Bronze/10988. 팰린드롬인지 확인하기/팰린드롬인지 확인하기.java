
import java.util.*;
import java.io.*;


public class Main {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        for(int i = 0; i<s.length(); i++){

            if (s.charAt(i) != s.charAt(s.length()-1-i)){
                System.out.println(0);
                return;
            }

        }

        System.out.println(1);

    }


}