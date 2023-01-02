// 23.01.02 https://www.acmicpc.net/problem/11047
#include <cstdio>

int main()
{
  int N, money;
  scanf("%d %d", &N, &money);

  int arr[N];
  for (int i = 0; i < N; i++)
  {
    int k;
    scanf("%d", &k);
    arr[i] = k;
  }

  int count = 0; // 동전의 개수
  for (int i = N - 1; i >= 0; i--)
  {
    int tmpM = money;
    while (tmpM > 0)
    {
      tmpM -= arr[i];
      if (tmpM >= 0)
      {
        count++;
      }
    }
    if (tmpM == 0)
    {
      break;
    }
    else
    {
      money = (tmpM + arr[i]);
    }
  }

  printf("%d", count);
  return 0;
}
