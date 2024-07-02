#include <bits/stdc++.h>
using namespace std;
int arr[80000];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    
    for(int i=0; i<N; i++){        
        cin>>arr[i];
    }
    stack<pair<int, int>> S;
    long long ans=0;
    S.push({1000000005,0});
    for(int i=N-1; i>=0;i--){        
        pair<int, int> building={arr[i],0};        
        while(S.top().first<building.first){//새로온놈이 있던놈보다 크면
            building.second+=S.top().second+1;
            S.pop();
        }
        ans+=building.second;
        S.push(building);
    }
    cout<<ans;;
}