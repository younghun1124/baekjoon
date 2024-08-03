#include <bits/stdc++.h>
using namespace std;
int arr[3000][3000];
int ans[3];

bool check(int n, int idx, int idx2){
    int tmp=arr[idx][idx2];
    for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                if(tmp!=arr[i+idx][j+idx2])
                    return false;
                    return true;
    
}

void func(int n, int idx, int idx2){
    if(check(n,idx,idx2)){
        ans[arr[idx][idx2]+1]++;
        return
    }
    for(int i=0; i<3; ++i)
            for(int j=0; j<3; ++j)
             func(n/3, i*n/3+idx, j*n/3+idx2);
        return;
    
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
            cin>>arr[i][j];
    func(n,0,0);
    for(auto i:ans) cout<<i<<'\n';
    
}