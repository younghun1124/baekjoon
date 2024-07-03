#include <bits/stdc++.h>
using namespace std;
int arr[1000005];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;   
    stack<pair<int, int>> S;  
  
    for(int i=0; i<N; ++i){
        int input;
        cin>>input;
        while(true){
            if(!S.empty()&&S.top().second<input){
                arr[S.top().first]=input;
                S.pop();
            } 
            else {
                S.push({i,input}); 
                break;
            }            
        }            
    }
    for(int i=0; i<N; ++i){
        if(arr[i]==0) cout<<"-1 ";
        else cout<<arr[i]<<" ";
    }    
}