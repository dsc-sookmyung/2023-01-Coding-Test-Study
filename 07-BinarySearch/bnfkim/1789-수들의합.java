import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 서로 다른 자연수의 개수
         * S -> 자연수의 합
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());
        System.out.println(Search(S));
    }
    public static int Search(long S){
        int count = 0;
        long sum = 0L;
        int i = 0;

        while(true) {
            sum += ++i;
            if(sum > S) return count;
            count++;
        }
    }
}