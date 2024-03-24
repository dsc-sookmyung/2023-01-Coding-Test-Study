# C++에서 문자열(String) 다루기

</br>

## string 클래스의 특징
- 문자의 끝에 null 문자 등이 포함되지 않음
- 배열처럼 한 문자씩 다룰 수 있음
- string 클래스끼리는 + 연산자로 문자열 합치기 가능
- 문자열 사전순 정렬 가능
- 다양한 멤버함수 존재

</br>

## 멤버 함수
- str.front(): 맨 앞 문자 반환
- str.back(): 맨 끝 문자 반환
- str.size() or str.length(): 문자열 길이 반환
- to_string(): 숫자>문자열
- str.capacity(): capacity 값 확인
- str.reverve(n): 미리 n byte 할당
- str.empty(): 빈 문자열인지 확인
- str.clear(): 문자열을 없앰 (capacity 값은 유지)
- str1.append(str2): str1 뒤에 str2 문자열 추가
- str.find(str2): str에서 str2를 찾고 시작점 인덱스 반환
- str.substr():문자열의 일부분 반환
- str.replace(): 다양하게 오버로딩 되더 있는 replace 함수

---

</br>

# BOJ 10798 세로읽기
## 문제 요약
1. 입력: 다섯 줄의 입력, 각 줄에 1~15개의 글자들이 주어짐
2. 출력: 세로로 읽은 순서대로 글자 출력

</br>

## 풀이과정
1. for문으로 문자열 5줄 입력 받기
2. 문자열 size 확인하면서 맨 앞부터 출력
   
</br>

## 코드
```cpp
// BOJ 10798 세로 읽기

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string str[5];
    for(int i=0; i<5; i++){
        cin >> str[i];
    }

    for(int i=0; i<15; i++){
        for(int j=0; j<5; j++){
            if(i<str[j].size()){
                cout << str[j][i];
            }
        }
    }

    return 0;
}
```

</br>

---

</br>

# BOJ 6550 부분 문자열
## 문제 요약
1. 입력: 여러 개의 테스트케이스, 문자열 s와 t
2. s가 t의 부분 문자열인지 판단하는 프로그램   
   - t에서 몇개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되어야 함
3. 출력: 부분 문자열인 경우 YES, 아닌 경우 NO
   
</br>

## 풀이과정
1. 문자열 입력 받고 s의 첫 문자부터 t의 첫 문자와 비교
2. s의 idx번 문자가 t의 i번 문자가 같으면 s의 다음 문자와 비교
3. idx값과 s의 length 값이 같아지면 res true로 바꾸고 break
4. res값에 따라 출력

</br>

## 코드
```cpp
// BOJ 6550 부분 문자열

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s, t;

    while (cin >> s >> t)
    {
        bool res = false;
        int idx = 0;

        for (int i = 0; i < t.size(); i++)
        {
            if (s[idx] == t[i])
                idx++;
            if (idx == s.length())
            {
                res = true;
                break;
            }
        }

        if (res)
            cout << "Yes\n";
        else
            cout << "No\n";
    }

    return 0;
}

```

</br>

# BOJ 20291 파일 정리
## 문제 요약
1. 입력: 바탕화면에 있는 파일의 개수 N, 파일의 이름(알파벳 소문자와 점으로 구성)
2. 출력: 확장자의 이름과 그 확장자 파일의 개수
</br>

## 풀이과정
1. map 사용해서 확장자 관리
2. 입력 받은 후 substr로 . 뒤의 글자 분리(확장자)

</br>

## 코드
```cpp
// BOJ 20291 파일 정리

#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    string s;
    map<string, int> ex;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> s;
        s = s.substr(s.find('.') + 1);
        ex[s]++;
    }

    for (auto it = ex.begin(); it != ex.end(); it++)
    {
        cout << (*it).first << " " << (*it).second << "\n";
    }

    return 0;
}
```
---

</br>

# BOJ 17609 회문
## 문제 요약
1. 입력: 문자열의 개수 T, 문자열
2. 회문: 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성
   유사 회문: 한 문자를 삭제하여 회문으로 만들 수 있음
3. 출력: 회문(0)인지, 유사 회문(1)인지, 둘 다 아닌지(2) 출력

</br>

## 풀이과정
1. 회문 판단을 위한 palindrome 함수 작성
   - left, right 비교하여 모두 같으면 return 0 (회문)
   - 틀린 부분이 있으면 부분 회문 확인
   - 모두 아니면 return 2 (둘 다 아님)
2. 입력 받고 회문 판단 후 출력

</br>

## 코드 
```cpp
// BOJ 17609 회문

#include <iostream>
#include <string>
using namespace std;

int palindrome(string s, int check)
{
    int left, right;
    left = 0;
    right = s.size() - 1;

    while (left < right)
    {
        if (s[left] != s[right])
        {
            if (check == 0)
            {
                int len = right - left;
                if (palindrome(s.substr(left + 1, len), 1) == 0 || palindrome(s.substr(left, len), 1) == 0)
                    return 1;
                else
                    return 2;
            }
            else 
                return 2;
        }
        left++;
        right--;
    }
    return 0;
}
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        string s;
        cin >> s;
        cout << palindrome(s, 0) << "\n";
    }
    return 0;
}
```
---

</br>

