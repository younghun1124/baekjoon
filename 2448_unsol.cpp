#include <bits/stdc++.h>
using namespace std;
char board[4000][8000];

void solve(int n, int x, int y){
    if(n==1){
        board[x][y]='*';
        return;
    }
    n=n/2;
    
    
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for(int i=0; i<n; ++i)
    fill_n(board[i],n,' ');
    
}