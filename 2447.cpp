#include <bits/stdc++.h>
using namespace std;
int arr[7000][7000];
void solve(int n, int x, int y){
    if(n==1){
        arr[x][y]=1;
        return;
    }
    n=n/3;
    for(int i=0; i<3; ++i)
        for(int j=0; j<3; ++j){
            if(i==1&&j==1) continue;
            solve(n,x+i*n,y+j*n);
        }
    return;   
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    solve(n,0,0);
    for(int j=0; j<n; ++j){
        for(int i=0; i<n; ++i)
          if(arr[j][i]) cout<<'*';
          else cout<<' ';
        cout<<'\n';
    }      
}