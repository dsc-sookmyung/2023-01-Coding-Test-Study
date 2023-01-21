import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //사람 수
        int K = Integer.parseInt(st.nextToken()); //순서

        Queue<Integer> queue = new LinkedList<>();

        //사람의 수 만큼 원소 넣기
        for(int i=0; i<N; i++){
            queue.offer(i+1);
        }

        sb.append("<");

        while (queue.size() != 1){
            for (int i = 0; i<K-1; i++){
                queue.offer(queue.poll());
            }
            sb.append(queue.poll()).append(", ");
        }

        sb.append(queue.poll()).append(">");
        System.out.println(sb);
    }
}