#include <bits/stdc++.h>
using namespace std;
//stl list ver
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, K;
    cin>>N>>K;
    list<int> L;    
    for(int i=1; i<=N; i++){
        L.push_back(i);    
    }
    list<int>::iterator iter=L.begin();
    cout<<"<";
    while(N--){
        for(int i=1; i<K; i++){
                iter++;
            if(iter==L.end()){            
                iter=L.begin();
            }
        }  
        cout<<*iter;
        if(N>0) cout<<", ";
        iter=L.erase(iter);
        if(iter==L.end()) iter=L.begin();          
    }
    cout<<">";
}