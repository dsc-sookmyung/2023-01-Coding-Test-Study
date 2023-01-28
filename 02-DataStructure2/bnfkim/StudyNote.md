# **02-DataStructure2**

# 1620번 : 나는야 포켓몬 마스터 이다솜

[1620번: 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        /**
         * 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N
         * 내가 맞춰야 하는 문제의 개수 M
         *
         * 알파벳으로만 들어오면 -> 포켓몬 번호 출력
         * 숫자로만 들어오면 -> 포켓몬 번호에 해당하는 문자를 출력
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> bookMap = new HashMap<>();
        String[] bookArr = new String[N+1];

        for(int i=1; i<N+1; i++){
            String name = br.readLine();
            bookMap.put(name, i); //이름 -> 번호 찾는 용
            bookArr[i] = name; //번호 -> 이름 찾는 용
        }

        while(M --> 0) {
            String question = br.readLine();
            // 숫자를 입력받은 경우
            if (isNumeric(question)) {
                sb.append(bookArr[Integer.parseInt(question)]);
            } else {
                sb.append(bookMap.get(question));
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    //문자열이 숫자인지 아닌지 판단하는 함수
    public static boolean isNumeric(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
```

### ⚠️ Point ⚠️

- 문자열이 숫자형태인지 아닌지 어떻게 판단할 것인지 ?
    - 문자열 → 숫자형 으로 바꿀때 아닌 경우는, 에러를 발생시킴
    - 그 에러를 잡아서, 에러가 발생한 경우/아닌 경우 로 나눠서 결과를 내줘야 함
    - 즉, 에러발생 시 → 숫자 형태가 아닌 것, 에러 미발생 시 → 숫자형태인 것

# 14425 문자열 집합

[14425번: 문자열 집합](https://www.acmicpc.net/problem/14425)

```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            map.put(br.readLine(), 0);
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            if (map.containsKey(br.readLine())) count++;
        }
        System.out.print(count);
    }
}
```

### ⚠️ Point ⚠️

- HashMap 사용하면 쉽게 풀이 가능

# 11279 최대힙

[11279번: 최대 힙](https://www.acmicpc.net/problem/11279)

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

- 자바에 있는 라이브러리 사용! → `PriorityQueue`
    - `add` 와 `poll` 모두 `O(log n)`으로 `O(nlogn)` 만에 해결 가능
- `Collections.reverseOrder()` 사용 → 내림차순

# 14425 문자열 집합

[2075번: N번째 큰 수](https://www.acmicpc.net/problem/2075)

```java
import java.util.*;
import java.io.*;

// https://www.acmicpc.net/problem/2075

class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[n*n];
        int index =0;

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                arr[index++] = Integer.parseInt(st.nextToken());
            }
        }

        Arrays.sort(arr);

        System.out.println(arr[n*n - n]);
    }
}
```

### ⚠️ Point ⚠️

- `표` 라고 생각하지 말고 `배열` 이라고 생각할 것
- 배열로 숫자를 쭉 둔 후, `정렬`하기