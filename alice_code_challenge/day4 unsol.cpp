#include <bits/stdc++.h>
using namespace std;

int p1, p2;
bool turn=true;
int ans;
void score_calc(vector<vector<int>> V, int num, int prev){
    if(turn) p1+=num;
    else p2+=num;
    turn=!turn;
    for(int &x:V[num]){
        if(prev!=x&&x) score_calc(V, x, num);
        else x=0;
    }
    if(V[num][0]==0){
        if(p1<p2){
            ans=0;
        }
    }
    if(turn) p1-=num;
    else p2-=num;
    turn=!turn;
}   
/*

*/

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    
    vector<vector<int>> V(100005); 
    for(int i=1; i<N; ++i){
        int a, b;
        cin>>a>>b;
        V[a].push_back(b);
        V[b].push_back(a);
    }
    
    for(int i=1; i<=N;++i){
        ans=1;
        score_calc(V,i,i);
        cout<<ans<<"\n";
    }
}
