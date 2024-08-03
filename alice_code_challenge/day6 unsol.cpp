#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs(int c, int n, vector<int>& count, vector<int>& arr, vector<int>& ans) {
    if (ans[0] > ans[1]) {
        return;
    }
    if (c == n) {
        if (ans[0] < ans[1]) {
            ans[1] = ans[0];
        }
        return;
    }

    if (arr[c] == 1) {
        int i = n;
        while (true) {
            if (count[i] != 0) {
                break;
            }
            i--;
        }
        int a = i;
        count[a]--;
        i = n;
        while (true) {
            if (count[i] != 0) {
                break;
            }
            i--;
        }
        int b = i;
        count[b]--;

        count[a + b]++;
        dfs(c + 1, n, count, arr, ans);
        count[a + b]--;
        count[a]++;
        count[b]++;
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (count[i] == 0) {
            continue;
        }
        count[i]--;
        for (int j = i; j <= n; j++) {
            if (count[j] == 0) {
                continue;
            }
            count[j]--;
            ans[0] += i * j;
            count[i + j]++;
            dfs(c + 1, n, count, arr, ans);
            ans[0] -= i * j;
            count[i + j]--;
            count[j]++;
        }
        count[i]++;
    }
}

int main() {
    int n;
    cin >> n;
    
    vector<int> count(n + 1, 0);  // 원소가 i개인 집합의 개수
    count[1] = n;
    
    vector<int> arr(n + 1, 0);
    for (int i = 1; i < n; i++) {
        cin >> arr[i];
    }
    
    vector<int> ans = {0, n * n};
    
    dfs(1, n, count, arr, ans);
    
    cout << ans[1] << endl;
    
    return 0;
}
