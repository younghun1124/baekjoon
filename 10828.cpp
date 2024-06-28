#include <bits/stdc++.h>
using namespace std;

int stk[10001];
int pos=0;
int empty(){
    if(pos) return 0;
    else return 1;
}
int top(){
    if(empty()) return -1;
    return stk[pos-1];
}
void push(int a){
    stk[pos++]=a;
}

int pop(){
    int val=top();
    if(val==-1) return val; 
    pos--;
    return val;
    
}

int size(){
    return pos;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N; 
    cin>>N;
    while(N--){
        string op;
        cin>>op;
        if(op=="push"){
            int a;
            cin>>a;
            push(a);
        }else if (op=="pop")
        {
            cout<<pop()<<'\n';
        }else if (op=="size"){
            cout<<size()<<'\n';
        }else if (op=="empty"){
            cout<<empty()<<'\n';
        }else if (op=="top"){
            cout<<top()<<'\n';
        }
        
    }  
}