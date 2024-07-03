#include <bits/stdc++.h>
using namespace std;
int arr[1000005];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    for(int i=0; i<N; ++i){
        cin>>arr[i];
    }
    stack<int> S;
    string ans="";
    for(int i=N-1; i>=0; --i){
        int input=arr[i];        
        while(true){
            if(!S.empty()&&S.top()>input){
                ans=to_string(S.top())+" "+ans;
                S.push(input);
                break;
            }
            if(!S.empty()&&S.top()<=input){
                S.pop();                
            }
            if(S.empty()){
                ans="-1 "+ans;
                S.push(input);     
                break;
            }
        }     
    }
    cout<<ans;
    
}