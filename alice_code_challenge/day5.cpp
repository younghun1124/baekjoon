#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin>>N;
    int K=pow(2,N);
    vector<int> L;
    vector<int> Skip;
    Skip.push_back(0);
    int skiter=0;
    
    while(K--){
        int input;
        cin>>input;
        L.push_back(input);        
    }
    sort(L.begin(),L.end()); 
    
    vector<int>::iterator iter=L.begin();   
    while(N--){
        int ans=0;
        
        while(true){
            if (skiter==Skip.size()||Skip[skiter]!=*iter){                
                ans=*iter;
                cout<<ans<<" ";
                int s=Skip.size();                
                for(int i=0;i<s;++i){
                    Skip.push_back(Skip[i]+ans);           
                }               
                               
                break;
            }else if(Skip[skiter]==*iter){               
                skiter++;
                iter++;
            }
        }
    }
}

/*
입력 받은 수열정렬
최대값은 모든 수를 더한것
0 제외 최소값은 첫번째 원소
최대에서 최대보다 하나 작은거를 빼면? 첫번째 원소
최대에서 최대보다 두개 작은거를 빼면? 두번째 원소?
0 1(a1) 2 3 4 5 6 7(a1~an)
0 1(a1) 2(a2) 3 4(a3~an) 5 6(a2~an)

ex 1 5 6
1(1) 5(2) 6 6(3,n) 7 11(2,n) 12(1,n) 

ex 1 3 5 7
1(1) 3(2) 4(a1+a2) 5 6 7(4~N) 8 8 9 10 11 12(3~N) 13 15(2~N) 16(1~N)
최대에서 최소를 빼가면서 구한 원소로 만들 수 있는 조합 거르기?(계산이 너무 많지 않나)

ex 1 3 4 7
0 1(1) 3(2) 4(1+2) 4(3) 5(1+3) 7(2+3) 7(4) 8(1,4) 8(1,2,3) 10 11 11(3~n) 12 14(2~n) 15(1~n)

skip
0 + 1 + 3 4 + 4 5 7 8 +7 8 10 11 11 12 14 15
0 
0 1 3 4 4 5 7 7 8



*/
