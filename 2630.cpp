#include <bits/stdc++.h>
using namespace std;
int arr[300][300];
int ans[2];
bool check(int n, int x, int y){
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
            if(arr[x][y]!=arr[x+i][y+j])
            return false;
    return true;
}
void solve(int n, int x, int y){
    if(check(n,x,y)){
        ans[arr[x][y]]++;
        return;
    }
    int a=n/2;
    for(int i=0; i<2; ++i)
    for(int j=0; j<2; ++j)
        solve(a, x+a*i,y+a*j);
    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for(int i=0; i<n; ++i)
    for(int j=0; j<n; ++j)
        cin>>arr[i][j];
    solve(n,0,0);
    for(int i:ans) cout<<i<<'\n';
}