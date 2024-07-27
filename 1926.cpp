#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
    int board[502][502];
    bool vis[502][502];
       int n,m;
      int dx[4]={1,0,-1,0};
    int dy[4]={0,1,0,-1};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    cin>>n>>m;
    for(int i=0; i<n;i++)
        for(int j=0; j<m;j++)
            cin>>board[i][j];  
    int picture_num=0;
    int max_area=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(vis[i][j]||board[i][j]==0) continue;
            picture_num++;
            queue<pair<int,int>> Q;
            vis[i][j]=1;
            Q.push({i,j});
            int tmp_area=0;
            while(!Q.empty()){
                tmp_area++;
                pair<int, int> cur=Q.front(); Q.pop();
                for(int dir=0; dir<4; dir++){
                    int nx=cur.X+dx[dir];
                    int ny=cur.Y+dy[dir];
                    if(nx<0||nx>=n||ny<0||ny>=m) continue;
                    if(vis[nx][ny]||board[nx][ny]!=1) continue;
                    vis[nx][ny]=1;
                    Q.push({nx,ny});
                }
            }
            max_area=max(max_area,tmp_area);            
        }
    }
    std::cout<<picture_num<<'\n'<<max_area;
}