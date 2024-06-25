#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    double K;
    double arr[2][6]={};
    cin>>N>>K;
    for(int i=0; i<N; i++){
        int a,b;
        cin>>a>>b;
        arr[a][b-1]++;        
    }
    double ans;
    for(int i=0; i<2; i++){
        for(int j=0; j<6; j++){
            ans+=ceil(arr[i][j]/K);            
        }
    }
    cout<<ans;
}