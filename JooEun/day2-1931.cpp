// 2023.01.03 https://www.acmicpc.net/problem/1931
// 틀린 상태임 :: 왜 틀렸을까 ㅎㅎㅎ

#include <cstdio>
#include <iostream>
#include <algorithm>

struct date
{
  int start;
  int end;
  int timeDiff;
};

// https://it-earth.tistory.com/129 참고
bool compare(const date &d1, const date &d2)
{
  if (d1.timeDiff == d2.timeDiff)
  {
    return d1.start <= d2.start;
  }
  else
  {
    if((d1.timeDiff == 0 && d2.timeDiff==1) || (d2.timeDiff == 0 && d1.timeDiff==1)){
      return d1.start < d2.start;
    }else{
      return d1.timeDiff < d2.timeDiff;
    }
  }
}

int main()
{
  int N;       // 회의 수
  scanf("%d", &N);
  date arr[N]; // 회의 시작, 끝시간, 두 시간의 차이를 저장

  // 값 전달받기
  for (int i = 0; i < N; i++)
  {
    int start, end;
    scanf("%d %d", &start, &end);
    arr[i].start = start;
    arr[i].end = end;
    arr[i].timeDiff = end - start;
  }
  
  // time diff를 기준으로 정렬
  std::sort(arr, arr + N, compare);

  // 정렬되어있는 상태를 확인하기 위함
  // for (int i = 0; i < N; i++)
  // {
  //   std::cout << i << " time diff: " << arr[i].timeDiff << " start: " << arr[i].start << "\n";
  // }

  // 회의 개수 확인하기
  int count=1;
  for (int i=1; i<N; i++){
    if((arr[i-1].end) <= arr[i].start){
      count++;
    }
  }
  printf("%d", count);
  return 0;
}
