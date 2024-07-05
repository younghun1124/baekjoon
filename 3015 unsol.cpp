#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    stack<long long> S;
    long long ans=0;    
    while(N--){
        long long input;
        cin>>input; 
        
            while(!S.empty()&&S.top()<input){            
            S.pop();
            ans++;     
            }        
       int same=0;
        while(!S.empty()){            
            if(S.top()==input){
                ans++;
                same++;
                S.pop();
            }
            if(S.top()>input){
                ans++;                
                break;
            }
        }
        while(same--){
            S.push(input);
        }
        S.push(input);        
    }
    cout<<ans;
}