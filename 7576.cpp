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
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++){
            cin>>board[i][j];
            if(board[i][j]==1) Q.push({i,j});
            if(board[i][j]==0) dist[i][j] = -1;
        }
    while(!Q.empty()){
        pair<int,int> cur=Q.front();Q.pop();
        for(int dir=0; dir<4; ++dir){            
            int nx=cur.first+dx[dir];
            int ny=cur.second+dy[dir];
            if(nx<0||nx>=n||ny<0||ny>=m) continue;           
            if(dist[nx][ny]>=0) continue;
            //if(board[nx][ny]==-1||dist[nx][ny]<=dist[cur.first][cur.second]+1) continue; 
            //위 코드는 다른 지점에서 탐색할때 거리가 더 가까울 경우 때문에 짰었는데 실제로는 BFS
            //이기 때문에 중간 지점에서 만난다면 같은 거리일 수밖에 없음.
            //따라서 그냥 탐색 했었는지만 판별하면 됨.
            dist[nx][ny]=dist[cur.first][cur.second]+1;
            Q.push({nx,ny});
        }
    }
    int max=0;
    for(int i=0; i<n; ++i)
        for(int j=0; j<m; ++j){
            if(dist[i][j]==-1) {
                 cout<<-1;
                 return 0;
            }else if(dist[i][j]>max) max=dist[i][j];            
            
        }
    
    cout<<max;
}