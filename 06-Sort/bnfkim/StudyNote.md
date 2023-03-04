# **06-DataStructure6**

### 주제

- 정렬
- 

### 정렬 문제

`Comparator`를 이용해 정렬하는 문제 `Comparator` 사용법을 알고 있어야한다.

```java
Arrays.sort(arr, new Comparator<String[]>(){
	@Override
    public int compare(String[] o1, String[] o2){
    	return Integer.parseInt(o1[1])-Integer.parseInt(o2[1]); // 오름차순 o1,o2
        // return Integer.parseInt(o2[1])-Integer.parseInt(o1[1]); // 내림차순 o2,o1
    }
});
```

1️⃣ **`첫 번째 파라미터의 값`과 `두 번째 파라미터의 값`을 비교하여 `-1`, `0`, `1`을 return 하여 정렬한다**

- o1 < o2 인 경우는 음수를 return
- o1 = o2 인 경우는 0 을 return
- o1 > o2 인 경우는 양수를 return

반환 값이 음수, 0 이면 객체의 자리를 변경하지 않고 `양수이면 객체의 자리를 변경`

⇒ 즉, 변경을 유도하려면 양수값이 나오게 해야함 ! o1 과 o2 의 위치를 적절히 변경하자

2️⃣  **Comparable vs Comparator**

`comparable` 은 정렬 기준이 **일반적일 경우(내림차순) 일때** 사용하지만 `comparator`은 정렬 기준이 **일반적이지 않을 때(문자열의 길이를 비교하여 오름차순, 내림차순으로 정의할 때)** 사용하는 경우가 많다.

[[알고리즘 문제 풀이 스킬] 자바 에서 Comparator, Comparable 로 정렬 기준 바꾸기 (람다를 이용해서 깔끔하게 재정의하기)](https://wonit.tistory.com/143?category=743304)

# 10814 : 국영수

[10825번: 국영수](https://www.acmicpc.net/problem/10825)

```java
import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 도영이네 반의 학생 수
         * 학생 이름, 국어, 영어, 수학 점수
         * 국어점수 감소 > 영어 점수 증가 > 수학 점수 감소 > 사전 순 이름
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        //학생 정보 입력
        String[][] arr = new String[N][4];
        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr[i][0] = st.nextToken();
            arr[i][1] = st.nextToken();
            arr[i][2] = st.nextToken();
            arr[i][3] = st.nextToken();
        }

        //정렬하기
        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(o2[1].equals(o1[1])){ //국어점수가 같으면
                    if(o1[2].equals(o2[2])){ //영어점수가 같으면
                        if(o1[3].equals(o2[3])) { //수학점수가 같으면
                            //compareTo -> 문자열의 아스키값을 기준으로 비교
                            //앞의 데이터의 앞 문자열과, 뒤의 데이터 앞 문자열의 아스키 차이값 반환
                            return o1[0].compareTo(o2[0]);
                        }
                        return Integer.parseInt(o2[3]) - Integer.parseInt(o1[3]);
                    }
                    return Integer.parseInt(o1[2])-Integer.parseInt(o2[2]);
                }
                return Integer.parseInt(o2[1])- Integer.parseInt(o1[1]);
            }
        });

        for(int i=0; i<arr.length; i++) {
            System.out.println(arr[i][0]);
        }
    }

}
```

### ⚠️ Point ⚠️

- 점수가 감소하는 순서 (내림차순)
    - o2 - o1
- 점수가 증가하는 순서 (오름차순)
    - o1 - o2
- `compareTo` 함수 이용
    - 맨 마지막 조건인 ‘**이름이 사전 순으로 증가하는 순서**’ 에 대해서 문자열 비교인 `compareTo` 를 이용한다

- 참고문헌

[[JAVA] 자바_compareTo ( 값 [문자열/숫자] 비교 )](https://mine-it-record.tistory.com/133)

# 10814 : 나이순정렬

[10814번: 나이순 정렬](https://www.acmicpc.net/problem/10814)

```java
import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 온라인 저지 회원 수
         * 나이, 이름
         * 나이가 같으면 가입한 순으로 정렬
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String[][] arr = new String[N][2];

        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = st.nextToken(); //나이
            arr[i][1] = st.nextToken(); //이름
        }

        //정렬하기
        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                return Integer.parseInt(o1[0])- Integer.parseInt(o2[0]);
            }
        });
        //출력하기
        for(int i=0; i<N; i++){
            sb.append(arr[i][0] + " " + arr[i][1]).append("\n");
        }
        System.out.println(sb);
    }
}
```

### ⚠️ Point ⚠️

- Arrays.sort()에 Comparator 의 compare 를 이용하는 가장 기본적인 방법!
- 추가로 해결 가능한 다른 방법
    - 배열에 넣지 않고 클래스 객체를 만들어 사용

        ```java
        public static void main(String[] args) {
        	Person[] p = new Paerson[size];
        }
         
        public static class Person {
        	int age;
        	String name;
            
        	public Person(int age, String name) {
        		this.age = age;
        		this.name = name;
        	}
        }
        ```

        ```java
        // 타입을 Person 으로 둘 것.
        		Arrays.sort(p, new Comparator<Person>() {
        			// 나이순으로 정렬
        			@Override
        			public int compare(Person s1, Person s2) {
        				return s1.age - s2.age;
        			}
        			
        		});
        ```


# 11652 : 카드

[11652번: 카드](https://www.acmicpc.net/problem/11652)

```java
import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 준규가 가지고 있는 수자 카드의 개수
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();

        int max = 0;
        long result = 0;

        //갯수가 가장 많은 경우를 해야하므로 map 사용
        for(int i=0; i<N; i++) {
            Long num = Long.parseLong(br.readLine());
            map.put(num, map.getOrDefault(num, 0)+1);

            if(map.get(num) > max) {
                max = map.get(num);
                result = num;
            } else if (map.get(num) == max) {
                //만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력
                result = Math.min(result, num);

            }
        }
        System.out.println(result);
    }
}
```

### ⚠️ Point ⚠️

- 갯수로 가져갈 것이기 때문에 map 사용해서 key 와 value 활용 !
- num은 범위
    - 2^-62~2^62 이므로 `Long`
- `getOrDefault`
    - 키 존재 → 키의 값을 반환, 키 없음 → 기본 값을 반환하는 메서드

# 18870 : 좌표압축

[18870번: 좌표 압축](https://www.acmicpc.net/problem/18870)

```java
import org.w3c.dom.Node;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N -> 좌표의 개수
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] originArr = new int[N];
        int[] sortedArr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        //입력받기
        for(int i=0; i<N; i++) {
            sortedArr[i] = originArr[i] = Integer.parseInt(st.nextToken());
        }

        //정렬하기
        Arrays.sort(sortedArr);

        //맵에 넣어주기
        int rank = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int value : sortedArr) {
            //앞선 원소가 이미 순위가 매겼을 시 중복되지 않게 처리
            if(!map.containsKey(value)) {
                map.put(value, rank);
                rank++;
            }
        }

        //출력하기
        for(int value : originArr) {
            sb.append(map.get(value)).append(" ");
        }
        System.out.println(sb);
    }
}
```

### ⚠️ Point ⚠️

- 압축 관련 알고리즘을 풀이
- map에 원소를 넣을 때, 무작정 넣는 것이 아닌, **반드시 `map에 똑같은 원소가 들어있지 않을 경우`** 에만 원소와 rank값을 넣어주어야 하는 것을 잊지말기

알고리즘 이해 자체가 어려워 이해는 아래 사이트 참고했다