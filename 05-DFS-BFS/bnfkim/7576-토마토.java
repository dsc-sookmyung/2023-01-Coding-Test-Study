import java.io.*;
import java.util.*;
public class Main {
    static int[][] box; //토마토상자
    static int M, N; //가로세로

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0,0,-1,1};
    static int nowX, nowY;
    static StringTokenizer st;
    static Queue<int[]> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        /**
         * M -> 상자의 가로 칸의 수
         * N -> 상자의 세로 칸의 수
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        box = new int[N][M];

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
                //토마토가 익었더라면
                if(box[i][j] == 1) {
                    queue.add(new int[]{i,j});
                }
            }
        }
        System.out.println(bfs());
    }

    private static int bfs() {
        while(!queue.isEmpty()) {
            int[] temp = queue.poll();
            int x = temp[0];
            int y = temp[1];

            for(int i=0; i<4; i++) {
                nowX = dx[i] + x;
                nowY = dy[i] + y;

                if (nowX < 0 || nowX >= N || nowY < 0 || nowY >= M) continue;

                //다음 뎁스가 넘어갈 때 현재 뎁스에서 1 값을 증가시켜주는 식
                if(box[nowX][nowY] == 0) {
                    box[nowX][nowY] = box[x][y] + 1;
                    queue.add(new int[]{nowX, nowY});
                }
            }
        }
        int max = Integer.MIN_VALUE;
        if(checkZero()) {
            return -1;
        } else {
            for(int i=0; i<N; i++) {
                for(int j=0; j<M; j++) {
                    if (max < box[i][j]) {
                        max = box[i][j];
                    }
                }
            }
            return max-1;
        }
    }
    private static boolean checkRange() {
        return (nowX >= 0 && nowX < N && nowY >= 0 && nowY <N);
    }

    private static boolean checkZero() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (box[i][j] == 0)
                    return true;
            }
        }
        return false;
    }
}