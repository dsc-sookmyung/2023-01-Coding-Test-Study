import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 관찰 횟수
         * 소의 번호 & 위치
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[11][1];
        int result = 0;

        for(int i=1; i<11; i++) {
            arr[i][0] = -1;
        }

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            //아직 관찰되지 않은 소 일 경우 -> y로 상태 바꿈
            if(arr[x][0] == -1) {
                arr[x][0] = y;
            } else {
                //관찰되었으나, 현재 소의 위치가 아니라면, 이동한 것이므로
                // result 를 증가시켜주고, 해당 위치로 새로 업데이트 해줌
                if(arr[x][0] != y) {
                    result++;
                    arr[x][0] = y;
                }
            }
        }
        System.out.println(result);
    }
}