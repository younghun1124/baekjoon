#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, L;
    cin>>N>>L;
    int min=1000000005;
    int nxtmin=1000000005;
    int minlife=0;
    int nxtminlife=0;
    while(N--){
        int input;
        cin>>input;
        if(input<=min){
            min=input;
            minlife=L;
        }else if(input<=nxtmin){
            nxtmin=input;
            nxtminlife=L;
        }
        cout<<min<<" ";
        nxtminlife--;
        minlife--;
        if(!minlife){
        min=nxtmin;
        minlife=nxtminlife;
        nxtmin=1000000005;
        nxtminlife=L;
        }
        if(!nxtminlife){        
        nxtminlife=L;
        nxtmin=1000000005;
        }   
        
    }
}