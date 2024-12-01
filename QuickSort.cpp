#include <bits/stdc++.h>
using namespace std;
int med[2];//중앙값을 찾아내기 위해 후보들을 저장하는 리스트 생성
vector<int> pvarr; 
int get_med(int A[], int left, int right){//3중앙값을 찾는 함수, 리스트에서 중앙값이 있는 인덱스를 반환한다.
    med[0]=A[left]; //배열의 최좌측 값 얻기
    med[1]=A[(left+right)/2]; //배열의 중간 인덱스 값 얻기
    med[2]=A[right]; //배열의 최 우측값 얻기
    sort(med, med+3); //중앙값 리스트 정렬
    if(med[1]==A[left])//중앙값이 리스트의 좌측이라면
        return left; //좌측 인덱스 반환
    else if(med[1]==A[right]) //중앙값이 리스트 우측이라면
        return right;//우측 인덱스 반환
    else// 둘다 아니라면
        return (left+right)/2; //가운데 인덱스 반환
}
void QuickSort(int A[],int left,int right){//Quick 정렬 함수, 정렬할 리스트와 좌 우측 끝단 인덱스를 인자로 받는다.
    if(left<right){//왼쪽이 우측보다 작으면, 즉 아직 끝점교차가 일어나지 않으면, 아직 정렬할 것이 남아있는 배열이라면
       int pidx=get_med(A,left,right); //피봇의 인덱스 값을 pidx에 저장(3중앙값)
       int pv=A[pidx]; //피봇의 값을 pv에 저장
       pvarr.push_back(pv); //추후 선택했던 피벗을 쭉 출력하기 위해 pvarr에 얻은 pv저장
       A[pidx]=A[left]; //
       A[left]=pv; // 피벗과 최좌측 값 스왑
       int high=right; //스왑을 위한 높은쪽을 가리키는 값
       int low=left+1; //스왑을 위한 낮은쪽을 가리키는 값, 최좌측값은 피벗이므로 +1 해준다.
       while(A[low]<pv) low++; //low가 가리키는 값이 피벗보다 작다면 패스(low값 증가)
       while(A[high]>pv) high--; //high가 가리키는 값이 피벗보다 크다면 패스(high감소) 
       //while문에 진입하기 전에 미리 high와 low를다루는 이유는 그래야 while 조건문을 통과하기 때문

         while(low<high){    //low가 high보다 작다면, 아직 피벗기준 스왑이 끝까지 완료되지 않았다면
            int tmp=A[low]; //
            A[low]=A[high]; // 
            A[high]=tmp; //low와 high에 들어있는 값을 바꾼다. 이후 반복
            while(A[low]<pv) low++; //low가 가리키는 값이 피벗보다 작다면 패스(low값 증가)
            while(A[high]>pv) high--; //high가 가리키는 값이 피벗보다 크다면 패스(high감소)     
    }   
    A[left]=A[high]; //
    A[high]=pv; // 다시 피벗을 원래 자리로 돌려놓음

    QuickSort(A,left,high-1); //피벗기준 좌측 배열에 대해 재귀적 퀵정렬
    QuickSort(A,high+1,right); //피벗기준 우측 배열에 대해 지귀적 퀵정렬
    }
    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;//입력받을 N
    int arr[100000];// 입력받은 N 개의 배열을 저장할 배열
    
    cin>>N; //N에 입력값 저장
    int left=0; //제일 좌측 인덱스 0으로 설정
    int right=N; //제일 우측 인덱스 N으로 설정
    for(int i=0; i<N; i++)
        cin>>arr[i]; //리스트에 N번 반복하며 초기 배열을 입력한다.
    QuickSort(arr,0,N-1); //0부터 n-1 까지 quicksort 실행
    for(int i=0; i<N; i++)
     cout<<arr[i]<<' '; //정렬된 배열 출력
    cout<<'\n';
    for(auto c:pvarr) 
    cout<<c<<' '; //선택했던 피벗리스트 출력
    
}