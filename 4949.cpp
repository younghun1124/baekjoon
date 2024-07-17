#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    
    string a;       
    while(true){
        stack<char> S;
        getline(cin,a); 
        if(a==".") break;
        string ans="yes";        
        for(char input:a){
            if(input=='['||input=='(') S.push(input);
            else if(input==']'){
                if(!S.empty()&&S.top()=='[') S.pop();
                else{
                    ans="no";
                    break;
                }
            }else if(input==')'){
                if(!S.empty()&&S.top()=='(') S.pop();
                else{
                    ans="no";
                    break;
                }
            }
        }
        if(!S.empty()) ans="no";
        cout<<ans<<"\n";
    }
    
}