#include <bits/stdc++.h>
using namespace std;
int board[1005][1005];
int dist[1005][1005];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin>>m>>n;
    queue<pair<int,int>> Q;
    for(int i=0; i<n; ++i) fill_n(dist[i],m,2000000);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++){
            cin>>board[i][j];
            if(board[i][j]==1){
                Q.push({i,j});  
                dist[i][j]=0;
            }           
        }
    while(!Q.empty()){
        pair<int,int> cur=Q.front();Q.pop();
        for(int dir=0; dir<4; ++dir){            
            int nx=cur.first+dx[dir];
            int ny=cur.second+dy[dir];
            if(nx<0||nx>=n||ny<0||ny>=m) continue;           
            if(board[nx][ny]==-1||dist[nx][ny]<=dist[cur.first][cur.second]+1) continue;
            dist[nx][ny]=dist[cur.first][cur.second]+1;
            Q.push({nx,ny});
        }
    }
    int max=0;
    for(int i=0; i<n; ++i)
        for(int j=0; j<m; ++j){
            if(board[i][j]!=-1&&dist[i][j]==2000000) {
                 cout<<-1;
                 return 0;
            }else if(dist[i][j]!=2000000&&dist[i][j]>max) max=dist[i][j];            
            
        }
    
    cout<<max;
}