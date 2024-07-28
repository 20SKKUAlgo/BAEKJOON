/*
* 문제 이해하는데 좀 걸림..
* 그냥 각 바구니에 들어간 마지막 공 숫자 출력하는 것임...  
* 결과: 맞았습니다.
*/

#include <iostream>

using namespace std;

int main() {
    int n, m;
    int arr[101] = { 0, }; //1 ≤ N ≤ 100이므로 배열의 인덱스는 101로, 값은 0으로 초기화 
    int a, b, c;
    
    // 첫번째 줄의 N과 M 입력받기
    cin >> n >> m;

    // 두번째 줄부터 M번 입력받기
    for(int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        for(int k = a; k <= b; k++) {
            arr[k] = c;
        }
    }

    // 출력
    for(int i = 1; i <= n; i++) {
        cout << arr[i] << ' ';
    }
    return 0;
}