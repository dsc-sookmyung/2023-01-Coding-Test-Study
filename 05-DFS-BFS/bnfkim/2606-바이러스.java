import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int computer[][]; //그래프 배열
    static int check[]; //방문배열

    static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();

        check[start] = 1; //시작한 컴퓨터는 감염되었다고 체크
        queue.offer(start); //큐에 start 컴퓨터 넣음
        int cnt = 0;

        while(!queue.isEmpty()){
            int x = queue.poll();

            for(int i=1; i< computer.length; i++){
                if (computer[x][i] == 1 && check[i] != 1){
                    queue.offer(i);
                    check[i] = 1;
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
    public static void dfs(int start) {

        check[start] = true;
        count++;

        for(int i = 0 ; i <= node ; i++) {
            if(arr[start][i] == 1 && !check[i])
                dfs(i);
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int com = Integer.parseInt(br.readLine()); //컴퓨터 수
        int net = Integer.parseInt(br.readLine()); //컴퓨터 쌍의 수

        computer = new int[com+1][com+1];
        check = new int[com+1];

        //컴퓨터 배열에 세팅
        for (int i=0; i<net; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            //무방향 그래프 희소행렬 표현 방법법
            computer[a][b] = 1;
            computer[b][a] = 1;
        }
        bfs(1);
    }
}