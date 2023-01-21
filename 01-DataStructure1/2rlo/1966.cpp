// BOJ 1966 프린터 큐

#include <iostream>
#include <queue>
using namespace std;

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n, m, res = 0;
        queue <pair<int,int>> q;
        priority_queue<int> pq;

        cin >> n >> m;

        for(int i=0; i<n; i++){
            int w;
            cin >> w;
            q.push({i, w});
            pq.push(w);
        } 

        while (!q.empty()){
            int currentIndex = q.front().first;
            int currentImportance = q.front().second;

            q.pop();

            if(pq.top() == currentImportance){
                pq.pop();
                res++;
                if(currentIndex == m){
                    cout << res << endl;
                    break;
                }
            }
            else {
                q.push({currentIndex, currentImportance});
            }
        }
    }

    return 0;
}