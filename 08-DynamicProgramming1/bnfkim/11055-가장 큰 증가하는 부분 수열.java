import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 수열 A의 크기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //입력값 받기
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N+1];
        int[] dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=1; i<N+1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        //각 원소의 가장 큰 증가 부분 수열 합
        int result = dp[1] = arr[1];
        for(int i=2; i<N+1; i++){
            dp[i] = arr[i];
            //dp[2] = 101, dp[3] = 3, dp[4] = 53, dp[5] = 113 ....
            for(int j=1; j<i; j++){
                //증가하는 부분 수열을 만들기 위해 필요한 조건식
                if(arr[i] > arr[j]){
                    //dp 에 이전 수열들이 저장되어있음. 하나씩 더하면서 dp를 그자리에서 업데이트
                    //기존 dp[i]를 비교했을때, 더 큰 값만 업데이트 되도록함
                    dp[i] = Math.max(dp[i], arr[i] + dp[j]);
                }
            }
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);
    }
}