import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * s가 t의 부분 문자열인지 판단하는 프로그램
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st;
        String str;

        while((str=br.readLine()) != null) {
            st = new StringTokenizer(str);

            String str1 = st.nextToken();
            String str2 = st.nextToken();
            int idx = 0;

            for(int i=0; i<str2.length(); i++){
                if(str1.charAt(idx) == str2.charAt(i)){
                    idx++;
                }
                if (idx == str1.length()) break;
            }

            if (idx == str1.length()) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}