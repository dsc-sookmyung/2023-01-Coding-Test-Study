import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * n -> 포도주 잔의 개수
         * 3잔 연속에서 먹을 수 없음
         * 즉, 두가지 방법으로 나뉨
         * (1) 전 와인을 먹고 현재 와인을 먹기
         * (2) 전전 와인을 먹고 현재 와인을 먹기
         * ! 현재 와인을 먹지 않는 경우도 생각해야함
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] wine;
        int[] dp;

        //입력값 받기
        int n = Integer.parseInt(br.readLine());

        wine = new int[n+1];
        dp = new int[n+1];

        for(int i=1; i<n+1; i++){
            wine[i] = Integer.parseInt(br.readLine());
        }

        //초기값 설정
        dp[1] = wine[1];

        // n=1 의 경우를 대비하여 예외처리를 해주어야 한다
        if(n>1) dp[2] = wine[1] + wine[2];

        for(int i=3; i<n+1; i++) {
            // (현재와인 선택 안 한 경우) vs (지금까지 먹은 와인 + 전와인과 현재 와인을 먹은 경우)
            dp[i] = Math.max(dp[i-1], Math.max(dp[i-2], dp[i-3] + wine[i-1]) + wine[i]);
        }

        System.out.println(dp[n]);

        /**
         * wine 6  10  13   9  8  1
         * dp   6  16  23  28 33 33
         */
    }
}