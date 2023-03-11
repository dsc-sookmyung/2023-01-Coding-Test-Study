# 이분 탐색
> 정렬된 리스트(배열)에서 원하는 값의 존재 여부(존재 위치)를 찾는 알고리즘   
> 탐색할 때마다 검사 범위가 절반으로 줄어듦   
> 재귀, 반복분, STL 사용   
> 단점: 반드시 리스트(배열)을 정렬해서 사용해야 함    
> 시간복잡도: `O($log N$)`

</br>

## 진행 과정
1. 검사 범위에서 중간 값(mid)를 선택해서 찾고자 하는 값이 같은지 확인
2. 만약 찾고자 하는 값이라면 해당 값을 반환
3. 만약 찾고자 하는 값보다 작다면 `low = mid + 1`
4. 만약 찾고자 하는 값보다 크다면 `high = mid - 1` 
5. 1~4를 반복하여 원하는 값이 나오면 해당 값 반환
6. 더 이상 검사 할 곳이 없으면(low>high) 돌아감

</br>

## 반복문 코드
```cpp
bool binary_search(vector<int>& arr, int len, int target){
	int low = 0, high = len - 1;
    
    while(low <= high){
    	int mid = (low + high) / 2;
        
        //원하는 값을 찾았다면 true 반환
        if(target == arr[mid])	return true;
        
        // 원하는 값이 더 작다면 검사 범위를 더 낮게 잡아야 한다.
        if(target < arr[mid]){
        	high = mid - 1;
        }
        // 원하는 값이 더 크다면 검사 범위를 더 크게 잡아야 한다.
        else if(target > arr[mid]){
        	low = mid + 1;
        }
    }
    return false; // 마지막까지 못찾는다면 false 반환
}
```

</br>

## 재귀 코드
```cpp
bool binary_search(vector<int>& arr, int low, int high, int target){
    if(low > end)	return false;
    int mid = (low + high) / 2;
    
    if(arr[mid] == target)	return true;
    
    // 찾는 수가 더 작다면, 검사 범위를 더 작게 잡아야 한다.
    if(arr[mid] > target)
    	return binary_search(arr, low, mid - 1, target);
        
    // 찾는 수가 더 크가면, 검사 범위를 더 크게 잡아야 한다.
    else
    	return binary_search(arr, mid + 1, high, target);
}
```

</br>

## STL 코드
```cpp
vector<int> nums;
int target = 3;
bool isFound = binary_search(nums.begin(), nums.end(), target);
// target(3)이 nums에 있다면 true를, 없다면 false를 반환
```
---

</br>

# BOJ 1789 수들의 합
## 문제 요약
1. 입력: 자연수 S (1 <= S <= 4,294,967,295)
2. 서로 다른 N개의 자연수의 합이 S일 때, N의 최댓값은?
3. 출력: 자연수 N의 최댓값

</br>

## 풀이과정
> 이분 탐색으로 풀려니 시간초과/메모리 초과가 빈번해서 결국 다르게 푼 문제   
1. 1부터 계속해서 더해줌
2. 만약 sum이 S보다 크다면 res--하고 break

</br>

## 코드
```cpp
// 1789 수들의 합

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long S, sum;
    int num = 1, res = 0;

    cin >> S;

    while (true) {
        sum += num;
        res++;
        if ( sum > S ){
            res--;
            break;
        }
        num++;
    }

    cout << res ;

    return 0;
}
```

</br>

---

</br>

# BOJ 2512 예산
## 문제 요약
1. 입력: 지방의 수 N, 지방의 예산 요청인 N개의 정수, 총 예산 M
2. 예산 배정 방법
   1. 모든 요청이 배정될 수 있는 경우 요청된 금액 그대로 배정
   2. 모든 요청이 배정될 수 없는 경우 특수한 정수 상한액을 계산하여 그 이상인 예산 요청에는 모두 상한액 배정, 상한액 이하 예산요청에 대해서는 요청한 금액 그대로 배정
3. 출력: 배정된 예산들 중 최댓값인 정수
</br>

## 풀이과정
1. 배열 입력받아서 정렬 후 이진 탐색
2. low = 0, high = max
3. 중간값보다 예산이 적으면 sum에 더해줌
4. 총액과 비교

</br>

## 코드
```cpp
// BOJ 2512 예산

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int bs(vector<int> arr, int n, int m, int max)
{
    int low = 0, high = max;
    int sum, res;

    while (low <= high)
    {
        sum=0;
        int mid = (low + high) / 2;
        for (int i = 0; i < n; i++)
        {
            sum += min(arr[i], mid);
        }
        if (m >= sum)
        {
            res = mid;
            low = mid + 1;
        }
        else
            high = mid - 1;
    }

    return res;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    vector<int> request;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        request.push_back(temp);
    }
    cin >> M;

    sort(request.begin(), request.end());
    cout << bs(request, N, M, request[N-1]);
    return 0;
}
```

</br>

# BOJ 1654 랜선 자르기
## 문제 요약
1. 입력: 랜선의 개수 K, 필요한 랜선의 개수 N, 이미 가지고 있는 각 랜선의 길이
2. 출력: N개를 만들 수 있는 랜선의 최대 길이
</br>

## 풀이과정
1. low=1, high=랜선들 중 가장 긴 길이 값
2. mid를 구하고 이분 탐색을 통해 만들 수 있는 전선 수를 구함
   1. 만들 수 있는 전선 수가 N보다 많거나 같다면 전선의 길이를 늘림
   2. 작다면 길이를 줄임
3. 랜선의 최대 길이 출력

</br>

## 코드
```cpp
// BOJ 1654 랜선 자르기

#include <iostream>
#include <algorithm>
using namespace std;

int K, N, res;
int len[10001];
int maxL = 0;
long long mid, high, low;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> K >> N;
    for (int i = 0; i < K; i++)
    {
        cin >> len[i];
        if (maxL < len[i])
            maxL = len[i];
    }

    low = 1;
    high = maxL;
    res = 0;

    while (low <= high)
    {
        mid = (low + high) / 2;
        int cnt = 0;
        for (int i = 0; i < K; i++)
            cnt += len[i] / mid;

        if (cnt >= N)
        {
            low = mid + 1;
            if (res < mid)
                res = mid;
        }
        else
            high = mid - 1;
    }

    cout << res;
    return 0;
}
```
---

</br>

# BOJ 징검다리 건너기 (large)
## 문제 요약
1. 입력: 돌의 개수 N, N개의 돌의 수 $A_i$
2. 건너는 방법
   1. 항상 오른쪽으로만 이동 가능
   2. i번째 돌에서 j번째 돌로 이동할 때 (j-i)*(1+$|A_i-A_j$)만큼 힘을 씀
   3. 돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 K
3. 출력: 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는 모든 경우 중 가능한 K의 최솟값

</br>

## 풀이과정
1. 오른쪽으로만 이동 가능
2. ans는 ans와 max(이후 ans, 현재 사용 힘)의 최솟값

</br>

## 코드 
```cpp
// BOJ 22871 징검다리 건너기 (large)

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
long long arr[5001], dp[5001];

long long solve(int x)
{
    if (x == N - 1)
        return 0;
    long long &ans = dp[x];
    if (ans != -1)
        return ans;

    ans = 1e10;
    for (int i = x + 1; i < N; i++)
    {
        ans = min(ans, max(solve(i), (i - x) * (1 + abs(arr[x] - arr[i]))));
    }
    return ans;
}
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(dp, -1, sizeof(dp));

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    cout << solve(0) << endl;

    return 0;
}
```
---

</br>

