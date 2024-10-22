#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long N, M;
    cin>>N>>M;
    long long ans=(N-1)*(M)+(M-1)*N+(N-1)*2*(M-1);
    cout<<ans;
}