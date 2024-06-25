#include <bits/stdc++.h>
using namespace std;
 int arr[2000001]={};
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    int x, ans=0;
   
    int a;
    for(int i=0; i<N; i++){
        cin>>a;
        arr[a]=1;
    }
    cin>>x;


    for(int i=1; i<(x+1)/2; i++){
        if(arr[i]&arr[x-i]){            
            ans++;
        }
        
    }
    cout<<ans;
}