#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    double arr[9]={};
    int N;
    cin>>N;
    while(N>0){
        if(N%10==6||N%10==9)
        arr[6]+=0.5;
        else
        arr[N%10]++;
        
        N/=10;
    }
    double max=0;
    
    for(int i=0; i<9;i++){
        if(arr[i]>max)
        max=arr[i];
    }
    cout<<ceil(max);
}