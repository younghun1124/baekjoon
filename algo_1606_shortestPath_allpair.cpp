#include <iostream>
#include <vector>
using namespace std;

const int INF = 1000000000; // 매우 큰 값으로 설정하여 연결되지 않은 경로를 나타냄

void floydWarshall(int n, vector<vector<int>>& D) {
    vector<vector<int>> dist(n, vector<int>(n, INF));

    // 초기화
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                dist[i][j] = 0;
            } else if (D[i][j] != -1) {
                dist[i][j] = D[i][j];
            }
        }
    }

    // 플로이드-워셜 알고리즘 적용
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] < INF && dist[k][j] < INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    // 결과 출력, INF 값을 -1로 변환하여 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == INF) {
                cout << "-1 ";
            } else {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> D(n, vector<int>(n));

    // 입력 처리
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> D[i][j];
        }
    }

    // 플로이드-워셜 알고리즘 실행
    floydWarshall(n, D);

    return 0;
}
