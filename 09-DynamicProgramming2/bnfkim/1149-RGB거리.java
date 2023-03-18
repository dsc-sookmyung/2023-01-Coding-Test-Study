import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 집의 가지수
         * 각 집을 빨강, 초록, 파랑으로 칠하는 비용 입력
         * 모든 집을 칠하는 비용의 최솟값 구하기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[][] house;
        int[][] dp;

        //입력값 받기
        int N = Integer.parseInt(br.readLine());
        house = new int[N+1][3];
        dp = new int[N+1][3];

        for(int i=1; i<N+1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            house[i][0] = Integer.parseInt(st.nextToken()); //빨강색 비용
            house[i][1] = Integer.parseInt(st.nextToken()); //초록색 비용
            house[i][2] = Integer.parseInt(st.nextToken()); //파랑색 비용
        }

        //초기값 설정
        dp[1][0] = house[1][0];
        dp[1][1] = house[1][1];
        dp[1][2] = house[1][2];

        for(int i=2; i<N+1; i++){
            //빨간색의 경우
            dp[i][0] = Math.min(dp[i-1][1] , dp[i-1][2]) + house[i][0];
            //초록색의 경우
            dp[i][1] = Math.min(dp[i-1][0] , dp[i-1][2]) + house[i][1];
            //파란색의 경우
            dp[i][2] = Math.min(dp[i-1][0] , dp[i-1][1]) + house[i][2];
        }
        int temp = Math.min(dp[N][0], dp[N][1]);
        System.out.println(Math.min(temp, dp[N][2]));
    }
}