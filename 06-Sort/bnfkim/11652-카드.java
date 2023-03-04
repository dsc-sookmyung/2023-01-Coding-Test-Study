import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 준규가 가지고 있는 수자 카드의 개수
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();

        int max = 0;
        long result = 0;

        //갯수가 가장 많은 경우를 해야하므로 map 사용
        for(int i=0; i<N; i++) {
            Long num = Long.parseLong(br.readLine());
            map.put(num, map.getOrDefault(num, 0)+1);

            if(map.get(num) > max) {
                max = map.get(num);
                result = num;
            } else if (map.get(num) == max) {
                //만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력
                result = Math.min(result, num);

            }
        }
        System.out.println(result);
    }
}