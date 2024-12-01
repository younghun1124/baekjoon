/*trumino algorithm*************************************
1. 중심을 기준으로 1,2, 3, 4구역을 돌며 비어있는지 체크
2. 차있는 곳을 제외한 빈 구역 3곳을 하나씩 체크하기
3. 다시 재귀 호출 -> DFS의 탐색구조를 가짐
*******************************************************/
#define X first
#define Y second

#include<iostream>
#include<cmath>
#include<cstdlib>
#include <bits/stdc++.h>
using namespace std;
int siz;
int num;

//주어진 범위 (x1, y1) ~ (y1, y2)를 탐색하며 모두 비어있으면 true, 하나라도 차있으면 false
bool check(int** arr, int x1, int y1, int x2, int y2) {
	for (int i = x1; i <= x2; i++) {
		for (int j = y1; j <= y2; j++) {
			if (arr[i-1][j-1] != 0) return false;
		}
	}
	return true;
}

void tromino(int** map, int& num, int size, int x, int y) {
	if (size == 1) return;
	num++;
	size /= 2;
	x -= size;
	y -= size;

	pair<int, int> dir[4] = { {x, y}, {x+1, y}, {x, y+1}, {x+1, y+1} };

	bool pos1 = check(map, x - (size - 1), y - (size - 1), x, y);  // 1구역 탐색
	bool pos2 = check(map, x + 1, y - (size - 1), x + size, y);  // 2구역 탐색
	bool pos3 = check(map, x - (size - 1), y + 1, x, y + size);  // 3구역 탐색
	bool pos4 = check(map, x + 1, y + 1, x + size, y + size); // 4구역 탐색
	//빈곳 num표시
	bool pos[4] = { pos1, pos2, pos3, pos4 };
	for (int i = 0; i < 4; i++) {
		if (pos[i] == true)  map[dir[i].X-1][dir[i].Y-1] = num;
	}

	//이후 재귀 호출(분할 정복)   
	tromino(map, num, size, x, y);
	tromino(map, num, size, x + size, y);
	tromino(map, num, size, x, y + size);
	tromino(map, num, size, x + size, y + size);	
}


int main(void) {
	int k, m, n;
	cin >> k;
	siz = pow(2, k);
	int** map = new int* [siz];
	for (int i = 0; i < siz; i++) {
		map[i] = new int[siz];
		memset(map[i], 0, siz*4);
	}

	cin >> m >> n;  //(채워지지 않는 한 곳 입력)
	map[m-1][n-1] = -1;
	tromino(map, num, siz, siz, siz);

	for (int i = 0; i < siz; i++) {
		for (int j = 0; j < siz; j++) {
			cout << map[i][j] << "  ";
		}
		cout << "\n";
	}
	return 0;
}