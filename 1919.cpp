#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s1, s2;
    cin>>s1>>s2;
    int arr[26]={};
    int ans;
    for(char c: s1){
        arr[c-'a']++;
    }
    for(char c: s2){
        arr[c-'a']--;
    }
    for(int a :arr){
        ans+=abs(a);
    }
    cout<<ans;
}