#include <bits/stdc++.h>
using namespace std;

bool check_valid(string S){
    stack<char> st;
    for(char c:S){
        if(c=='('||c=='[') st.push(c);
        else if(c==')'){
            if(!st.empty()&&st.top()=='(') st.pop();
            else return false;
        }else if(c==']'){
            if(!st.empty()&&st.top()=='[') st.pop();
            else return false;
        }
    }
    if(st.empty()) return true;
    return false;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string a;
    cin>>a;    
    if(!check_valid(a)){
         cout<<0;
         return 0;
    }
    stack<int> st;
    for(char c:a){
        int tmp=0;
        if(c==')'){
            if(!st.empty()&&st.top()!=0){
                tmp+=st.top()*2;
                st.pop();
            }else tmp+=2;
            st.pop();
            while(!st.empty()&&st.top()!=0){
                tmp+=st.top();
                st.pop();
            }
            st.push(tmp);
        }else if(c==']'){
            if(!st.empty()&&st.top()!=0){
                tmp+=st.top()*3;
                st.pop();
            }else tmp+=3;
            st.pop();
            while(!st.empty()&&st.top()!=0){
                tmp+=st.top();
                st.pop();
            }
            st.push(tmp);
        }
        else st.push(0);
    }
    cout<<st.top();
}