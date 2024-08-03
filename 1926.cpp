#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
    int board[502][502];
    bool vis[502][502];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m;
    cin>>n>>m;
    int dx[4]={1,0,-1,0};
    int dy[4]={0,1,0,-1};

    for(int i=0; i<n;i++){
        for(int j=0; j<m;j++){
            cin>>board[i][j];
        }
    }
    queue<pair<int,int>> Q;
    int picture_num=0;
    int max_area=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(!vis[i][j]&&board[i][j]){
                picture_num++;
                vis[i][j]=1;
                int tmp_area=1;
                Q.push({i,j});
                while(!Q.empty()){
                    pair<int, int> cur=Q.front(); Q.pop();
                    for(int dir=0; dir<4; ++dir){
                        int nx=cur.X+dx[dir];
                        int ny=cur.Y+dy[dir];
                        if(nx<0||nx>=n||ny<0||ny>=m) continue;
                        if(vis[nx][ny]||board[nx][ny]!=1) continue;
                        vis[nx][ny]=1;
                        tmp_area++;
                        Q.push({nx,ny});
                    }
                }
                if(tmp_area>max_area) max_area=tmp_area;
            }
        }
    }
    cout<<picture_num<<"\n"<<max_area;
}