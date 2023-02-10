import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 전구 개수
         * M -> 명령어의 개수
         * 1 -> 전구가 켜져 있는 상 & 0 -> 전구가 꺼져 있는 상태
         *
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

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if(command == 1){ //1번 명령어인 경우 -> i번째 전구 x로 상태 변경
                arr[x-1] = y;
            } else {
                for (int j=x-1; j<y; j++) {
                    if (command == 2) { //2번 명령어인 경우 -> l~r 전구 상태 변경
                        if(arr[j] == 0) arr[j] = 1;
                        else arr[j] = 0;
                    } else if (command == 3) { //3번 명령어인 경우 -> l~r 전구 끄기
                        arr[j] = 0;
                    } else { //4번 명령어인 경우 -> l~r 전구 키기
                        arr[j] = 1;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int data : arr) {
            sb.append(data).append(" ");
        }
        System.out.println(sb);
    }
}