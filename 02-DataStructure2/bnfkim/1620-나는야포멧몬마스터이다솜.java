import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N
         * 내가 맞춰야 하는 문제의 개수 M
         *
         * 알파벳으로만 들어오면 -> 포켓몬 번호 출력
         * 숫자로만 들어오면 -> 포켓몬 번호에 해당하는 문자를 출력
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> bookMap = new HashMap<>();
        String[] bookArr = new String[N+1];

        for(int i=1; i<N+1; i++){
            String name = br.readLine();
            bookMap.put(name, i); //이름 -> 번호 찾는 용
            bookArr[i] = name; //번호 -> 이름 찾는 용
        }

        while(M --> 0) {
            String question = br.readLine();
            // 숫자를 입력받은 경우
            if (isNumeric(question)) {
                sb.append(bookArr[Integer.parseInt(question)]);
            } else {
                sb.append(bookMap.get(question));
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    //문자열이 숫자인지 아닌지 판단하는 함수
    public static boolean isNumeric(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}