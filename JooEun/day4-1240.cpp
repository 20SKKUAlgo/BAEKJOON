// 2023.01.05 시작 https://www.acmicpc.net/problem/1240
// 틀린 코드임.

#include <cstdio>
#include <vector>

struct node
{
  int destination;
  int distance;
};

// dfs 참고 https://better-tomorrow.tistory.com/entry/DFS-BFS-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0
void dfs(std::vector<node> *graph, std::vector<bool> &visited, std::vector<bool> &turn, int start, int end, int prevD, int &distance)
{
  visited[start] = true;
  for (int i = 0; i < graph[start].size(); i++)
  {
    int nextN = graph[start][i].destination;
    int dis = graph[start][i].distance;

    if (!visited[nextN])
    {
      distance += dis;
      turn[start] = true;
      if (nextN == end)
      {
        break;
      }
      dfs(graph, visited, turn, nextN, end, dis, distance);
    }
    else
    {
      // visitend[nextN] == true
      // if(graph[start].size() == 1)

      distance -= prevD;
    }
  }
}

int main()
{
  int nodeNum, askNum;
  scanf("%d %d", &nodeNum, &askNum);

  // 그래프 생성
  // 참고 https://twpower.github.io/72-implement-graph-in-cpp
  std::vector<node> graph[nodeNum + 1]; // 1부터 시작하기 위해 1더함. 2중 배열
  for (int i = 0; i < nodeNum - 1; i++)
  {
    int start, end, distance;
    scanf("%d %d %d", &start, &end, &distance);

    // 양방향으로 만들기 위해 2개 노드 생성
    node n1;
    n1.destination = end;
    n1.distance = distance;
    node n2;
    n2.destination = start;
    n2.distance = distance;

    graph[start].push_back(n1);
    graph[end].push_back(n2);
  }

  for (int i = 0; i < askNum; i++)
  {
    int aN1, aN2;
    scanf("%d %d", &aN1, &aN2);
    std::vector<bool> visited(nodeNum + 1);
    std::vector<bool> turn(nodeNum + 1);

    int resultDistance = 0;
    dfs(graph, visited, turn, aN1, aN2, 0, resultDistance);
    printf("%d\n", resultDistance);
  }
  return 0;
}
