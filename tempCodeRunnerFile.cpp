#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

double calc_dist(pair<int,int> p1, pair<int,int> p2){
    return sqrt(pow(p1.X-p2.X,2)+pow(p1.Y-p2.Y,2));    
}

double closest_pair(vector<pair<int,int>> v,int sidx, int eidx){
    if((eidx-sidx+1)<=3){//점의 개수가 계산할만 하면
        vector<double> tv;
        tv.push_back(calc_dist(v[sidx],v[sidx+1]));
        if((eidx-sidx+1)==3){
         tv.push_back(calc_dist(v[sidx+1],v[sidx+2]));
         tv.push_back(calc_dist(v[sidx],v[sidx+2]));
        }
        // cout<<*min_element(tv.begin(),tv.end())<<'\n';
        return *min_element(tv.begin(),tv.end());
    }
    int midx=(sidx+eidx)/2;
    double sl=closest_pair(v, sidx, midx);
    double sr=closest_pair(v, midx+1, eidx);
    double min_dist=min(sl,sr);
    int left,right;
    for(left=midx; min(sl,sr)>v[left].X; left--);
    for(right=midx+1; min(sl,sr)>v[right].X; right++);
    sort(v.begin()+left,v.begin()+right,[](const pair<int,int> &a, const pair<int,int> &b){//중간범위만 Y값으로 정렬
        return a.Y<b.Y;
    });
    for(int i=0; i<right-left;i++){
        for(int j=i+1; i<right-left+1;j++){
            if(v[j].Y-v[i].Y>=min_dist) break;
            min_dist=min(min_dist,calc_dist(v[i],v[j]));
        }
    }
    return min_dist;
    
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;

    vector<pair<int, int>> v(N);
     cin.ignore();
    for(int i=0;i<N; i++){
        string input;
    // 입력을 받음 (숫자 사이에 쉼표가 포함된 문자열)
     getline(cin, input);
    
    // 쉼표의 위치를 찾아 숫자를 나눔
    size_t commaPos = input.find(',');

    // 첫 번째 숫자와 두 번째 숫자를 추출하고 정수로 변환
    v[i].X = stoi(input.substr(0, commaPos));
    v[i].Y = stoi(input.substr(commaPos + 2));
    }
    sort(v.begin(),v.end());
    cout<<closest_pair(v,0,v.size()-1);

}