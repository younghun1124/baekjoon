#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    int arr[N]={};
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    int v;
    cin>>v;
    int ans;
    for(int num:arr){
        if(num==v){
            ans++;
        }
    }
    cout<<ans;
}