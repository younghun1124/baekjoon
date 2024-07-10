/*
문자열 압축 해제
시간 제한: 1초
엘리스 토끼는 문자열을 직접 압축 해제하려고 합니다.

압축되지 않은 문자열 S가 주어졌을 때, 이 문자열 중 어떤 부분 문자열은 K(Q)와 같이 압축할 수 있습니다. 이것은 Q라는 문자열이 K 번 반복된다는 뜻입니다. K는 한 자릿수의 정수이고, Q는 0자리 이상의 문자열입니다.

예를 들면, 53(8)은 다음과 같이 압축을 해제할 수 있습니다.

53(8) = 5 + 3(8) = 5 + 888 = 5888

압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하세요.
*/
#include <bits/stdc++.h>
using namespace std;
stack<int> st;

void stack_top_sum(int i){
    if(st.top()==0){
        st.push(i);
    }else{
         int temp=st.top()+i;
    st.pop();
    st.push(temp);
    }
   
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string S;
    cin>>S;
    
    bool multiple_flag=false;
    st.push(0);
    for(int i=S.length()-1; i>=0; --i){
        char c= S[i];
        if(multiple_flag){
            int temp=st.top();
            st.pop();
            stack_top_sum(temp*(c-'0'));
            multiple_flag=false;
        }else if(c==')'){
            st.push(0);
        }else if(c=='('){
            multiple_flag=true;
        }else{
            stack_top_sum(1);
        }
    }
    cout<<st.top();
   

}

