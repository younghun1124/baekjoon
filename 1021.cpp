#include <bits/stdc++.h>
using namespace std;
deque<int> dq;
void move_left(){
    dq.push_back(dq.front());
    dq.pop_front();
}
void move_right(){
    dq.push_front(dq.back());
    dq.pop_back();
}
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
   
    int N, M;
    cin>>N>>M;
    
}