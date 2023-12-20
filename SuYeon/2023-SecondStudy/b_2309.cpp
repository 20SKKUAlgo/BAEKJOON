/*
9개의 숫자 중에서 7개의 합이 100인 것을 찾는 것보다 아닌 2개를 찾는 것이 더 빠르겠지..?
먼저 모든 합을 구하고 거기서 100을 빼서 차이를 계산하자
9개의 숫자 중에서 2개의 합이 차이인 것을 찾자...
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> height_vect;

    int h, diff=0;
    for(int i=0;i<9;i++){
        cin >> h;
        diff += h;
        height_vect.push_back(h);
    }
    sort(height_vect.begin(), height_vect.end()); // 오름차순 정렬
    diff -= 100; // 두 개의 합이 diff인 것을 찾아야 함

    for(int i=0;i<9;i++){
        for(int j=i+1;j<9;j++){
            if(height_vect[i]+height_vect[j]==diff){ // 두개의 합이 diff인 것 찾음
                height_vect.erase(height_vect.begin() + i); // 두 숫자 중 첫번째 거 제거
                height_vect.erase(height_vect.begin() + j-1); // 두 숫자 중 두번째 거 제거 (i보다 j가 큰 것을 감안하여 i를 제거하면 앞에거 하나가 없어지므로 j에서 1을 뺀 index 제거)
                for(auto h:height_vect)
                {
                    cout << h << endl; // 답 출력
                }
                return 0;
            }
        }
    }
}