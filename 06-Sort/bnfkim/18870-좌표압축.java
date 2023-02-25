import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 좌표의 개수
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] originArr = new int[N];
        int[] sortedArr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        //입력받기
        for(int i=0; i<N; i++) {
            sortedArr[i] = originArr[i] = Integer.parseInt(st.nextToken());
        }

        //정렬하기
        Arrays.sort(sortedArr);

        //맵에 넣어주기
        int rank = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int value : sortedArr) {
            //앞선 원소가 이미 순위가 매겼을 시 중복되지 않게 처리
            if(!map.containsKey(value)) {
                map.put(value, rank);
                rank++;
            }
        }

        //출력하기
        for(int value : originArr) {
            sb.append(map.get(value)).append(" ");
        }
        System.out.println(sb);
    }
}