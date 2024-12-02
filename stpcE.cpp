#include <bits/stdc++.h>
using namespace std;
void ABB(string S, int k, int j){   
    string nS=S;
    bool isbreak=false;  
    if(j<0) j=0;   
    for(int i=j; i<k-2; i++){
        if(S.substr(i,3)=="ABB"){
        if(i+3>k)
         nS=S.substr(0,i)+"BA";
        else
         nS=S.substr(0,i)+"BA"+S.substr(i+3);
        ABB(nS,k-1,i-2);
        isbreak=true;
        return;
        }
        if(i==k-3) isbreak=true;
    }
    if(isbreak)
    cout<<nS<<'\n';
}
int main(void){ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    while(N--){
        int k;
        cin>>k;
        string S;
        cin>>S;
        if(S.length()<3){
            cout<<S<<'\n';
        continue;
        }
        
        if(S=="ABB"){
        cout<<"BA\n";
        continue;
        }
        ABB(S,k,0);
    }

}