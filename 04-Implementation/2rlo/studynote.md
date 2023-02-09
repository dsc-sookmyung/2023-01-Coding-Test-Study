# 완전 탐색
> 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법   
> `Brute-Force`라고도 부름   
> 가능한 경우의 수가 많은 경우에는 이용하기 어려우므로 잘 파악하는 것이 중요

</br>

## 완전 탐색 기법
1. 단순 Brute-Force
     - 어느 기법을 사용하지 않고 단순히 for문과 if문 등으로 모든 case들을 만들어 답을 구하는 방법
2. 비트마스크 (Bitmask)
     - 2진수를 이용하는 컴퓨터의 연산을 이용하는 방법
     - 문제에서 나올 수 있는 모든 경우의 수가 `각각의 원소가 포함되거나, 포함되지 않는 두 가지 선택`으로 구성되는 경우에 유용함
3. 재귀 함수
      - 재귀함수를 통해서 문제를 만족하는 경우를 만들어 냄
      - 비트마스크와 마찬가지로 주로 각 원소가 포함되거나 포함되지 않는 두 가지 선택을 가질 때 이용
4. 순열 (Permutation)
      - 순열에 원소를 하나씩 채워가는 방식
      - 재귀 함수를 이용하거나 `C++`에서는 `next_permutation` 함수 사용
5. BFS / DFS
      - 대표적인 유형으로는 길 찾기 문제

</br>

## 사용 예시
1. 입력으로 주어지는 데이터의 크기가 매우 작을 때
2. 답의 범위가 작고, 임의의 답을 하나 선택했을 때 문제 조건을 만족하는지 역추적 가능할 때
3. 여러 문제 조건 중 한 조건을 고정시키면 문제 풀이가 간단해 질 때

</br>

---

</br>

# BOJ 21918 전구
## 문제 요약
1. 입력: 전구의 개수 `N`, 입력되는 명령어의 개수 `M`, N개의 전구의 현재 상태 `s(1 or 0)` 세 개의 정수 `a(a번째 명령어), b(a가 1인 경우 i 아니면 l), c(a가 1인 경우 x, 아니면 r)`
2. 제어 명령어 4개
   - i번째 전구의 상태를 x로 변경
   - l번째부터 r번째까지의 전구의 상태 변경
   - l번째부터 r번째까지 전구를 끔
   - l번째부터 r번째까지 전구를 킴
3. 출력: 모든 명령어를 수행한 후 전구의 상태

</br>

## 풀이과정
1. 명령어 1일 경우: s[b] = c
2. 명령어 2일 경우: (b부터 c까지) s[i] = !s[i]
3. 명령어 3일 경우: (b부터 c까지) s[i] = 0
4. 명령어 4일 경우: (b부터 c까지) s[i] = 1

</br>

## 코드
```cpp
// BOJ 21918 전구

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    int s[4001] = {
        0,
    };

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        cin >> s[i];
    }

    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 1)
        {
            s[b] = c;
        }
        else if (a == 2)
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = !s[i];
            }
        }
        else if (a == 3)
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = 0;
            }
        }
        else
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = 1;
            }
        }
    }

    for (int i = 1; i <= N; i++)
        cout << s[i] << ' ';

    return 0;
}
```

</br>

---

</br>

# BOJ 2798 블랙잭
## 문제 요약
1. 입력: 카드의 개수 `N, M`, 카드에 쓰여 있는 수
2. 출력: M을 넘지 않으면서 `M에 최대한 가까운 카드 3장의 합`

</br>

## 풀이과정
1. 입력을 받고 3중 for문으로 모두 더해보기
2. sum이 M을 넘지않고 max보다 작으면 max를 갱신

</br>

## 코드
```cpp
// BOJ 2798 블랙잭

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, sum = 0, max = 0;
    int num[101];

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        cin >> num[i];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                sum = num[i] + num[j] + num[k];
                if (sum <= M)
                {
                    if (sum > max)
                        max = sum;
                }
            }
        }
    }

    cout << max << "\n";
    
    return 0;
}
```

</br>

# BOJ 14467 소가 길을 건너간 이유 1
## 문제 요약
1. 입력: 관찰 횟수 `N (<=100)`, `관찰 결과 (소의 번호와 위치)`
2. 출력: 소가 길을 건너간 `최소 횟수`

</br>

## 풀이과정
1. 배열을 -1로 초기화하여 -1이라면 번호와 위치를 저장만 함
2. 아니라면 `cow[num]`과 `loc`를 `XOR` 연산하여 true면 `res++`

</br>

## 코드
```cpp
// BOJ 14467 소가 길을 건너간 이유 1

#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, num, loc, res = 0;
    int cow[11];

    memset(cow, -1, 11*sizeof(int));

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> num >> loc;
        if (cow[num] != -1){
            if(cow[num] ^ loc) res++;
        }
        cow[num] = loc;
    }

    cout << res << "\n";

    return 0;
}
```
---

</br>

# BOJ 2578 빙고
## 문제 요약
1. 입력: `빙고판에 쓰여진 수`와 `사회자가 부르는 수`
2. 선이 세 개 이상 그어지는 순간 "빙고"를 외침
3. 출력: 사회자가 `몇 번째 수`를 부른 후 "빙고"를 외치는지

</br>

## 풀이과정
> 변수 초기화에 유의하기
1. 가로 세로 대각선 체크해서 `3줄 이상이면 true 반환`하는 `check` 함수 작성
2. `num 배열`에 수 저장
3. 부르는 숫자 입력 받고 배열에서 찾은 뒤 0으로 값을 바꾸고 `check()`
4. `true`이면 res 출력 후 종료

</br>

## 코드 
```cpp
// BOJ 2578 빙고

#include <iostream>
using namespace std;

int num[6][6];

bool check()
{
    int bingo = 0, crossR = 0, crossL = 0;
    for (int i = 1; i <= 5; i++)
    {
        int col = 0, row = 0;
        for (int j = 1; j <= 5; j++)
        {
            if (num[i][j] == 0)
                row++;
            if (num[j][i] == 0)
                col++;
        }
        if (row == 5)
            bingo++;
        if (col == 5)
            bingo++;
        if (num[i][i] == 0)
            crossR++;
        if (num[i][6 - i] == 0)
            crossL++;
    }

    if (crossR == 5)
        bingo++;
    if (crossL == 5)
        bingo++;
    if (bingo >= 3)
        return true;
    return false;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int call, res = 0;

    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            cin >> num[i][j];
        }
    }

    for (int i = 1; i <= 25; i++)
    {
        res++;
        cin >> call;
        for (int j = 1; j <= 5; j++)
        {
            for (int k = 1; k <= 5; k++)
            {
                if (num[j][k] == call)
                {
                    num[j][k] = 0;
                    if (check())
                    {
                        cout << res << "\n";
                        return 0;
                    }
                }
            }
        }
    }

    return 0;
}
```
---

</br>

# BOJ 20436 ZOAC 3
## 문제 요악
1. 입력: 두 알파벳 소문자 $S_L, S_R$ (왼손 검지, 오른손 검지의 처음 위치), 알파벳 소문자로 구성된 `문자열`
2. 한글 자음 쪽 자판은 왼손 검지로, 모음 쪽 자판은 오른손 검지로
3. 이동하는 데 걸리는 시간은 $|x_1-x_2|+|y_1-y_2|$
4. 각 키를 누르는 데에는 `1`의 시간이 걸림
5. 두 손을 동시에 움직일 수 없음
6. 출력: 입력으로 주어진 문자열을 출력하는 데에 걸리는 시간의 `최솟값`

</br>

## 풀이 과정
1. 알파벳 위치를 `arr` 배열에 저장
2. 왼쪽과 오른쪽을 구분하기 위해 한글 자음 쪽 자판을 `vector`에 저장
3. 입력을 받고, s[i]번째 문자를 vector에서 찾을 수 있으면 왼쪽 자판이므로 l로 계산하고 `res++, l=s[i]`
4. 찾을 수 없으면 오른쪽 자판이므로 r로 계산하고 `res++, r=s[i]`

</br>

## 코드
```cpp
// BOJ 20436 ZOAC 3

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;

void init()
{
    v.push_back('q' - 'a');
    v.push_back('w' - 'a');
    v.push_back('e' - 'a');
    v.push_back('r' - 'a');
    v.push_back('t' - 'a');
    v.push_back('a' - 'a');
    v.push_back('s' - 'a');
    v.push_back('d' - 'a');
    v.push_back('f' - 'a');
    v.push_back('g' - 'a');
    v.push_back('z' - 'a');
    v.push_back('x' - 'a');
    v.push_back('c' - 'a');
    v.push_back('v' - 'a');
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    init();
    
    int arr[26][2] = {
        {1, 2},
        {5, 3},
        {3, 3},
        {3, 2},
        {3, 1},
        {4, 2},
        {5, 2},
        {6, 2},
        {8, 1},
        {7, 2},
        {8, 2},
        {9, 2},
        {7, 3},
        {6, 3},
        {9, 1},
        {10, 1},
        {1, 1},
        {4, 1},
        {2, 2},
        {5, 1},
        {7, 1},
        {4, 3},
        {2, 1},
        {2, 3},
        {6, 1},
        {1, 3}};

    char l, r;
    string s;

    cin >> l >> r;
    cin >> s;

    int res = 0;

    for (int i = 0; i < s.size(); i++)
    {
        if(find(v.begin(), v.end(), s[i]-'a') != v.end()){
            res += (abs(arr[l-'a'][0]-arr[s[i]-'a'][0]) + abs(arr[l-'a'][1]-arr[s[i]-'a'][1]));
            res++;
            l=s[i];
        }
        else
        {
            res+=(abs(arr[r-'a'][0]-arr[s[i]-'a'][0]) + abs(arr[r-'a'][1]-arr[s[i]-'a'][1]));
            res++;
            r=s[i];
        }
    }

    cout << res << "\n";

    return 0;
}
```