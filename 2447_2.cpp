// Authored by : cpprhtn
// Co-authored by : BaaaaaaaaaaarkingDog
// http://boj.kr/1e1d8717951a425c94049401b38053b6
#include <bits/stdc++.h>
using namespace std;

void print_star(int i, int j, int num) {
  if ((i / num) % 3 == 1 && (j / num) % 3 == 1) //빈공간을 찾을 조건, 현재 좌표가 빈공간이라면 빈공간 프린트
    cout << ' ';
  else {
    if (num / 3 == 0)  //
      cout << '*';
    else
      print_star(i, j, num / 3); //더 작은 3*3 범위로 나눈다.
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int num;
  cin >> num;
  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) print_star(i, j, num);
    cout << '\n';
  }
}