#include <bits/stdc++.h>
using namespace std;
//custom linked list ver
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, K;
    cin>>N>>K;
    int pre[5001], nxt[5001];
       
    for(int i=1; i<=N; ++i){
        pre[i]=i-1;
        nxt[i]=i+1;
    }
     pre[1]=N;
     nxt[N]=1;     
     int iter=1;
     cout<<"<";
     while(N--){
        for(int i=1;i<K;++i){
            iter=nxt[iter];
        }
        cout<<iter;
        pre[nxt[iter]]=pre[iter];
        nxt[pre[iter]]=nxt[iter];
        iter=nxt[iter];
        if(N>0) cout<<", ";
     }
     cout<<">"; 
}