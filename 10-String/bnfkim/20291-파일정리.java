import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N : 바탕화면에 있는 파일의 개수
         * 바탕화면에 있는 파일의 이름
         * 파일의 이름은 알파벳 소문자와 점(.)으로만 구성
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new TreeMap<>();
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();
            String key = str.substring(str.indexOf(".")+1);

            if(!map.containsKey(key)) {
                map.put(key, 1);
            } else {
                map.replace(key, map.get(key)+1);
            }
        }
        map.forEach((key, value) -> {
            System.out.println(key + " " + value);
        });
    }
}