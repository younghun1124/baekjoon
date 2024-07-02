#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    vector<int> V;
    while(N--){
        int input;
        cin>>input;
        V.push_back(input);
    }
    for(int i=0; i<V.size(); i++){
        int hit=0;
        for(int j=i-1; j>=0; j--){
            if(V[j]>V[i]){
                hit=j+1;
                break;
            }
        }
        cout<<hit<<" ";
    }
}