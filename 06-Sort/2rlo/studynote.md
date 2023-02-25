# 정렬

## 버블 정렬
> 배열의 2개 아이템을 선택하고 비교하여 왼쪽이 오른쪽보다 크면 swap, 이를 반복   
> 시간복잡도 $O(n^2)$

</br>

## 선택 정렬
> 가장 작은 아이템의 위치를 저장하고, 앞에서부터 swap   
> 최악의 경우 시간복잡도 $O(n^2)$, 최고의 경우 시간복잡도 $O(n)$
  
</br>

## 삽입 정렬
> 특정한 데이터가 적절한 위치에 들어가기 이전, 그 앞까지는 이미 정렬되어있다고 가정   
> 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤, 그 위치에 삽입   
> 최악의 경우 시간복잡도 $O(n^2)$, 최고의 경우 시간복잡도 $O(n)$

</br>

## 퀵 정렬
> 기준을 정한 다음 2개의 부분 배열로 분할하고 부분 배열을 정렬, 부분 배열의 크기가 충분히 작지 않으면 다시 분할 정복, 이후 정렬된 부분 배열들을 하나의 배열에 합병   
> 기준인 pivot 설정은 미리 명시   
> 시간 복잡도 $O(nlog_2n)$, 최악의 경우 시간복잡도 $O(n^2)$

</br>

## 병합 정렬
> 2개의 부분 배열로 분할 후 부분 배열을 정렬, 부분 배열의 크기가 충분히 작지 않으면 다시 분할 정복, 이후 정렬된 부분 배열들을 하나의 배열에 합병   
> pivot값을 사용하지 않음   
> 시간복잡도 $O(nlog_2n)$

</br>

## C++에서의 정렬
- `<algorithm>` 헤더에 `sort()` 함수 사용
- 함수의 시간 복잡도는 $O(nlogn)$
- intro sort로 구현됨: quick sort를 기반으로 heap sort와 insertion sort를 섞은 방식

</br>

---

</br>

# BOJ 10825 국영수
## 문제 요약
1. 입력: 도현이네 반 학생의 수 `N`, 각 학생의 `이름, 국어, 영어, 수학 점수`
2. 정렬 기준
   1. 국어 점수가 감소하는 순서로
   2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
   3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
   4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 옴)
3. 출력: 정렬 기준에 따라 `정렬한 후 각 학생의 이름` 출력

</br>

## 풀이과정
1. 비교해야 하는 값들을 담은 구조체 선언
2. 정렬 기준에 따라 cmp 함수 작성
3. 입력 받은 후 sort 함수로 정렬
4. 출력

</br>

## 코드
```cpp
// BOJ 10825 국영수

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct student {
    string name;
    int kor, eng, math;
};

bool cmp(student a, student b){
    if (a.kor == b.kor && a.eng == b.eng && a.math == b.math)
    return a.name < b.name;
    if(a.kor == b.kor && a.eng == b.eng)
    return a.math > b.math;
    if(a.kor == b.kor)
    return a.eng < b.eng;
    return a.kor > b.kor;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;

    vector<student> v(N);

    for(int i=0; i<N; i++){
        cin >> v[i].name >> v[i].kor >> v[i].eng >> v[i].math;
    }

    sort(v.begin(), v.end(), cmp);

    for(int i=0; i<N; i++){
        cout << v[i].name<<"\n";
    }
    
    return 0;
}
```

</br>

---

</br>

# BOJ 10814 나이순 정렬
## 문제 요약
1. 입력: 회원 수 `N`, 각 회원의 `나이와 이름`
2. 입력은 가입한 순서대로 주어짐
3. 출력: 나이 순, 나이가 같으면 가입한 순으로 `이름` 출력
</br>

## 풀이과정
1. 비교해야 하는 값들을 구조체로 구현
2. 비교 기준에 따른 cmp 함수 작성
3. 입력 받은 값 토대로 sort 함수 사용
4. 출력

</br>

## 코드
```cpp
// BOJ 10814 나이순 정렬

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct user
{
    int age, order;
    string name;
};

bool cmp(user a, user b)
{
    if (a.age == b.age)
        return a.order < b.order;
    return a.age < b.age;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;
    vector<user> v(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i].age >> v[i].name;
        v[i].order = i;
    }

    sort(v.begin(), v.end(), cmp);

    for (int i = 0; i < N; i++)
    {
        cout << v[i].age << " " << v[i].name << "\n";
    }

    return 0;
}
```

</br>

# BOJ 11652 카드
## 문제 요약
1. 입력: 숫자 카드의 개수 `N`, 숫자 카드에 적혀있는 정수
2. 수는 $-2^{64}$보다 크거나 같고, $2^{64}$보다 작거나 같음
3. 가장 많이 가지고 있는 정수가 여러가지일 경우 작은 것 출력
4. 출력: `가장 많이 가지고 있는 정수`
</br>

## 풀이과정
1. 범위 값이 크므로 `long long` 자료형으로 선언
2. 입력 받은 후 sort 함수로 정렬
3. arr[i] == arr[i-1] 경우 cnt++
4. cnt가 max보다 크면 max = cnt, res = arr[i]
5. 출력

</br>

## 코드
```cpp
// BOJ 11652 카드

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, max = 1, cnt = 1;
    long long res;
    long long arr[100001];

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    res = arr[0];
    for (int i = 1; i < N; i++)
    {
        if (arr[i] == arr[i - 1])
            cnt++;
        else
            cnt = 1;

        if (max < cnt)
        {
            max = cnt;
            res = arr[i];
        }
    }

    cout << res << "\n";

    return 0;
}
```
---

</br>

# BOJ 18870 좌표 압축
## 문제 요약
1. 입력: `N`, $X_n$
2. 압축한 결과 값은 $X_i>X_j$를 만족하는 서로 다른 좌표의 개수와 같아야 함
3. 출력: `압축한 결과 값`
</br>

## 풀이과정
> 결국 오름차순으로 정렬하고 중복을 제거한 순서
1. 입력받고 vc에 복제
2. vc를 이용해서 sort 함수 사용 후 unique 함수와 erase 함수 사용해서 중복값 제거
3. v[i]가 몇번째인지 출력

</br>

## 코드 
```cpp
// BOJ 18870 좌표 압축

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<int> v(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i];
    }

    vector<int> vc(v);
    sort(vc.begin(), vc.end());
    vc.erase(unique(vc.begin(), vc.end()), vc.end());

    for (int i = 0; i < N; i++)
    {
        auto it = lower_bound(vc.begin(), vc.end(), v[i]);
        cout << it - vc.begin() << " ";
    }

    return 0;
}
```
---

</br>