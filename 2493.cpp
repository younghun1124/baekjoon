#include <bits/stdc++.h>
using namespace std;
#define height first
#define index second
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    stack<pair<int,int>> S; 
    int order=1;
    while(N--){
        int hit=0;  
        int input;        
        cin>>input;        
            while(!S.empty()){
                if(S.top().height>input){
                    hit=S.top().index;
                    break;
                }else{
                    S.pop();
                }
            }
        S.push({input,order++});       
        cout<<hit<<" ";
    }
    
}