import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * T -> 테스트 케이스
         * N -> 동전의 가지수
         * M -> 주어진 N가지 동전으로 만들어야 할 금액
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] coins;
        int[] dp;

        //입력값 받기
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 수

        while(T-->0){
            int N = Integer.parseInt(br.readLine()); //동전의 가지수
            coins = new int[N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=0; i<N; i++){
                coins[i] = Integer.parseInt(st.nextToken());
            }

            /**
             * {2,3,5}
             *            0  1  2  3  4  5  6  7  8  9  10
             * (2) dp ->  1  0  1  0  1  0  1  0  1  0  1
             * (3) dp ->  1  0  0  1  1  1  2  1  2  2  2
             * (5) dp ->  1  0  1  1  1  2  2  2  3  3  4
             *
             * => 총 네가지 방법
             */

            int M = Integer.parseInt(br.readLine());
            dp = new int[M+1];
            dp[0] = 1;
            for(int coin : coins) {
                for(int j = coin; j<M+1; j++){
                    dp[j] = dp[j] + dp[j - coin];
                }
            }
            System.out.println(dp[M]);
        }
    }
}