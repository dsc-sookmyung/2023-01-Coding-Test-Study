import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 물품의 수
         * K -> 준서가 버틸 수 있는 무게
         * W -> 각 물건의 무게
         * V -> 해당 물건의 가치
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] W = new int[N+1]; //무게
        int[] V = new int[N+1]; //가치
        int[] dp = new int[K+1];

        for(int i=1; i<N+1; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        /**
         * 가방 최대 무게를 넘기면 안 됨
         * 가방 최대 무게를 넘기지 않는 선에서, 물건의 가치합의 최댓값을 출력해야함
         *
         * W -> 6   4   3   5
         * V -> 13  8   6   12
         */

        /**
         * 다른 방법
         *             dp[][] = new int[N+1][K+1] 을 사용할경우
         *             for(int j=1; i<K+1; j++){
         *                 // i번째 무게를 더 담을 수 없는 경우
         *                 if (W[i] > j) {
         *                     dp[i][j] = dp[i-1][j];
         *                 } else { // i번째 무게를 더 담을 수 있는 경우
         *                     dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j - W[i]] + V[i]);
         *                 }
         *             }
         */

        for(int i=1; i<N+1; i++) {
            for(int j=K; j-W[i] >= 0; j--){
                dp[j] = Math.max(dp[j], dp[j - W[i]] + V[i]);
            }
        }
        System.out.println(dp[K]);
    }
}