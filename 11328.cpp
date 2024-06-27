#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    string a,b;
    
    while(N--){
        bool valid=true;
        cin>>a>>b;
        int arr[26]={};
        for(int c:b){
            arr[c-'a']++;
        }
        for(int c:a){
            arr[c-'a']--;
        }
        for(int c:arr){
            if(c!=0){
                valid=false;
                break;
            }
        }                       
        if(valid) cout<<"Possible\n";
        else cout<<"Impossible\n";
    }
}