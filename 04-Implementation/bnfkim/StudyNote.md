# **04-DataStructure4**

### 주제

- 시뮬레이션
    - 완전구현
    -

# 21918번 : 전구

[21918번: 전구](https://www.acmicpc.net/problem/21918)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 전구 개수
         * M -> 명령어의 개수
         * 1 -> 전구가 켜져 있는 상 & 0 -> 전구가 꺼져 있는 상태
         *
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if(command == 1){ //1번 명령어인 경우 -> i번째 전구 x로 상태 변경
                arr[x-1] = y;
            } else {
                for (int j=x-1; j<y; j++) {
                    if (command == 2) { //2번 명령어인 경우 -> l~r 전구 상태 변경
                        if(arr[j] == 0) arr[j] = 1;
                        else arr[j] = 0;
                    } else if (command == 3) { //3번 명령어인 경우 -> l~r 전구 끄기
                        arr[j] = 0;
                    } else { //4번 명령어인 경우 -> l~r 전구 키기
                        arr[j] = 1;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int data : arr) {
            sb.append(data).append(" ");
        }
        System.out.println(sb);
    }
}
```

### ⚠️ Point ⚠️

- `if` 문을 통해서 명령어에 따라, 어떤 행동을 취할지 처리

# 2798번 : 블랙잭

[2798번: 블랙잭](https://www.acmicpc.net/problem/2798)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 카드의 개수
         * M -> 가까워져야 할 숫자
         * 카드 N 개 중 3개를 골라 M 에 가깝게
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = blackjack(arr, N, M);
        System.out.println(result);

    }
    static int blackjack(int[] arr, int N, int M) {

        int result = 0;

        for(int i=0; i<N-2; i++) {

            //첫 번째 카드가 M보다 클 경우 -> 넘어가버림
            if(arr[i] > M) continue;

            for(int j=i+1; j<N-1; j++) {

                //첫 번째 카드 + 두번째 카드 M보다 클 경우 -> 넘어가버림
                if(arr[i] + arr[j] > M) continue;

                for(int k=j+1; k<N; k++) {

                    // 카드 세개를 더해서 변수 temp 저장
                    int temp = arr[i] + arr[j] + arr[k];

                    // M과 세 카드의 합이 같을 경우 -> 종료
                    if (M == temp) {
                        return temp;
                    }

                    if(result<temp && temp<M) {
                        result = temp;
                    }
                }
            }
        }
        return result;
    }
}
```

### ⚠️ Point ⚠️

- 완전 탐색이므로 `for`문을 통해 모두 탐색하는 것이 중요
    - `삼중 for`문을 통해, 카드 3개의 합을 구함
- 카드 3개 미만일 경우에 넘으면 패스하도록 하면 시간을 줄일 수 있음

# 14467 : 소가 길을 건너간 이유1

[14467번: 소가 길을 건너간 이유 1](https://www.acmicpc.net/problem/14467)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * N -> 관찰 횟수
         * 소의 번호 & 위치
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[11][1];
        int result = 0;

        for(int i=1; i<11; i++) {
            arr[i][0] = -1;
        }

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            //아직 관찰되지 않은 소 일 경우 -> y로 상태 바꿈
            if(arr[x][0] == -1) {
                arr[x][0] = y;
            } else {
                //관찰되었으나, 현재 소의 위치가 아니라면, 이동한 것이므로
                // result 를 증가시켜주고, 해당 위치로 새로 업데이트 해줌
                if(arr[x][0] != y) {
                    result++;
                    arr[x][0] = y;
                }
            }
        }
        System.out.println(result);
    }
}
```

### ⚠️ Point ⚠️

- 관찰되지 않은 소의 경우와 아닌 경우를 나누고, 이동한 경우에만 체크할 것

# 2578번 : 빙고

[2578번: 빙고](https://www.acmicpc.net/problem/2578)

```java
import java.io.*;
import java.util.*;
public class Main {
    static int[][] arr = new int[5][5]; //빙고판
    static int result = 0; //체크
    public static void main(String[] args) throws IOException {

        /**
         * N -> 관찰 횟수
         * 소의 번호 & 위치
         */

        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        StringTokenizer st;

        //빙고판 입력받기
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        for(int x=0; x<25; x++){
            int num = sc.nextInt();

            //부른 값은 0으로 체크하기
            for(int i=0; i<5; i++){
                for(int j=0; j<5; j++) {
                    if(arr[i][j] == num)  arr[i][j] = 0;
                }
            }

            //빙고 체크하기
            rowCheck();
            colCheck();
            diagonalL();
            diagonalR();

            //빙고 3개 이상일 시 불린 숫자 출력
            if(result >= 3) {
                System.out.println(x+1);
                break;
            }
            //빙고 체크 후 다시 리셋해주어야함
            result = 0;
        }
    }

    public static void rowCheck() {
        for(int i=0; i<5; i++){
            int count = 0;
            for(int j=0; j<5; j++){
                if(arr[i][j] == 0) count++;
            }
            if(count == 5) result++;
        }
    }

    public static void colCheck() {
        for(int i=0; i<5; i++){
            int count = 0;
            for(int j=0; j<5; j++){
                if(arr[j][i] == 0) count++;
            }
            if(count == 5) result++;
        }
    }

    public static void diagonalL() {
        int count = 0;
        for(int i=0; i<5; i++) {
            if(arr[i][i] == 0) count++;
        }
        if(count == 5) result++;
    }
    public static void diagonalR() {
        int count = 0;
        for(int i=0; i<5; i++) {
            if(arr[i][4-i] == 0) count++;
        }
        if(count == 5) result++;
    }
}
```

### ⚠️ Point ⚠️

- 빙고체크를 따로 함수로 두어서 체크할 것
- 빙고가 되었을때 `for문`이 종료되어 시간 단축시킬 것