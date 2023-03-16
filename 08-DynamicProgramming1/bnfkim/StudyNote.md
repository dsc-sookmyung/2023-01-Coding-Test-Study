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

# 2023 - **2×n 타일링**

```java

```

### ⚠️ Point ⚠️

- 일정한 패턴이 반복되는 것을 확인
    - 세로가 2로 고정되어있어, 이전 계산에 하나씩 더 붙는 것을 확인할 수 있음
- mod 연산 결과값 출력 시 신경쓰기
    - 반드시 연산할 때마다 mod 연산을 해주어야 한다. 계속 숫자를 더하고 마지막 출력시에만 mod연산을 해줄 경우 Integer.MAX_VALUE
      를 넘어 **Overflow** 가 발생.

---

# 11055 - 가장 큰 증가하는 부분 수열

[11055번: 가장 큰 증가하는 부분 수열](https://www.acmicpc.net/problem/11055)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 수열 A의 크기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //입력값 받기
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N+1];
        int[] dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=1; i<N+1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        //각 원소의 가장 큰 증가 부분 수열 합
        int result = dp[1] = arr[1];
        for(int i=2; i<N+1; i++){
            dp[i] = arr[i];
            //dp[2] = 101, dp[3] = 3, dp[4] = 53, dp[5] = 113 ....
            for(int j=1; j<i; j++){
                //증가하는 부분 수열을 만들기 위해 필요한 조건식
                if(arr[i] > arr[j]){
                    //dp 에 이전 수열들이 저장되어있음. 하나씩 더하면서 dp를 그자리에서 업데이트
                    //기존 dp[i]를 비교했을때, 더 큰 값만 업데이트 되도록함
                    dp[i] = Math.max(dp[i], arr[i] + dp[j]);
                }
            }
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);
    }
}
```

### ⚠️ Point ⚠️

- dp에는 각 원소를 더한 값 중 가장 큰 합
- Math.max() 를 통해서, 현재의 값과 새로 더한 값 중 더 큰 값만 업데이트 되도록 해야함

# 9465 - 스티커

[9465번: 스티커](https://www.acmicpc.net/problem/9465)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 수열 A의 크기
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[][] arr;
        int[][] dp;

        //입력값 받기
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 수

        for(int k=0; k<T; k++){
            int n = Integer.parseInt(br.readLine()); //스티커 행의 수

            arr = new int[2][n+1];
            dp = new int[2][n+1];

            //입력받기
            for(int i=0; i<2; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j=1; j<n+1; j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            //초기값 설정
            dp[0][1] = arr[0][1];
            dp[1][1] = arr[1][1];

            for(int i=2; i<n+1; i++){
                dp[0][i] = Math.max(dp[1][i-1], dp[1][i-2]) + arr[0][i];
                dp[1][i] = Math.max(dp[0][i-1], dp[0][i-2]) + arr[1][i];
                // 밑과 같이 전개됨
                // 50 40  200 140 250
                // 30 100 120 210 260
            }
            System.out.println(Math.max(dp[0][n], dp[1][n]));
        }
    }
}
```

### ⚠️ Point ⚠️

- 더해서 앞 dp 를 채우는 것만 생각하는 것만 아니라, 뒤 값을 더해서 현재 값을 업데이트 하는 것도 생각할 줄 알아야한다
- 특정 n번 째 dp값을 채우기 위해선, 한 칸 또는 두 칸 뒤의 대각선을 고려할 것 !
- 핵심 포인트
    - **dp [0][j] = Math.max(dp [1][j-1] , dp [1][j-2]) + cost [0][j]**
    - **dp [1][j] = Math.max(dp [0][j-1] , dp [0][j-2]) + cost [1][j]**

---

# 9084 - 동전

[9084번: 동전](https://www.acmicpc.net/problem/9084)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * T -> 테스트 케이스
         * N -> 동전의 가지수
         * M -> 주어진 N가지 동전으로 만들어야 할 금액
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] coins;
        int[] dp;

        //입력값 받기
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 수

        while(T-->0){
            int N = Integer.parseInt(br.readLine()); //동전의 가지수
            coins = new int[N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i=0; i<N; i++){
                coins[i] = Integer.parseInt(st.nextToken());
            }

            /**
             * {2,3,5}
             *            0  1  2  3  4  5  6  7  8  9  10
             * (2) dp ->  1  0  1  0  1  0  1  0  1  0  1
             * (3) dp ->  1  0  0  1  1  1  2  1  2  2  2
             * (5) dp ->  1  0  1  1  1  2  2  2  3  3  4
             *
             * => 총 네가지 방법
             */

            int M = Integer.parseInt(br.readLine());
            dp = new int[M+1];
            dp[0] = 1;
            for(int coin : coins) {
                for(int j = coin; j<M+1; j++){
                    dp[j] = dp[j] + dp[j - coin];
                }
            }
            System.out.println(dp[M]);
        }
    }
}
```

### ⚠️ Point ⚠️

- 이해가 안 되면 … dp는 일단 진짜 스스로 규칙성을 찾을 때까지 그냥 다 써보는게 나을 듯 하다

이해 자체가 어려워서 아래 사이트 참고

[[백준] 9084. 동전](https://ddb8036631.github.io/boj/9084_동전/)