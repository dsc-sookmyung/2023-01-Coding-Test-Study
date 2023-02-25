import java.io.*;
import java.util.*;
public class Main {
    static int[][] map;
    static boolean visit[][];
    static int dx[] = {0, 0, -1, 1}; // -> 좌우 판단
    static int dy[] = {-1, 1, 0, 0}; // -> 상하 판단
    static int num = 0; //아파트 단지 번호 수
    static int count = 0; //단지로 묶인 수
    static int nowX, nowY, N;
    public static void main(String[] args) throws IOException {

        /**
         * N -> 지도의 크기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        visit = new boolean[N][N];
        List<Integer> list = new ArrayList<>();

        //전체 사각형 입력받기
        for(int i=0; i<N; i++) {
            String str = br.readLine();
            for(int j=0; j<N; j++) {
                map[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
            }
        }

        //지도 -> [방문하지 않고] + [1로 표시되어 있는 곳] -> 다시 dfs 메소드 실행 -> map 전체 탐색
        //모든 면에 0이 있으면 더 이상 갈 수 없다고 판단 -> 메소드 종료
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if (visit[i][j] == false && map[i][j] == 1) {
                    count = 0;
                    num++;
                    dfs(i, j);
                    list.add(count);
                }
            }
        }
        Collections.sort(list); //list 정렬
        sb.append(num).append("\n"); //총 단지수
        for(int num : list) {
            sb.append(num).append("\n");
        }
        System.out.println(sb);
    }

    private static void dfs(int x, int y) {
        visit[x][y] = true; //방문했다고 표시
        map[x][y] = num; //단지번호 부여
        count++;

        //범위에 맞는 값을 계산해서 nowX 와 nowY 저장
        for(int i=0; i<4; i++) {
            nowX = dx[i] + x;
            nowY = dy[i] + y;
            //범위조건에 true 일 경우에만 방문 여부를 true 로 바꿔줌
            if(check() && visit[nowX][nowY] == false && map[nowX][nowY] == 1) {
                visit[nowX][nowY] = true;
                map[nowX][nowY] = num;

                dfs(nowX, nowY);
            }
        }
    }

    private static boolean check() {
        return (nowX >= 0 && nowX < N && nowY >= 0 && nowY <N);
    }
}