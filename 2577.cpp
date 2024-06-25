#include <bits/stdc++.h>
using namespace std;
int arr[10];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, c,abc;
    cin>>a>>b>>c;
    abc=a*b*c;
    while(abc>0){
        arr[abc%(10)]++;
        abc=abc/10;
        }
   
    for(auto i:arr){
        cout<<i<<'\n';
    }
    
}