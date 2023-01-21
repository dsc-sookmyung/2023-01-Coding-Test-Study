import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //테스트 케이스의 수 입력
        int T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken()); //문서의 개수
            int M = Integer.parseInt(st.nextToken()); //궁금한 문서 위치

            //큐 채우기
            LinkedList<int[]> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());

            for(int j=0; j<N; j++){
                //[초기위치, 중요도] 로 정수 배열을 원소로 한 queue 생성
                queue.offer(new int[] {j, Integer.parseInt(st.nextToken())});
            }

            int count = 0; //출력 횟수

            while(!queue.isEmpty()) {
                int[] front = queue.poll(); //첫 번째 원소
                boolean isMax = true;

                //큐에 남아있는 원소들과 중요도 비교
                for(int j=0; j< queue.size(); j++){

                    //처음 뽑은 원소보다 큐에 있는 i번째 원소가 중요도가 더 큰 경우
                    if(front[1] < queue.get(j)[1]){

                        // front 원소가 가장 큰 원소가 아니었으므로 false 하고 탐색 마침
                        isMax = false;
                        break;
                    }
                }

                //isMax == true -> front 가 가장 큰 경우 -> 해당 원소의 첫 위치가 M이랑 같은지 비교
                //isMax == false -> front 원소가 가장 큰 경우가 아닌 경우 -> 반복문 다시 시작
                if(isMax){
                    count++;
                    if(front[0] == M) break;
                } else {
                    //뽑은 원소 및 i 이전의 원소들을 뒤로 보냄
                    queue.offer(front);
                }
            }
            sb.append(count).append("\n");
        }
        System.out.println(sb);
    }
}