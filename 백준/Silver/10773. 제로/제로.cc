#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> S;
    int K;
    cin>>K;
    int a;
    int N=K;
    long long ans=0;
    for(int i=0; i<K;++i){
        
        cin>>a;
        if(a==0) {
            S.pop();
            N--;
        }
        else{
            S.push(a);            
        } 
    }
    while(N--){
        if(!S.empty()) {
        ans+=S.top();
        S.pop();
        }
    }
    cout<<ans;    
}