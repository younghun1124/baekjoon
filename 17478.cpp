#include <bits/stdc++.h>
using namespace std;

void func(int n, int total){
    string s="";
    for(int i=0; i<total-n; ++i) s+="____";
    cout<<s;
    cout<<"\"����Լ��� ������?\""<<'\n';
    if(n==0){
        cout<<s;
        cout<<"\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n";
        cout<<s;
        cout<<"��� �亯�Ͽ���.\n";
        return;
    }
    cout<<s;
    cout<<"\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n";
    cout<<s;
    cout<<"���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n";
    cout<<s;
    cout<<"���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n";
    func(n-1,total);
    cout<<s;
    cout<<"��� �亯�Ͽ���.\n";
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    cout<<"��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n";
    func(n, n);
}