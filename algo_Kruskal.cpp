#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Structure to represent an edge with two vertices u, v and weight w
struct Edge {
    int u, v, w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

// Disjoint Set Union (DSU) for union-find operations
vector<int> parent, rankSet;

// Find the representative of a set with path compression
int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

// Union by rank
void unite(int x, int y) {
    x = find(x);
    y = find(y);
    if (x != y) {
        if (rankSet[x] < rankSet[y]) {
            parent[x] = y;
        } else if (rankSet[x] > rankSet[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rankSet[x]++;
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    // Read all the edges
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    // Sort edges by their weights
    sort(edges.begin(), edges.end());

    // Initialize DSU
    parent.resize(n);
    rankSet.resize(n, 0);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }

    // Kruskal's algorithm
    vector<Edge> mst;
    int totalWeight = 0;

    for (Edge e : edges) {
        if (find(e.u) != find(e.v)) {
            unite(e.u, e.v);
            mst.push_back(e);
            totalWeight += e.w;
        }
    }

    // Output the edges in the MST
    for (Edge e : mst) {
        cout << e.u << " " << e.v << " " << e.w << endl;
    }

    // Output the total weight of the MST
    cout << totalWeight << endl;

    return 0;
}
