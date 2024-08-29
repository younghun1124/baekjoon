#include <bits/stdc++.h>
using namespace std;
string arr[64];
bool check(int n, int x, int y){
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
            if(arr[x][y]!=arr[x+i][y+j]) return false;     
    return true;
}
void solve(int n, int x, int y){
    if(check(n,x,y)){
        cout<<arr[x][y];
        return;
    }
    n=n/2;
    cout<<"(";
    for(int i=0; i<2; ++i)
     for(int j=0; j<2; ++j)
        solve(n, x+i*n, y+j*n);
    cout<<")";
    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for(int i=0; i<n; ++i) 
        cin>>arr[i];
    solve(n,0,0);
}