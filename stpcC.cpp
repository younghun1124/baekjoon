#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int l,r,x;
    vector<int> v;
    cin>>l>>r>>x;
    for(int i=0; i<r-l+1; i++){
        v.push_back((l+i)|x);
    }
    sort(v.begin(),v.end());
    for(int i=0; i<r-l+1; i++){
        if(v[i]!=i){
            cout<<i;
            return 0;
        }        
    }
    cout<<v.back()+1;

}