import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * 입력 : 총 다섯줄의 입력
         * 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        char[][] arr = new char[5][15];

        for(int i = 0; i < 5; i++) {
            String s = br.readLine();

            for(int j = 0; j < s.length(); j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        for(int i = 0; i < 15; i++) {
            for(int j = 0; j < 5; j++) {
                if(arr[j][i] != '\0')
                    sb.append(arr[j][i]);
            }
        }

        System.out.println(sb.toString());
    }
}