/*
9���� ���� �߿��� 7���� ���� 100�� ���� ã�� �ͺ��� �ƴ� 2���� ã�� ���� �� ��������..?
���� ��� ���� ���ϰ� �ű⼭ 100�� ���� ���̸� �������
9���� ���� �߿��� 2���� ���� ������ ���� ã��...
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
    sort(height_vect.begin(), height_vect.end()); // �������� ����
    diff -= 100; // �� ���� ���� diff�� ���� ã�ƾ� ��

    for(int i=0;i<9;i++){
        for(int j=i+1;j<9;j++){
            if(height_vect[i]+height_vect[j]==diff){ // �ΰ��� ���� diff�� �� ã��
                height_vect.erase(height_vect.begin() + i); // �� ���� �� ù��° �� ����
                height_vect.erase(height_vect.begin() + j-1); // �� ���� �� �ι�° �� ���� (i���� j�� ū ���� �����Ͽ� i�� �����ϸ� �տ��� �ϳ��� �������Ƿ� j���� 1�� �� index ����)
                for(auto h:height_vect)
                {
                    cout << h << endl; // �� ���
                }
                return 0;
            }
        }
    }
}