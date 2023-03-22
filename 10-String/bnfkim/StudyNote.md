## 문자열

- **유형 1. 회문(Palindrome)**
    - **앞뒤가 똑같은 단어나 문장**을 의미
    - 문제로는 "앞뒤가 같은 단어를 찾아라.", "회문인 것을 찾아라." 등으로 출제
    - 최근 코딩 테스트는 영어로 코딩 테스트가 출제되고 있다.
- **유형 2. 문자열 뒤집기**
    - 리스트 내부에 있는 문자열을 뒤집는 방법을 물어보는 것
    - 예를 들면 ['a', 'b', 'c']를 ['c', 'b', 'a']로 변환하는 방식을 물어봄
- **유형 3 조건에 맞게 재정렬**
- **유형 4. 특정 단어 추출**
- **유형 5. 애너그램(anagrams)**
    - 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 의미
    - 입력값을 넣었을 때, 알파벳 순서를 바꾸면 같은 값이 되는 것들끼리 묶어서 출력되는 것과 같은 문제
    - 각각의 단어를 sorted()한 값들을 비교하여 같은 단어끼리 묶어주면 됨

## 스트링 관련 자바 메서드

```text
String str = "abcde";

str.length() // str의 길이 반환
str.isEmpty() // str의 길이가 0이면 true, 아니면 false

str.charAt(2) // 인덱스로 문자 찾기, c 반환
str.indexOf("c") // 문자로 첫번째 인덱스 찾기, 2 반환
str.lastIndexOf("c") // 문자의 마지막 인덱스 찾기, 2 반환

str.substring(2, 4) // 2~3 위치의 문자열 "cd" 반환
str.substring(3) // 3부터 끝까지의 문자열 "de" 반환

str.replace('b', 'k') // b를 k로 변경 (akcde)

str.equals("abcde") // str과 abcde를 비교해서 같으면 true, 다르면 false
str.contains("bc") // str에 bc가 포함되어 있으면 true, 아니면 false

str.split(" ") // 띄어쓰기로 구분된 문자열 str을 분리해서 String[] 배열 반환
str.split() // 띄어쓰기 없는 문자열 str을 한 문자씩 분리해서 String[] 배열 반환

str.trim() // str의 앞뒤 공백 제거, 문자열 사이 공백은 제거 X

str.toLowerCase() // 대문자를 모두 소문자로 변경
str.toUpperCase() // 소문자를 모두 대문자로 변경

str.compareTo("abcdd")
/*
str과 abcdd가 같으면 0
str이 abcdd보다 사전순으로 앞이면 -1
str이 abcdd보다 사전순으로 뒤면 1
str과 abcdd가 마지막 문자만 다르면 마지막 문자의 사전순 차이 반환 (여기선 1)
*/

Integer.parseInt("300") // 문자열을 숫자로 변환
Integer.toString(300) // 숫자를 문자열로 변환
```

[[Java] 코딩테스트 문법 속성 정리 (1)](https://velog.io/@hygge/Java-코딩테스트-문법-속성-정리)

# 10798-세로읽기

[10798번: 세로읽기](https://www.acmicpc.net/problem/10798)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * 입력 : 총 다섯줄의 입력
         * 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        char[][] arr = new char[5][15];

        for(int i = 0; i < 5; i++) {
            String s = br.readLine();

            for(int j = 0; j < s.length(); j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        for(int i = 0; i < 15; i++) {
            for(int j = 0; j < 5; j++) {
                if(arr[j][i] != '\0')
                    sb.append(arr[j][i]);
            }
        }

        System.out.println(sb.toString());
    }
}
```

### ⚠️ Point ⚠️

- NULL이 아닐 때를 표현하고 싶다면 **if(arr[j][i] != '\0')**

- 왜 안 될까?

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * 입력 : 총 다섯줄의 입력
         * 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //이차원 배열받아서 출력하기
        String[] arr = new String[5];

        for(int i=0; i<5; i++){
            arr[i] = br.readLine();
        }

        while (sb.length() <= 15){
            for(int i=0; i<15; i++){
                for(int j=0; j<5; j++){
                    if(arr[j].length() > i){
                        sb.append(arr[j].charAt(i));
                    }
                }
            }
        }
        System.out.println(sb.toString());
    }
}
```

---

# 6550-부분문자열

[6550번: 부분 문자열](https://www.acmicpc.net/problem/6550)

```java
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * s가 t의 부분 문자열인지 판단하는 프로그램
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st;
        String str;

        while((str=br.readLine()) != null) {
            st = new StringTokenizer(str);

            String str1 = st.nextToken();
            String str2 = st.nextToken();
            int idx = 0;

            for(int i=0; i<str2.length(); i++){
                if(str1.charAt(idx) == str2.charAt(i)){
                    idx++;
                }
                if (idx == str1.length()) break;
            }

            if (idx == str1.length()) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}
```

### ⚠️ Point ⚠️

- 테스트케이스 수를 안 주는 경우
    - `while((str=br.readLine()) != null)`
- 인덱스를 사용하여 해당 문자열이 포함되어있는지 확인하는게 핵심!

---

# 20291-파일정리

[20291번: 파일 정리](https://www.acmicpc.net/problem/20291)

```java
import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * N : 바탕화면에 있는 파일의 개수
         * 바탕화면에 있는 파일의 이름
         * 파일의 이름은 알파벳 소문자와 점(.)으로만 구성
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new TreeMap<>();
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();
            String key = str.substring(str.indexOf(".")+1);

            if(!map.containsKey(key)) {
                map.put(key, 1);
            } else {
                map.replace(key, map.get(key)+1);
            }
        }
        map.forEach((key, value) -> {
            System.out.println(key + " " + value);
        });
    }
}
```

### ⚠️ Point ⚠️

- TreeMap 사용
    - 넣을때마다 Key 값으로 정렬해주는 Map
- `str.substring(str.indexOf(".")+1);`
    - 특정문자를 기준으로 자를때 사용하는 방식
- map key,value 꺼낼 때 쓰는 방법
    - `map.forEach((key, value) -> {    System.*out*.println(key + " " + value);});`
    - `for(String key : map.keySet()) {    System.*out*.println(key + " " + map.get(key));}`

---

# 17609-회문

[17609번: 회문](https://www.acmicpc.net/problem/17609)

```java
import java.io.*;

public class Main {
    static char[] word;
    static class Position {
        int left;
        int right;
        public Position(int left, int right){
            this.left = left;
            this.right = right;
        }
    }
    public static void main(String[] args) throws IOException {
        /**
         * T : 주어지는 문자열의 개수
         * 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            word = br.readLine().toCharArray();
            Position position = new Position(0, word.length-1);

            if(isPalindrome(position)){
                System.out.println(0);
            } else {
                if(isPalindrome(new Position(position.left+1, position.right))
                        || isPalindrome(new Position(position.left, position.right-1))) {
                    System.out.println(1);
                } else {
                    System.out.println(2);
                }
            }
        }
    }
    static boolean isPalindrome(Position position){
        while (position.left <= position.right) {
           if (word[position.left] == word[position.right]) {
                position.left++;
                position.right--;
            } else {
                return false;
            }
        }
        return true;
    }
}
```

### ⚠️ Point ⚠️

- String 그대로 사용하면 메모리 초과로 실패
    - → 인덱스로 접근하여 메모리를 계속해서 쓰지 않게 하도록 하자

- 메모리초과로 실패

```java
import java.io.*;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * T : 주어지는 문자열의 개수
         * 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i <T; i++) {
            String str = br.readLine();
            System.out.println(isPalindrome(str));
        }
    }

    static int isPalindrome(String str){
        for(int i=0; i<str.length()/2; i++){
            if(str.charAt(i) == str.charAt(str.length()-1-i)){
                continue;
            } else {
                //앞 문자열을 삭제
                if(isPalindrome(str.substring(i+1, str.length()-i)) == 0
                || isPalindrome(str.substring(i,str.length()-1-i)) == 0) {
                    return 1;
                } else {
                    return 2;
                }
            }
        }
        return 0;
    }
}
```