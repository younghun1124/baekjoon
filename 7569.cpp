#include <bits/stdc++.h>
using namespace std;
int board[105][105][105];
int vis[105][105][105];
int dx[6]={1,0,0,-1,0,0};
int dy[6]={0,1,0,0,-1,0};
int dh[6]={0,0,1,0,0,-1};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int M,N,H;
    cin>>M>>N>>H;
    queue<tuple<int,int,int>> Q;
    for(int k=0; k<H; ++k)
        for(int i=0; i<N; ++i)
            for(int j=0; j<M; ++j){
                int input;
                cin>>input;
                board[k][i][j]=input;
                if(input==1) Q.push({k,i,j});
                if(input==0) vis[k][i][j]=-1;
            }

            //비어있다 0
            //들어있다 -1
            //걸러야하는것=>이미 익은곳, 토마토없는곳
    while(!Q.empty()){
        tuple<int,int,int> cur=Q.front(); Q.pop();
        for(int i=0; i<6; ++i){
            int nh=dh[i]+get<0>(cur);
            int nx=dx[i]+get<1>(cur);
            int ny=dy[i]+get<2>(cur);
            if(nh<0||nh>=H||nx<0||nx>=N||ny<0||ny>=M) continue;
            if(vis[nh][nx][ny]>=0) continue;
            vis[nh][nx][ny]=vis[get<0>(cur)][get<1>(cur)][get<2>(cur)]+1;
            Q.push({nh,nx,ny});
        }   
    }
    int mx=0;
    for(int k=0; k<H; ++k)
        for(int i=0; i<N; ++i)
            for(int j=0; j<M; ++j){
                if(vis[k][i][j]==-1){
                    cout<<-1;
                    return 0;
                }
                mx=max(vis[k][i][j],mx);

            }
    cout<<mx;

            
}