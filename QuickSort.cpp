#include <bits/stdc++.h>
using namespace std;
int med[2];
vector<int> pvarr;
int get_med(int A[], int left, int right){
    med[0]=A[left];
    med[1]=A[(left+right)/2];
    med[2]=A[right];
    sort(med, med+3);
    if(med[1]==A[left])
        return left;
    else if(med[1]==A[right])
        return right;
    else
        return (left+right)/2;
}
void QuickSort(int A[],int left,int right){
    if(left<right){
       int pidx=get_med(A,left,right);
       int pv=A[pidx];
       pvarr.push_back(pv);
       A[pidx]=A[left];
       A[left]=pv;
       int high=right;
       int low=left+1;
       while(A[low]<pv) low++;
       while(A[high]>pv) high--;
         while(low<high){    
            int tmp=A[low];
            A[low]=A[high];
            A[high]=tmp;
            while(A[low]<pv) low++;
            while(A[high]>pv) high--;            
    }   
    A[left]=A[high];
    A[high]=pv;

    QuickSort(A,left,high-1);
    QuickSort(A,high+1,right);
    }
    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    int arr[100000];//이거 나중에 늘리자!!
    
    cin>>N;
    int left=0;
    int right=N;
    for(int i=0; i<N; i++)
        cin>>arr[i];
    QuickSort(arr,0,N-1);
    for(int i=0; i<N; i++)
     cout<<arr[i]<<' ';
    cout<<'\n';
    for(auto c:pvarr)
    cout<<c<<' '; 
    
}