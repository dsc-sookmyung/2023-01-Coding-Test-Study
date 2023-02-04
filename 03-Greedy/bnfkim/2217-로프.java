import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * 첫째 줄에 정수 N이 주어진다.
         * 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];

        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        //최대 중량이 제일 큰 로프순으로 써내서, 순서대로 병렬로 연결
        Arrays.sort(arr);
        int result = 0;

        for(int i=N-1; i>=0; i--){
            arr[i] = arr[i] * (N-i);
            if(result < arr[i]) {
                result = arr[i];
            }
        }
        System.out.println(result);

    }
}