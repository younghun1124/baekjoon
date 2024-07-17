#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, L;
    deque<pair<int,int>> dq;
    cin>>N>>L;
    for(int i=0; i<N; ++i){
        int input;
        cin>>input;
        while(!dq.empty()&&dq.back().first>=input)dq.pop_back();
        dq.push_back({input,i});        
        while(i-dq.front().second>=L)dq.pop_front();
        cout<<dq.front().first<<" ";        
    }
    
}