import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * [dp]
         * 2원 짜리와 5원짜리로만 거스름돈
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int count = 0;

        while(n>0) {
            //5로 나뉘는 경우
            if (n%5 == 0) {
                count = n/5 + count;
                break;
            }

            //5로 나뉘지 않으면 2씩 빼기
            n = n-2;
            count++;
        }
        if (n < 0) {
            System.out.println(-1);
        } else {
            System.out.println(count);
        }
    }
}