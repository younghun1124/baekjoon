#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int weight;
    int value;
    int index; // 원래 인덱스
};

// 가치/무게 비율에 따라 정렬하기 위한 비교 함수
bool compare(Item a, Item b) {
    return (double)a.value / a.weight > (double)b.value / b.weight; // 비율이 높은 순으로 정렬
}

void fractional_knapsack(int n, vector<Item>& items, int capacity) {
    // 가치/무게 비율이 높은 순으로 정렬
    sort(items.begin(), items.end(), compare);
    
    double total_value = 0; // 배낭에 담긴 총 가치
    vector<pair<int, double>> selected_items; // 선택된 물건과 그 비율

    for (int i = 0; i < n; i++) {
        int weight = items[i].weight;
        int value = items[i].value;
        int idx = items[i].index;

        if (capacity >= weight) {
            // 배낭에 물건을 전부 담을 수 있는 경우
            selected_items.push_back({idx, 1.0});
            total_value += value;
            capacity -= weight;
        } else {
            // 배낭에 부분적으로 담아야 하는 경우
            double fraction = (double)capacity / weight;
            selected_items.push_back({idx, fraction});
            total_value += value * fraction;
            break; // 배낭 용량을 채웠으므로 반복 종료
        }
    }

    // 선택된 물건과 비율 출력
    sort(selected_items.begin(), selected_items.end()); // 인덱스에 따라 정렬
    for (const auto& item : selected_items) {
        cout << item.first << " " << item.second << endl;
    }
    
    // 배낭에 담긴 총 가치 출력
    cout << (int)total_value << endl;
}

int main() {
    int n; // 물건의 개수
    cin >> n;

    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].value;
        items[i].index = i; // 원래 인덱스 저장
    }

    int capacity; // 배낭의 용량
    cin >> capacity;

    fractional_knapsack(n, items, capacity);

    return 0;
}
