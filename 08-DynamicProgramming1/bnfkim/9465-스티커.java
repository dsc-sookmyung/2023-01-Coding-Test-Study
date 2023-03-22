import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 수열 A의 크기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[][] arr;
        int[][] dp;

        //입력값 받기
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 수

        for(int k=0; k<T; k++){
            int n = Integer.parseInt(br.readLine()); //스티커 행의 수

            arr = new int[2][n+1];
            dp = new int[2][n+1];

            //입력받기
            for(int i=0; i<2; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j=1; j<n+1; j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            //초기값 설정
            dp[0][1] = arr[0][1];
            dp[1][1] = arr[1][1];

            for(int i=2; i<n+1; i++){
                dp[0][i] = Math.max(dp[1][i-1], dp[1][i-2]) + arr[0][i];
                dp[1][i] = Math.max(dp[0][i-1], dp[0][i-2]) + arr[1][i];
                // 밑과 같이 전개됨
                // 50 40  200 140 250
                // 30 100 120 210 260
            }
            System.out.println(Math.max(dp[0][n], dp[1][n]));
        }
    }
}