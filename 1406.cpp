#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    int M=0;
    char command;
    cin>>s>>M;
    list<char> L;
    for(auto c:s){
        L.push_back(c);
    }
    auto t=L.end();
    while(M--){
         cin>>command;
        switch (command)
        {
        case 'L':
            if(t!=L.begin())t--;
            break;
        case 'D':
            if(t!=L.end())t++;
            break;
        case 'B':
            if(t!=L.begin()){
                t--;
                t=L.erase(t);
                      
                
            }             
            
            break;
        case 'P':
            char c;
            cin>>c;        
            L.insert(t,c);
            break;
        }
    }
    for(auto c:L){
        cout<<c;
    } 
}