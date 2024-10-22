#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    string s;
    cin>>N>>s;
    for(int i=0;i<N;i++){
        if(s[i]=='I')
        s[i]='i';
        else
        s[i]='L';
    }
    for(auto c:s)
    cout<<c;
}