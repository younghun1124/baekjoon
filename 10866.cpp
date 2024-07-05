#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    string op;
    deque<int> DQ;
    while(N--){
        cin>>op;
        if(op=="push_front"){
            int input;
            cin>>input;
            DQ.push_front(input);
        }else if(op=="push_back"){
            int input;
            cin>>input;
            DQ.push_back(input);
        }else if(op=="size"){
            cout<<DQ.size()<<"\n";
        }else if(op=="empty"){
            cout<<DQ.empty()<<"\n";
        }else if(op=="pop_front"){
            if(DQ.empty()) cout<<"-1\n";
            else{
                cout<<DQ.front()<<"\n";
                DQ.pop_front();
            }
        }else if(op=="pop_back"){
            if(DQ.empty()) cout<<"-1\n";
            else{
                cout<<DQ.back()<<"\n";
                DQ.pop_back();
            }
        }else if(op=="front"){
              if(DQ.empty()) cout<<"-1\n";
            else{
                cout<<DQ.front()<<"\n";                
            }
        }else if(op=="back"){
              if(DQ.empty()) cout<<"-1\n";
            else{
                cout<<DQ.back()<<"\n";                
            }
        }
    }
}