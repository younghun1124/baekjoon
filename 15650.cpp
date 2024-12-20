#include <bits/stdc++.h>
using namespace std;

int arr[9];
bool isused[9];
int n,m;

void func(int k){
    if(k==m){
        for(int i=0; i<m; i++)cout<<arr[i]<<' ';
        cout<<'\n';
        return;
    }
    for(int i=k+1; i<=n; i++){
        
        if(!isused[i]){
            arr[k]=i;
            isused[i]=1;
            func(k+1);
            isused[i]=0;
        }
    }      
}

/*
1 
3 
*/

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin>>n>>m;
    func(0);
}

