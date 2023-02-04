# **03-DataStructure3**

DP

# 14916번 : 거스름돈

[14916번: 거스름돈](https://www.acmicpc.net/problem/14916)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * [dp]
         * 2원 짜리와 5원짜리로만 거스름돈
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int count = 0;

        while(n>0) {
            //5로 나뉘는 경우
            if (n%5 == 0) {
                count = n/5 + count;
                break;
            }

            //5로 나뉘지 않으면 2씩 빼기
            n = n-2;
            count++;
        }
        if (n < 0) {
            System.out.println(-1);
        } else {
            System.out.println(count);
        }
    }
}
```

### ⚠️ Point ⚠️

- DP 가 어려우면 구현으로 풀기!
    - dp 방법으로 생각하다가 오히려 꼬여버려서 구현 방식으로 품
    - 가볍게 풀 수 있는 문제면 가볍게 풀기

# 2217번 : 로프

[2217번: 로프](https://www.acmicpc.net/problem/2217)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * 첫째 줄에 정수 N이 주어진다.
         * 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];

        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        //최대 중량이 제일 큰 로프순으로 써내서, 순서대로 병렬로 연결
        Arrays.sort(arr);
        int result = 0;

        for(int i=N-1; i>=0; i--){
            arr[i] = arr[i] * (N-i);
            if(result < arr[i]) {
                result = arr[i];
            }
        }
        System.out.println(result);

    }
}
```

### ⚠️ Point ⚠️

- 최대 중량이 제일 큰 로프순으로 꺼내서 순서대로 병렬로 연결하는게 포인트

# 11508 : 2+1세일

[11508번: 2+1 세일](https://www.acmicpc.net/problem/11508)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0)
                sb.append(queue.size() == 0 ? 0 : queue.poll()).append('\n');
            else queue.add(num);
        }
        System.out.println(sb.toString());
    }
}
```

### ⚠️ Point ⚠️

- 최소 비용을 구하기 위해서는 뺄 수 있는 값 중에 가장 큰 값을 빼는 것이 유리
    - 유제품들의 가격을 내림차순으로 정렬한 뒤 3개 씩 묶어서 가장 작은 값을 빼주면 된다

# 13305 : 주유소

[13305번: 주유소](https://www.acmicpc.net/problem/13305)

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        long[] dist = new long[N - 1];	// 거리
        long[] cost = new long[N];	// 비용

        // 거리 입력
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < N - 1; i++) {
            dist[i] = Long.parseLong(st.nextToken());
        }

        // 리터당 기름값 입력
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < N; i++) {
            cost[i] = Long.parseLong(st.nextToken());
        }

        long sum = 0;
        long minCost = cost[0];	// 이전 까지의 과정 중 주유 최소 비용

        for(int i = 0; i < N - 1; i++) {

            /*
             *  현재 주유소가 이전 주유소의 기름값보다 쌀 경우
             *  minCost를 갱신해준다.
             */
            if(cost[i] < minCost) {
                minCost = cost[i];
            }

            sum += (minCost * dist[i]);
        }

        System.out.println(sum);

    }
}
```

### ⚠️ Point ⚠️

- 리터당 기름 값이 **'내림차순'일 경우에 주유**