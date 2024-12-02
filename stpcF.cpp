#include <bits/stdc++.h>
using namespace std;
vector<char> S;
void push_B(){
    if(!S.empty()){
        if(S.back()=='C'){
            S.pop_back();
            push_B();
            S.push_back('A');
        }else if(S.back()=='A'){
            S.pop_back();
            S.push_back('C');
        }else{
            S.push_back('B');
        }
    }else{
        S.push_back('B');
    }
}
int main(void){ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    while(N--){
        int k;
        cin>>k;
        while(k--){
            char input;
            cin>>input;
            if(input=='B') push_B();
            else S.push_back('A');
        }
        for(auto c:S) {
            if(c=='C')
            cout<<"BA";
            else cout<<c;
            }cout<<'\n';
        
    }

}