/*
정리 정돈을 좋아하는 k씨
시간 제한: 1초
정리 정돈을 좋아하는 k씨의 본명은 아무도 모릅니다. 사람들은 k씨의 특이한 행동 2가지 때문에 그를 '정리 정돈을 좋아하는 k씨'라고 부릅니다. 그 두 가지 행동은 그가 숫자를 정리하는 일을 하면 아무 규칙없이 나열되어 있는 숫자중 범위를 정한 후 무조건 오름차순으로 정리한다는 것, 그리고 오름차순으로 정리된 숫자 중 k번째 숫자를 선택한다는 것입니다

예를 들어 a={1,7,6,8,1,6,4,5}라는 수열이 있습니다. 정리정돈을 좋아하는 k씨는 범위를 2에서 5로 정하고, k를 2라고 정했습니다.
그러면 k 
a
​
 ={7,6,8,1}이 되고, 이것을 오름차순으로 정리를 하면 k 
a
​
 ={1,6,7,8}이 됩니다. 그리고 k씨는 2번째인 6을 선택합니다.

배열 a가 주어지고, k씨가 일을 한 횟수가 주어졌을 때, k씨가 고른 숫자를 출력하는 프로그램을 작성하세요
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> V;
    int n, m;
    cin>>n>>m;
    while(n--){
        int input;
        cin>>input;
        V.push_back(input);
    }    
    
    while(m--){
        
        int first, last, k;
        cin>>first>>last>>k;
        vector<int> tmpV(V.begin()+first-1,V.begin()+last);
        
        sort(tmpV.begin(),tmpV.end());
        cout<<tmpV[k-1]<<endl;

    }
}

