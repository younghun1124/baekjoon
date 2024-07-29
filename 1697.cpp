#include <bits/stdc++.h>
using namespace std;
int board[100002];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N,K;
    cin>>N>>K;
    queue<int> Q;
    fill_n(board,100002,-1);
    Q.push(N);
    board[N]=0;
    while(!Q.empty()){
        int cur=Q.front(); Q.pop();
        for(int nx:{cur-1,cur+1,cur*2}){
            if(nx<0||nx>100000) continue;
            if(board[nx]>=0) continue;
            board[nx]=board[cur]+1;
            Q.push(nx);
        }            
    }
    cout<<board[K];
}