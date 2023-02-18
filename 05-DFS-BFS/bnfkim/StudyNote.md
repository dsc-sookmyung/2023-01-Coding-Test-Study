# **05-DataStructure5**

### 주제

- 구현
    - 완전구현
    - 시뮬레이션

### 구현 문제

·  풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

- 코딩 테스트에서는 구현이 중심이 되는 문제가 자주 출제된다.

- ex) 완전 탐색, 시뮬레이션 유형

▶ 완전 탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법

▶ 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제

# 2606 : 바이러스

[2606번: 바이러스](https://www.acmicpc.net/problem/2606)

```java
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
```

### ⚠️ Point ⚠️

- arr[a][b] = a [b][a] = 1의 값을 넣어줍니다. 양쪽에 다 넣어주는 이유는 1, 2나 2,1이나 같은 의미
- 그냥 단순하게 전구 갯수만큼의 배열로 만들고 전구 상태를 바꿔줌
- DFS든 BFS든 어떠한 방법으로도 구할 수 있음

# 2667번 : 단지번호붙이기

[2667번: 단지번호붙이기](https://www.acmicpc.net/problem/2667)

```java
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
```

### ⚠️ Point ⚠️

- String.valueOf()
    - 문자열 형변환
    - 파라미터가 null이면 문자열 "null"을 만들어서 반환
- DFS, BFS로 풀 수 있는 문제
- 범위조건이 맞는 경우에만 true로 바꿔줌
    - (1) 배열의 범위를 벗어나지 않은 경우
        - `check()` 함수 → *`nowX* >= 0 && *nowX* < *N* && *nowY* >= 0 && *nowY* <*N*`
    - (2) 아직 방문하지 않은 경우
        - *`visit*[*nowX*][*nowY*] == false`
    - (3) 집이 있는 경우
        - *`map*[*nowX*][*nowY*] == 1`

# 7576 : 토마토

[14467번: 소가 길을 건너간 이유 1](https://www.acmicpc.net/problem/14467)

```java
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
```

### ⚠️ Point ⚠️

- 최소일수를 구하라고 했으니 BFS로 접근

어려워서 아래 사이트 참고

[[백준] 7576번 토마토 - Java, 자바](https://velog.io/@kimmjieun/%EB%B0%B1%EC%A4%80-7576%EB%B2%88-%ED%86%A0%EB%A7%88%ED%86%A0-Java-%EC%9E%90%EB%B0%94)

# 14502번 : 연구소

[14502번: 연구소](https://www.acmicpc.net/problem/14502)

```java
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
```

### ⚠️ Point ⚠️

- `clone()`
- 연구소 모든 칸에 벽을 세우려면 빈칸인지 확인을 하고 벽을 세워야 하기 때문에 dfs 방식으로 해결 할 수 있다.
- 바이러스는 **상하좌우 인접한 방향**으로 퍼지고 각 1*1정사각형으로 나누어져 있어 **가중치가 1**이기 떄문에 BFS를 사용하여 바이러스를 퍼트릴 수 있다.
- 바이러스를 퍼트려 얻을 수 있는 안전 영역의 최대 크기값을 계속 구한다.
- 안전 영역의 최대 크기를 출력한다.

어려워서 실패 및 아래 코드 참고 (다시 풀어볼 예정)