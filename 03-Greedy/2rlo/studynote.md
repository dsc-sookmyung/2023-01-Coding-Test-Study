# 그리디 알고리즘
> `Greedy`: 탐욕스러운, 욕심 많은  
> 선택의 순간마다 최적의 상황만을 쫓아 최종적인 답에 도달하는 방법  
> 탐욕 알고리즘을 적용할 수 있는 문제들은 지역적으로 최적이면서 전역적으로 최적인 문제들
---
## 문제 해결 방법
1. `선택 절차 (Selection Procedure)`: 현재 상태에서 최적의 해답 선택
2. `적절성 검사(Feasibility Check)`: 선택된 해가 문제의 조건을 만족하는지 검사
3. `해답 검사(Solution Check)`: 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 과정을 반복
---
## 적용 조건
1. `탐욕스런 선태 조건 (Greedy choice property)`: 앞의 선택이 이후의 선택에 영향을 주지 않음
2. `최적 부분 구조 조건 (optimal substructure)`: 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성 됨

- `매트로이드`: 특별한 구조가 있는 문제에 대해서는 탐욕 알고리즘이 언제나 최적해를 찾아낼 수 있음.
---
## 근사 알고리즘 (Approximation Algorithm)
- 어떤 최적화 문제에 대한 해의 근사값을 구하는 알고리즘
- 가장 최적화 되는 답을 구할 수는 없지만, 비교적 빠른 시간에 계산이 가능하며 어느 정도 보장된 근사해 계산 가능
---
# BOJ 14916 거스름돈
## 문제 요약
- 입력: 거스름돈 액수 `N`
- `2원과 5원`으로만 거스름돈을 주어야 함
- 출력: `최소` 동전의 개수 / 거슬러 줄 수 없는 경우에는 `-1`
---
## 풀이과정
1. `1원과 3원`의 경우 거슬러 줄 수 없으므로 `-1` 출력
   - 나머지 액수는 거슬러 줄 수 있음 (2와 5의 조합)
2. 5로 나눈 나머지가 짝수인 경우   
 5원 거스름돈 개수(`n/5`) + 남은 돈을 2원 거스름돈으로(`n%5/2`)
3. 5로 나눈 나머지가 홀수인 경우: 이 경우에는 5원을 더해서 2원 거스름돈으로 주어야 하므로 **(1,3,5의 경우 2원으로 거스름돈을 주지 못하므로 6, 8, 10원으로 계산하여야 함)**    
   5원 거스름돈 개수(`n/5`)-1+2원 거스름돈 개수(`(n%5+5)/2`) 
---
## 코드
```cpp
// BOJ 14916 거스름돈

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;

    cin >> n; 

    if (n==1 || n ==3)
    {
        cout << -1 <<"\n";
        return 0;
    }

    if(n % 5 % 2)
    {
        cout << n/5-1 + (n%5+5) / 2;
    }
    else
    {
        cout << n/5+n%5/2;
    }
    
    return 0;
}
```
---
# BOJ 2217 로프
## 문제 요약
- 입력: `N(1≤N≤100,000)개의 로프`와 `각 로프가 버틸 수 있는 최대 중량`
- 여러 개의 로프를 병렬로 연결 시 로프에 걸리는 `중량을 나눌 수 있음` (k개의 로프를 사용하여 w를 들어올릴 시 각각의 로프에 가해지는 중량은 `w/k`)
- 모든 로프를 사용할 필요는 없음
- 출력: 들어올릴 수 있는 물체의 `최대 중량`
---
## 풀이과정
1. **`최대 중량` = 버틸 수 있는 최대 중량 * 버틸 수 있는 최대 중량을 만족하는 로프의 수**
2. 따라서 `우선순위 큐`로 정렬하고 하나씩 꺼내 로프의 수만큼 곱함
3. res보다 곱한 값이 크다면 res를 재정의
   
---
## 코드
```cpp
// BOJ 2217 로프

#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;
    priority_queue<int> rope;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        rope.push(temp);
    }

    for (int i = 0; i < n; i++)
    {
        int sum = rope.top() * (i + 1);
        rope.pop();
        if (sum > res)
            res = sum;
    }

    cout << res << "\n";

    return 0;
}
```

# BOJ 11508 2+1 세일
## 문제 요약
- 입력: 유제품의 수 `N`과 가격 $C_i$
- 3개로 묶어 가장 싼 것의 가격은 지불하지 않음
- 출력: 최소비용

## 풀이과정
1. **`최소 비용`: 가장 비싼것부터 정렬하여 3의 배수 번째의 경우 더해주지 않은 값**
2. 우선순위 큐로 정렬하고, 3의 배수의 경우 더하지 않음
---
## 코드
```cpp
// BOJ 11508 2+1 세일

#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;
    priority_queue<int> product;

    cin >> n;

    for(int i=0; i<n; i++)
    {
        int temp;
        cin >> temp;
        product.push(temp);
    }

    for (int i=1; i<=n; i++)
    {
        if (i%3)
            res += product.top();
        product.pop();
    }

    cout << res << "\n";
    
    return 0;
}
```
---
# BOJ 13305 주유소
## 문제 요약
- 입력: 도시의 개수 `N`, 두 도시를 연결하는 도로의 길이(`N-1개`), 각 도시의 주유소 리터당 가격
- 처음 출발할 때 자동차에 기름을 넣고 출발하여야 함
- 기름통의 크기는 무제한
- 1km마다 1리터의 기름 사용
- 출력: 제일 왼쪽에서 제일 오른쪽 도시로 가는 `최소 비용`
---
## 풀이과정
1. 기름 리터당 가격이 가장 낮은 곳에서 주유해야 함   
2. 따라서 가장 낮은 곳의 `cost`를 저장하고 `저장한 코스트 * 도로의 길이` 계산
---
## 코드 
```cpp
// BOJ 13305 주유소

#include <iostream>
#include <climits>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    long long res = 0;
    int cost = INT_MAX;
    int len[100001], oil[100001];

    cin >> n;

    for (int i = 0; i < n - 1; i++)
    {
        cin >> len[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> oil[i];
    }

    for(int i=0; i<n; i++){
        if(oil[i] < cost)
            cost = oil[i];
        res += (long long)cost * (long long)len[i];
    }

    cout << res << "\n";

    return 0;
}
```
---
# BOJ 20365 블로그2
## 문제 요악
- 입력: 칠해야 하는 문제의 수 `N`, `N개의 문자`(R=빨간색, B=파란색)
- 연속된 임의의 문제들을 선택해 선택된 문제들을 전부 같은 색으로 칠함
- 출력: 작업횟수의 `최솟값`
---
## 풀이 과정
1. `color`가 `B`일 경우   
   1-1. 만약 이전 color가 red라면 red++   
   1-2. red_flag를 false, blue_flag를 true로 변경
2. `color`가 `R`인 경우   
   2-1. 만약 이전 color가 blue라면 blue++   
   2-2. blue_flag를 false, red_flag를 true로 변경
3. red, blue 값 중 `최소값`을 출력
---
## 코드
```cpp
// BOJ 20365 블로그2

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, red = 1, blue = 1;
    string color;
    bool red_flag = true, blue_flag = true;

    cin >> n >> color;

    for (int i = 0; i < n; i++)
    {
        if (color[i] == 'B')
        {
            if (red_flag)
                red++;
            red_flag = false;
            blue_flag = true;
        }
        else if (color[i] == 'R')
        {
            if (blue_flag) blue++;
            blue_flag = false;
            red_flag = true;
        }
    }

    cout << min(red, blue);

    return 0;
}
```
---
# BOJ 1541 잃어버린 괄호
## 문제 요약
- 입력: `'0'~'9', '+', '-'`만으로 이뤄진 `식`
- 출력: 식에 `괄호`를 쳐서 만들 수 있는 `최소 값`
---
## 풀이 과정
- `"-"` 부호가 나올 경우 뒤의 식들을 모두 빼 줌.
---
## 코드
```cpp
// BOJ 1541 잃어버린 괄호

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int res = 0;

    string input, num;
    cin >> input;

    bool isMinus = false;

    for (int i=0; i<=input.size(); i++){
        if(input[i] == '-' || input[i] == '+' || i == input.size()) {
            if (isMinus) {
                res -= stoi(num);
                num = "";
            }
            else {
                res += stoi(num);
                num = "";
            }
        }
        else {
            num += input[i];
        }

        if(input[i] == '-') {
            isMinus = true;
        }
    }

    cout << res << "\n";

    return 0;
}
```