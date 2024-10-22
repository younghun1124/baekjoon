#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    vector<int> p,s;
    for(int i=0; i<N; i++){
        int input;
        cin>>input;
        p.push_back(input);
    }
     for(int i=0; i<N; i++){
        int input;
        cin>>input;
        s.push_back(input);
    }
    for(int i=0; i<N; i++){
        int x=i;
        long long ans=0;
        while(!(x<0||x>=N)){
            ans+=s[x];
            x=p[x];
        }
        cout<<ans<<' ';
    }
}