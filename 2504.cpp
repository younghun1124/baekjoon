#include <bits/stdc++.h>
using namespace std;
stack<string> S;

bool stack_calc(string op, int val){
    int tmp=0;
    while(!S.empty()&&(S.top()!="("||S.top()!="[")){
        if(op==")"||S.top()=="["){
            return false;
        }else if(op=="]"||S.top()=="("){
            return false;
        }
        tmp+=stoi(S.top());
        S.pop();
    }
    S.push(tmp+val);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string a;
    cin>>a;
    
    for(string s:a){
        if(s=="("||s=="[") S.push(s);
        else if(s==")"){
            if(!S.empty()&&S.top()=="("){
                S.pop();
            }
        }
    }
}