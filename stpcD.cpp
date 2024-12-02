#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long N;
    cin>>N;
    for(int i=1; i<=N; i++){
        if((N/i)!=(N+1)/i){
            cout<<i<<' ';
        }
    }
}