#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N=0;
    
    cin>>N;
    while(N--){
        list<char> L;
        list<char>::iterator iter=L.begin();
        string s;
        cin>>s;
        for(auto c:s){
            switch(c){
                case '<':
                if(iter!=L.begin()) iter--;
                break;
                case '>':
                if(iter!=L.end()) iter++;
                break;
                case '-':
                if(iter!=L.begin()){
                    iter--;
                    iter=L.erase(iter);
                }
                break;
                default:
                L.insert(iter,c);
            }
        }
        for(auto c:L){
            cout<<c;
        }
        cout<<endl;
        

        
    }
}