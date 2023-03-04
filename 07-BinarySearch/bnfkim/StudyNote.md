### 주제

- 이분탐색

# 1789 : 수들의합

[1789번: 수들의 합](http://acmicpc.net/problem/1789)

```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 서로 다른 자연수의 개수
         * S -> 자연수의 합
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());
        System.out.println(Search(S));
    }
    public static int Search(long S){
        int count = 0;
        long sum = 0L;
        int i = 0;

        while(true) {
            sum += ++i;
            if(sum > S) return count;
            count++;
        }
    }
}
```

### ⚠️ Point ⚠️

- S의 범위 신경쓰기
    - S의 범위가 int 형 범위를 벗어나므로 long으로 선언.
    - S를 입력 받을 때도, Long.parseLong 을 사용!

# 2512-예산

[2512번: 예산](https://www.acmicpc.net/problem/2512)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int left=0, right=-1;
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, arr[i]);
        }

        int m = Integer.parseInt(br.readLine());
        while(left<=right) {
            int mid = (left+right)/2;
            long budget =0;
            for(int i=0; i<n; i++) {
                if(arr[i]>mid) budget += mid;
                else budget+= arr[i];
            }
            if(budget<=m) {
                left = mid+1;
            }else {
                right = mid-1;
            }
        }
        System.out.println(right);
    }
}
```

### ⚠️ Point ⚠️

- left~right범위 안에서 파라메트릭 서치를 통해 K를 찾기
    - 상한액(mid)으로 얻을 수 있는 예산을 budget 이라 함
    - budget <= m, 예산이 아직 총량에 도달하지 못했으므로 left = mid+1;
    - budget > m, 예산이 초과되었으므로 right = mid -1;

# 1654 : 랜선자르기

[1654번: 랜선 자르기](https://www.acmicpc.net/problem/1654)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] arr = new int[K];

        long max = 0;

        // 입력과 동시에 해당 랜선의 길이가 최댓값인지를 확인하고 max를 갱신
        for (int i = 0; i < K; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            if(max < arr[i]) {
                max = arr[i];
            }
        }

        max++;

        long min = 0;
        long mid = 0;

        while (min < max) {

            mid = (max + min) / 2;
            long count = 0;

            for (int i = 0; i < arr.length; i++) {
                count += (arr[i] / mid);
            }
            if(count < N) {
                max = mid;
            }
            else {
                min = mid + 1;
            }
        }
        System.out.println(min - 1);
    }
}
```

### ⚠️ Point ⚠️

- **이분 탐색의 범위는 인덱스가 아닌 랜선의 길이를 의미**
- 특**정 개수에 대한 특정 길이를 찾고자 한다** 는 것

# 22871-징검다리건너기

[22871번: 징검다리 건너기 (large)](https://www.acmicpc.net/problem/22871)

```java
import java.io.*;
import java.util.*;

public class Main {
    static int n,k=0;
    static long[] arr, dp;
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        arr = new long[n];
        dp = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i =0;i<n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
            dp[i] = -1;
        }
        System.out.println(jump(0));

    }
    public static long jump(int x){
        if (x==n-1) return 0;
        if (dp[x] != -1) {
            return dp[x];
        }
        dp[x] = Long.MAX_VALUE;

        for(int i=x+1;i<n;i++){
            dp[x] = Math.min(dp[x], Math.max(go(i),(i-x)*(1+Math.abs(arr[x]-arr[i]))));
        }
        return dp[x];
    }
}

```

### ⚠️ Point ⚠️

시간 부족과 어려워서 참고

[백준 22871 징검다리 건너기(large) java 자바 - jimoo](https://jimoo-vision.tistory.com/29)