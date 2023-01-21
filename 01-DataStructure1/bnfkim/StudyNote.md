# **01-DataStructure1**

### 주요 개념들

- 스택
- 큐
- 연결리스트

## 1158-요세푸스 문제

### ⚠️포인트⚠️

- 큐를 링크드리스트처럼 풀도록 함

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); //사람 수
        int K = Integer.parseInt(st.nextToken()); //순서

        Queue<Integer> queue = new LinkedList<>();

        //사람의 수 만큼 원소 넣기
        for(int i=0; i<N; i++){
            queue.offer(i+1);
        }

        sb.append("<");

        while (queue.size() != 1){
            for (int i = 0; i<K-1; i++){
                queue.offer(queue.poll());
            }
            sb.append(queue.poll()).append(", ");
        }

        sb.append(queue.poll()).append(">");
        System.out.println(sb);
    }
}
```

## 1966-프린터큐

### ⚠️포인트⚠️ → 중요도가 높은 걸 맨 앞으로

- 중요도가 높은 문서가 맨 앞에 배치되도록 함
- 큐에서 탐색할 때 처음 poll() 된 원소
    - 가장 큰 경우 → 해당 원소의 첫 위치가 M과 같은지 판단
    - 아닌 경우 → 원소들을 뒤로 보낸 뒤, 다시 첫 원소를 poll 하여 비교

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //테스트 케이스의 수 입력
        int T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken()); //문서의 개수
            int M = Integer.parseInt(st.nextToken()); //궁금한 문서 위치

            //큐 채우기
            LinkedList<int[]> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());

            for(int j=0; j<N; j++){
                //[초기위치, 중요도] 로 정수 배열을 원소로 한 queue 생성
                queue.offer(new int[] {j, Integer.parseInt(st.nextToken())});
            }

            int count = 0; //출력 횟수

            while(!queue.isEmpty()) {
                int[] front = queue.poll(); //첫 번째 원소
                boolean isMax = true;

                //큐에 남아있는 원소들과 중요도 비교
                for(int j=0; j< queue.size(); j++){

                    //처음 뽑은 원소보다 큐에 있는 i번째 원소가 중요도가 더 큰 경우
                    if(front[1] < queue.get(j)[1]){

                        // front 원소가 가장 큰 원소가 아니었으므로 false 하고 탐색 마침
                        isMax = false;
                        break;
                    }
                }

                //isMax == true -> front 가 가장 큰 경우 -> 해당 원소의 첫 위치가 M이랑 같은지 비교
                //isMax == false -> front 원소가 가장 큰 경우가 아닌 경우 -> 반복문 다시 시작
                if(isMax){
                    count++;
                    if(front[0] == M) break;
                } else {
                    //뽑은 원소 및 i 이전의 원소들을 뒤로 보냄
                    queue.offer(front);
                }
            }
            sb.append(count).append("\n");
        }
        System.out.println(sb);
    }
}
```

- 참고사이트

[[백준] 1966번 : 프린터 큐 - JAVA [자바]](https://st-lab.tistory.com/201)

## 9021-괄호

---

### ⚠️포인트⚠️ → 올바른 괄호열인지 판단

- () 짝이 맞을 경우 → pop
- string 문이 끝났을 때
    - 스택이 비어있는 경우 = 짝이 맞다는 것 → True
    - 스택이 비어있지 않는 경우 = 짝이 안 맞다는 것 → False

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();

            for(int j=0; j<str.length(); j++){
                char ch = str.charAt(j);

                if (ch == '(') {
                    stack.push(ch);
                } else {
                    if (stack.empty()){
                        stack.push(ch);
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }
            if(stack.empty()) {
                sb.append("YES").append("\n");
            }
            else {
                sb.append("NO").append("\n");
            }
        }
        System.out.println(sb);
    }
}
```

## 10799-쇠막대기

### ⚠️포인트⚠️ → `)` 가 나왔을때 쇠막대기인지, 레이저인지 구분

- `(` 인 경우 → push 를 통해 stack에 넣음
- `)` 인 경우 → pop 진행
    - 바로 앞 괄호가 `(` 인 경우 → 레이저
        - `(` 수 만큼 막대기가 잘리게됨 → `+스택 사이즈`
    - 바로 앞 괄호가 ) 인 경우 → 쇠막대기
        - 자신의 쇠막대기만 잘리게됨 → `+1`

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int result = 0;
        String input = br.readLine();
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<input.length(); i++) {
            if(input.charAt(i) == '(') {
                stack.push('(');
                continue;
            }
            if(input.charAt(i) == ')') {
                stack.pop();

                if(input.charAt(i-1) == '(') {
                    result += stack.size();
                } else {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
```