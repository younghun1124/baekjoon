#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

double calc_dist(pair<int,int> p1, pair<int,int> p2){
    return sqrt(pow(p1.X - p2.X, 2) + pow(p1.Y - p2.Y, 2));
}

double closest_pair(vector<pair<int,int>> &v, int sidx, int eidx){
    if ((eidx - sidx + 1) <= 3) {  // If the number of points is small enough
        vector<double> tv;
        tv.push_back(calc_dist(v[sidx], v[sidx+1]));
        if ((eidx - sidx + 1) == 3) {
            tv.push_back(calc_dist(v[sidx+1], v[sidx+2]));
            tv.push_back(calc_dist(v[sidx], v[sidx+2]));
        }
        return *min_element(tv.begin(), tv.end());
    }

    int midx = (sidx + eidx) / 2;
    double sl = closest_pair(v, sidx, midx);
    double sr = closest_pair(v, midx + 1, eidx);
    double min_dist = min(sl, sr);

    // Adjust left and right pointers for the middle area
    vector<pair<int,int>> middle;
    for (int i = sidx; i <= eidx; i++) {
        if (abs(v[midx].X - v[i].X) < min_dist) {
            middle.push_back(v[i]);
        }
    }

    // Sort the middle strip by Y-coordinates
    sort(middle.begin(), middle.end(), [](const pair<int,int> &a, const pair<int,int> &b){
        return a.Y < b.Y;
    });

    // Calculate the minimum distance in the middle strip
    for (int i = 0; i < middle.size(); i++) {
        for (int j = i + 1; j < middle.size() && (middle[j].Y - middle[i].Y) < min_dist; j++) {
            min_dist = min(min_dist, calc_dist(middle[i], middle[j]));
        }
    }

    return min_dist;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    
    vector<pair<int, int>> v(N);

    cin.ignore();
    for (int i = 0; i < N; i++) {
        string input;
        getline(cin, input);

        size_t commaPos = input.find(',');
        pair<int,int> tp = {stoi(input.substr(0, commaPos)), stoi(input.substr(commaPos + 2))};
        v[i] = tp;
    }

    // Sort points by X-coordinates
    sort(v.begin(), v.end());

    // Call closest_pair function
    cout << fixed << setprecision(6) << closest_pair(v, 0, N - 1) << '\n';

    return 0;
}
