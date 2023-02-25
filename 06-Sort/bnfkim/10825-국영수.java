import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 도영이네 반의 학생 수
         * 학생 이름, 국어, 영어, 수학 점수
         * 국어점수 감소 > 영어 점수 증가 > 수학 점수 감소 > 사전 순 이름
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        //학생 정보 입력
        String[][] arr = new String[N][4];
        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr[i][0] = st.nextToken();
            arr[i][1] = st.nextToken();
            arr[i][2] = st.nextToken();
            arr[i][3] = st.nextToken();
        }

        //정렬하기
        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(o2[1].equals(o1[1])){ //국어점수가 같으면
                    if(o1[2].equals(o2[2])){ //영어점수가 같으면
                        if(o1[3].equals(o2[3])) { //수학점수가 같으면
                            //compareTo -> 문자열의 아스키값을 기준으로 비교
                            //앞의 데이터의 앞 문자열과, 뒤의 데이터 앞 문자열의 아스키 차이값 반환
                            return o1[0].compareTo(o2[0]);
                        }
                        return Integer.parseInt(o2[3]) - Integer.parseInt(o1[3]);
                    }
                    return Integer.parseInt(o1[2])-Integer.parseInt(o2[2]);
                }
                return Integer.parseInt(o2[1])- Integer.parseInt(o1[1]);
            }
        });

        for(int i=0; i<arr.length; i++) {
            System.out.println(arr[i][0]);
        }
    }

}