# **09-DataStructure9**

## 동적계획법 DP (dynamic programming)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c448c19-d837-4b40-a046-b833a2bbfaf0/Untitled.png)

- 의미
    - 특정 범위까지의 값을 구하기 위해, 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘
    - 구체적인 알고리즘이라기보다는 문제해결 패러다임에 가깝다.
    - 과거에 구한 해를 활용하는 방식의 알고리즘
    - 최적 부분 구조(Optimal Substructure)
        - 답을 구하기 위해서 했던 계산을 또 하고 또 하고 계속해야 하는 종류
- 구현
    - 기본적으로 분할 정복 알고리즘과 비슷 → 원래의 문제를 부분 문제로 나누는 방식에 차이 존재
    - 주어진 문제를 나눌 때 부분 문제를 최대한 많이 이용하도록 나눈 다음, 주어진 부분 문제의 정답을 한 번만 계산하고 저장해 둔 뒤 다시 한 번 이 부분 문제를 이용할 때에는 저장해둔 정답을 바로 산출하여 이용함으로써 속도를 향상
- 방법
    - 1. 테이블 정의
    - 2. 점화식 찾기
    - 3. 초기값 정하기

# 1149-RGB거리

[1149번: RGB거리](https://www.acmicpc.net/problem/1149)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 집의 가지수
         * 각 집을 빨강, 초록, 파랑으로 칠하는 비용 입력
         * 모든 집을 칠하는 비용의 최솟값 구하기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[][] house;
        int[][] dp;

        //입력값 받기
        int N = Integer.parseInt(br.readLine());
        house = new int[N+1][3];
        dp = new int[N+1][3];

        for(int i=1; i<N+1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            house[i][0] = Integer.parseInt(st.nextToken()); //빨강색 비용
            house[i][1] = Integer.parseInt(st.nextToken()); //초록색 비용
            house[i][2] = Integer.parseInt(st.nextToken()); //파랑색 비용
        }

        //초기값 설정
        dp[1][0] = house[1][0];
        dp[1][1] = house[1][1];
        dp[1][2] = house[1][2];

        for(int i=2; i<N+1; i++){
            //빨간색의 경우
            dp[i][0] = Math.min(dp[i-1][1] , dp[i-1][2]) + house[i][0];
            //초록색의 경우
            dp[i][1] = Math.min(dp[i-1][0] , dp[i-1][2]) + house[i][1];
            //파란색의 경우
            dp[i][2] = Math.min(dp[i-1][0] , dp[i-1][1]) + house[i][2];
        }
        int temp = Math.min(dp[N][0], dp[N][1]);
        System.out.println(Math.min(temp, dp[N][2]));
    }
}
```

### ⚠️ Point ⚠️

- 9465 스티커 문제와 비슷하다
- 뒤에서 더하는 전개식을 이용하면 된다
- 고정되어 있는 빨강, 초록, 파랑은 하나씩 식을 세워서 풀이한다

---

# 2156-포도주시식

[2156번: 포도주 시식](https://www.acmicpc.net/problem/2156)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * n -> 포도주 잔의 개수
         * 3잔 연속에서 먹을 수 없음
         * 즉, 두가지 방법으로 나뉨
         * (1) 전 와인을 먹고 현재 와인을 먹기
         * (2) 전전 와인을 먹고 현재 와인을 먹기
         * ! 현재 와인을 먹지 않는 경우도 생각해야함
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] wine;
        int[] dp;

        //입력값 받기
        int n = Integer.parseInt(br.readLine());

        wine = new int[n+1];
        dp = new int[n+1];

        for(int i=1; i<n+1; i++){
            wine[i] = Integer.parseInt(br.readLine());
        }

        //초기값 설정
        dp[1] = wine[1];

        // n=1 의 경우를 대비하여 예외처리를 해주어야 한다
        if(n>1) dp[2] = wine[1] + wine[2];

        for(int i=3; i<n+1; i++) {
            // (현재와인 선택 안 한 경우) vs (지금까지 먹은 와인 + 전와인과 현재 와인을 먹은 경우)
            dp[i] = Math.max(dp[i-1], Math.max(dp[i-2], dp[i-3] + wine[i-1]) + wine[i]);
        }

        System.out.println(dp[n]);

        /**
         * wine 6  10  13   9  8  1
         * dp   6  16  23  28 33 33
         */
    }
}
```

### ⚠️ Point ⚠️

- n=1 의 경우를 대비하여 예외처리
    - `if(n>1) dp[2] = wine[1] + wine[2];`
    - 안 했더니 `ArrayIndexOutOfBounds` 발생 …
- 어렵다 … 풀이를 봐도 잘 이해가 되지 않는 문제 및 풀이방법이다
- 우선 3잔 연속 먹지 못 한다는 조건에 집중
    - 와인 ‘3잔’을 기준으로 나눠 생각하기
    - 와인을 먹는 방법을 나눠 생각하기
        - *`(1) 전 와인을 먹고 현재 와인을 먹기`*
        - *`(2) 전전 와인을 먹고 현재 와인을 먹기`*

- 참고한 사이트

[[백준 - Java] 2156번 : 포도주 시식](https://minhamina.tistory.com/155)

---

# 1563-1로만들기

[1463번: 1로 만들기](https://www.acmicpc.net/problem/1463)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    //메모제이션 배열
    static Integer[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        dp = new Integer[N+1];
        dp[0] = dp[1] = 0;

        System.out.println(recur(N));
    }

    static int recur(int N) {
        if (dp[N] == null){
            if (N % 6 == 0){ //3으로 나누는 경우, 2로 나누는 경우, 1을 빼는 경우 중
                // 3)) + 1;
            } else if(N % 2 == 0){ //2로 나누는 경우, 1을 빼는 경우를 최솟갑스로 나눠 dp갱신
                dp[N] = Math.min(recur(N-1), recur(N/2)) + 1;
            } else {
                dp[N] = recur(N-1) + 1;
            }
        }
        return dp[N];
    }
}
```

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 1보다 크거나 같고, 106보다 작거나 같은 정수
         * (1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
         * (2) X가 2로 나누어 떨어지면, 2로 나눈다.
         * (3) 1을 뺀다.
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N+1];
        dp[0] = dp[1] = 0;

        for(int i=2; i<N+1; i++){
            dp[i] = dp[i-1] + 1; //먼저 1을 빼주기
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1); // 1을 뺀 값과 2로 나눈 값 중 최솟값을 dp[i]에 저장한다
            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1); // 1을 뺀 값과 2로 나눈 값 중 최소값인 dp[i] 와 3으로 나눈 값 중 최솟값을 dp[i]에 저장한다
        }
        System.out.println(dp[N]);
    }
}
```

### ⚠️ Point ⚠️

- 두 가지 방법으로 가능
    - 입력받은 N 을 숫자로 나눠서 탑다운 방식으로 하는 것
    - 나누는 값으로 바텀업 방식으로 하는 것
        - 이 방법이 우리가 했던 dp[] 를 이용하는 방식과 비슷하다
        - 이 방법이 메모리나 시간이 더 유리하다

---

# 12865-평범한배낭

[12865번: 평범한 배낭](https://www.acmicpc.net/problem/12865)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 물품의 수
         * K -> 준서가 버틸 수 있는 무게
         * W -> 각 물건의 무게
         * V -> 해당 물건의 가치
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] W = new int[N+1]; //무게
        int[] V = new int[N+1]; //가치
        int[] dp = new int[K+1];

        for(int i=1; i<N+1; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        /**
         * 가방 최대 무게를 넘기면 안 됨
         * 가방 최대 무게를 넘기지 않는 선에서, 물건의 가치합의 최댓값을 출력해야함
         *
         * W -> 6   4   3   5
         * V -> 13  8   6   12
         */

        /**
         * 다른 방법
         *             dp[][] = new int[N+1][K+1] 을 사용할경우
         *             for(int j=1; i<K+1; j++){
         *                 // i번째 무게를 더 담을 수 없는 경우
         *                 if (W[i] > j) {
         *                     dp[i][j] = dp[i-1][j];
         *                 } else { // i번째 무게를 더 담을 수 있는 경우
         *                     dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j - W[i]] + V[i]);
         *                 }
         *             }
         */

        for(int i=1; i<N+1; i++) {
            for(int j=K; j-W[i] >= 0; j--){
                dp[j] = Math.max(dp[j], dp[j - W[i]] + V[i]);
            }
        }
        System.out.println(dp[K]);
    }
}
```

### ⚠️ Point ⚠️

- 바텀-업 방법으로 해결하는 것이 오히려 단순할 수 있음
- 최대 가능한 무게에서 가방 무게를 하나씩 없애서 비교함

- 참고사이트