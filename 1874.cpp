#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    stack<int> S;
    string ans="";
    int nextnum=1;
    while(N--){
        int input;
            cin>>input;
        while(true){
            if(input>=nextnum){
                S.push(nextnum++);
                ans+="+\n";
            }else{
                if(S.top()==input){
                    S.pop();
                    ans+="-\n";
                    break;
                }else{
                    cout<<"NO";
                    return 0;
                }
            }
    }
}
 cout<<ans;
}