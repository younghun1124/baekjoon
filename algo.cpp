#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

void printMST(const vector<Edge>& mst) {
    cout << "MST: ";
    for (const auto& edge : mst) {
        cout << "(" << edge.u << ", " << edge.v << ") ";
    }
    cout << endl;
}

void printTour(const vector<int>& path) {
    cout << "방문 경로: ";
    for (int v : path) {
        cout << v << " ";
    }
    cout << path[0] << endl;
}

vector<Edge> generateMST(const vector<vector<int>>& adjMatrix, int n) {
    vector<bool> visited(n, false);
    vector<Edge> mst;
    vector<int> minCost(n, INT_MAX);
    vector<int> mstParent(n, -1);

    minCost[0] = 0;

    for (int i = 0; i < n; ++i) {
        int u = -1;
        for (int v = 0; v < n; ++v) {
            if (!visited[v] && (u == -1 || minCost[v] < minCost[u])) {
                u = v;
            }
        }

        visited[u] = true;
        if (mstParent[u] != -1) {
            mst.push_back({ mstParent[u], u, adjMatrix[mstParent[u]][u] });
        }

        for (int v = 0; v < n; ++v) {
            if (!visited[v] && adjMatrix[u][v] < minCost[v]) {
                minCost[v] = adjMatrix[u][v];
                mstParent[v] = u;
            }
        }
    }
    return mst;
}

void greedyTour(const vector<vector<int>>& adjMatrix, int n, vector<int>& path, int current, vector<bool>& visited) {
    visited[current] = true;
    path.push_back(current);

    int next = -1;
    int minDist = INT_MAX;

    for (int v = 0; v < n; ++v) {
        if (!visited[v] && adjMatrix[current][v] < minDist) {
            minDist = adjMatrix[current][v];
            next = v;
        }
    }

    if (next != -1) {
        greedyTour(adjMatrix, n, path, next, visited);
    }
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> adjMatrix(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> adjMatrix[i][j];
        }
    }

    vector<Edge> mst = generateMST(adjMatrix, n);
    printMST(mst);

    vector<bool> visited(n, false);
    vector<int> path;
    greedyTour(adjMatrix, n, path, 0, visited);
    printTour(path);

    return 0;
}