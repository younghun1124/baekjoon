#include <bits/stdc++.h>
using namespace std;
string board[1005];
int vis[1005][1005];
int fire[1005][1005];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int R,C;
    cin>>R>>C;
    queue<pair<int,int>> Q1, Q2;   
    for(int i=0; i<R; ++i){
         fill_n(vis[i],C,-1);
         fill_n(fire[i],C,-1);
    }
   
    for(int i=0; i<R; ++i){
        cin>>board[i];
        for(int j=0; j<C; ++j){
            if(board[i][j]=='F'){
                Q1.push({i,j});
                fire[i][j]=0;
            }
            if(board[i][j]=='J'){
                Q2.push({i,j});
                vis[i][j]=0;
            }
        }
            
    }
        
    while(!Q1.empty()){
        auto cur=Q1.front();Q1.pop();
        for(int dir=0; dir<4; dir++){
            int nx=dx[dir]+cur.first;
            int ny=dy[dir]+cur.second;
            if(nx<0||nx>=R||ny<0||ny>=C) continue;
            if(fire[nx][ny]>=0||board[nx][ny]=='#') continue;
            fire[nx][ny]=fire[cur.first][cur.second]+1;
            Q1.push({nx,ny});
        }        
    }
    while(!Q2.empty()){
        auto cur=Q2.front();Q2.pop();
        for(int dir=0; dir<4; dir++){
            int nx=dx[dir]+cur.first;
            int ny=dy[dir]+cur.second;
            if(nx<0||nx>=R||ny<0||ny>=C){
                cout<<vis[cur.first][cur.second]+1;
                return 0;
            }
            if(vis[nx][ny]>=0||board[nx][ny]=='#') continue;
            if(fire[nx][ny]!=-1&&fire[nx][ny]<=vis[cur.first][cur.second]+1) continue;
            vis[nx][ny]=vis[cur.first][cur.second]+1;
            Q2.push({nx,ny});
        }     
    }
    cout<<"IMPOSSIBLE";
}