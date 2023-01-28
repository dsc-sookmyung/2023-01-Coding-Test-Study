# BOJ 1620 나는야 포켓몬 마스터 이다솜 
## 풀이과정
> `map` 사용
---
1. `N, M, Map<string, int>, name[]` 선언
2. N만큼 Poketon 입력 받아 map과 배열에 저장
3. M만큼 입력받음   
    3-1. **숫자**라면 name 배열에서 찾아 temp번째 포켓몬 출력   
    3-2. **문자열**이라면 map에서 find로 찾아 인덱스 출력

## map
> 각 노드가 **key와 쌍**으로 이뤄진 중복을 허용하지 않는 트리   
> first-key, second-value로 저장 됨

1. Header   
   `#include <map>`
2. 선언   
   `map<key type, value type> name;`
3. method
    - **begin()**: 첫 번째 원소의 iterator 반환
    - **end()**: 마지막 원소 다음의 반복자를 반환
    - **clear**: 저장하고 있는 모든 원소 삭제
    - **insert()**: 원소 추가
    - **find(key)**: key와 관련된 원소의 반복자를 반환 (찾지 못한 경우 end() 반복자 반환)
    - **size()**: 원소의 개수 반환
    - **erase(key)**: 해당 원소 삭제
    
## 시간 초과
> **`cin, cout`의 문제점**: printf, scanf와 비교했을 때 현저히 느린 속도
        
- 개행문자 사용 시 `endl`보다 `\n` 사용
- cin, cout을 보다 빠르게 사용하고 싶은 경우 아래 소스코드 추가

    ```c++
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.ite(NULL);
    ```

    - `ios_base :: sync_with_stdio(false)`: `cin, cout`은 기본적으로 C의 `stdio.h`와 동기화 되어 있는데, `false`로 설정하여 동기화 해제

  - `.tie(NULL)`: cin과 cout이 연결되어 생기는 플러시 과정(버퍼를 비우는 작업)에서 소요되는 시간을 줄이기 위해 cin과 cout의 상호 연결을 끊어줌

- 주의점
  - scanf, printf와 섞어 사용하지 말 것
  - 싱글 쓰레드 환경에서만 사용할 것    
    
# BOJ 14425 문자열 집합
## 풀이과정
> `map` 사용
---
1. `N, M, map S, result` 선언
2. S 집합 문자열을 N개만큼 받아와 map s 에 저장
3. m개의 문자열을 받아와 find로 s에 존재하면 result++
4. 출력

# BOJ 11279 최대 힙
## 풀이과정
> `priority_queue` 사용
---
1. `N, priority_queue` 선언
2. N만큼 입력을 받아옴   
   2-1. 0이고 큐가 비어있다면 0 출력   
   2-2. 0이고 큐가 비어있지 않으면 q.top 출력 후 pop   
   2-3. 0이 아닌 자연수라면 큐에 push

# BOJ 2075 N번째 큰 수
## 풀이과정
> `priority_queue` 사용   
> `priority_queue`를 그냥 사용할 시 메모리 초과   
---
1. `N, priority_queue(오름차순)` 선언
2. N만큼 입력을 받아옴   
   2-1. 입력 받아옴 → 오름차순으로 자동 정렬   
   2-2. q.size()가 n보다 크면 pop → 가장 작은 수가 pop 됨
3. `2`를 끝내면 n번째로 큰 수가 가장 앞에 있으므로 이를 출력