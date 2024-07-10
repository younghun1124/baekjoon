#include <bits/stdc++.h>
using namespace std;

deque<int> dq;
int tempcnt=0;
void move_L(){
    dq.push_back(dq.front());
    dq.pop_front();
}
void move_R(){
    dq.push_front(dq.back());
    dq.pop_back();
}
void move_until_find(int input){
    tempcnt=0;
    while(!(dq.front()==input)){
        move_R();   
        tempcnt++;
    }
    
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
   
    int N, M, ans=0;

    cin>>N>>M;
    while(N--){
        dq.push_front(N+1);
    }
    while(M--){
        int input;
        cin>>input;
        move_until_find(input);
        if(tempcnt<=dq.size()/2){
            ans+=tempcnt;
        }else{
            ans+=(dq.size()-tempcnt);
        }
        dq.pop_front();
    }
    cout<<ans;
}