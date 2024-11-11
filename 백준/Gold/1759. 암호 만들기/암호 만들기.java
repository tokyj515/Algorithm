

import java.util.*;
import java.io.*;

public class Main {

    static int L, C;
    static String[] alp;
    static ArrayList<String> result = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        alp = new String[C];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            alp[i] = st.nextToken();
        }

        Arrays.sort(alp);

        backtrack(0, 0, new StringBuilder());

        for (String res : result) {
            System.out.println(res);
        }
    }

    static void backtrack(int dep, int pre, StringBuilder password) {
        if (dep == L) {
            int vowelCount = 0;
            int consonantCount = 0;

            for (int i = 0; i < password.length(); i++) {
                char ch = password.charAt(i);
                if (isVowel(ch)) {
                    vowelCount++;
                } else {
                    consonantCount++;
                }
            }

            // 모음이 1개 이상이고 자음이 2개 이상인 경우만 추가
            if (vowelCount >= 1 && consonantCount >= 2) {
                result.add(password.toString());
            }
            return;
        }

        for (int i = pre; i < C; i++) {
            password.append(alp[i]);
            backtrack(dep + 1, i + 1, password);
            password.deleteCharAt(password.length() - 1); // 백트래킹
        }
    }

    static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
