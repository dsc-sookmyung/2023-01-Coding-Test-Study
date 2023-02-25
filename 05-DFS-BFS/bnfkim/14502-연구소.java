import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    static int[][] map; //지도
    static int[][] copyMap; //카피지도
    static int M, N; //가로세로
    static int nowX, nowY;
    static int[] dx = {0, 0, -1, 1}; //상하좌우
    static int[] dy = {-1, 1, 0, 0}; //상하좌우
    static int result = Integer.MIN_VALUE; //안전지역 개수

    //Queue 에 좌표값 x,y를 넣기 위함.
    static class Node {
        int x, y;
        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        /**
         * N -> 상자의 세로 칸의 수
         * M -> 상자의 가로 칸의 수
         * 0=빈칸, 1=벽, 2=바이러스
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        copyMap = new int[N][M];

        //지도 입력
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //지도카피
        copyMap = map;
        //벽 세우면서 바이러스 뿌리기 시작
        dfs(0);

        System.out.println(result);
    }
    //벽 세우기
    private static void dfs(int depth) {
        //벽이 3개 설치된 경우 -> bfs 탐색 시작
        if(depth == 3) {
            bfs();
            return;
        }
        //벽 3개 설치 못 한 경우 -> 다시 세움
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(map[i][j] == 0) {
                    //벽 세우기
                    map[i][j] = 1;
                    dfs(depth+1);
                    //다시 돌려놓기
                    map[i][j] = 0;
                }
            }
        }
    }

    private static void bfs() {
        Queue<Node> q = new LinkedList<>();

        //virusMap copy
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                copyMap[i][j] = map[i][j];

                if(map[i][j] == 2) {
                    q.add(new Node(i,j));
                }
            }
        }

//        //바이러스라면 큐에 넣음
//        for(int i=0; i<N; i++) {
//            for(int j=0; j<M; j++) {
//                if(map[i][j] == 2) {
//                    q.add(new Node(i,j));
//                }
//            }
//        }

        //bfs 탐색 시작
        while (!q.isEmpty()) {
            Node now = q.poll();
            //현재값
            int x = now.x;
            int y = now.y;

            for(int k=0; k<4; k++) {
                nowX = dx[k] + x;
                nowY = dy[k] + y;

                //연구소 범위 밖이 아닌 경우 + 빈칸인 경우 -> 바이러스
                if(checkRange()) {
                    if(copyMap[nowX][nowY] == 0) {
                        q.add(new Node(nowX, nowY));
                        copyMap[nowX][nowY] = 2;
                    }
                }
            }
        }
        //SafeZone 확인
        safe(copyMap);
    }

    private static void safe(int[][] copyMap) {
        int safeZone =0;
        for(int i=0; i<N ; i++) {
            for(int j=0; j<M; j++) {
                if(copyMap[i][j] == 0) {
                    safeZone++;
                }
            }
        }
        if (result < safeZone) {
            result = safeZone;
        }
    }

    private static boolean checkRange() {
        return (nowX >= 0 && nowX < N && nowY >= 0 && nowY <N);
    }
}