import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 카드의 개수
         * M -> 가까워져야 할 숫자
         * 카드 N 개 중 3개를 골라 M 에 가깝게
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = blackjack(arr, N, M);
        System.out.println(result);

    }
    static int blackjack(int[] arr, int N, int M) {

        int result = 0;

        for(int i=0; i<N-2; i++) {

            //첫 번째 카드가 M보다 클 경우 -> 넘어가버림
            if(arr[i] > M) continue;

            for(int j=i+1; j<N-1; j++) {

                //첫 번째 카드 + 두번째 카드 M보다 클 경우 -> 넘어가버림
                if(arr[i] + arr[j] > M) continue;

                for(int k=j+1; k<N; k++) {

                    // 카드 세개를 더해서 변수 temp 저장
                    int temp = arr[i] + arr[j] + arr[k];

                    // M과 세 카드의 합이 같을 경우 -> 종료
                    if (M == temp) {
                        return temp;
                    }

                    if(result<temp && temp<M) {
                        result = temp;
                    }
                }
            }
        }
        return result;
    }
}