# 20200923

## Algorithm

### 강결합 컴포넌트(SCC; Strongly Connected Component)



#### 1)  강결합 컴포넌트(SCC; Strongly Connected Component)

##### 1) 강결합 컴포넌트란?

##### 

![사진1](https://user-images.githubusercontent.com/45934494/93757896-763d6e80-fc42-11ea-8121-eeefaa82eb0f.jpg)



* SSC 내의 임의의 두 정점 u, v 사이의 u -> v 경로와 v -> u 경로가 항상 존재.

* SSC 내의 임의의 정점 u와 외부의 임의의 정점 v 사이에 u -> v 경로와, v -> u 경로가 동시에 존재하는 경우는 없음.

  > 즉, SSC는 내부의 모든 정점에서 내부의 다른 모든 정점으로 갈 수 있는 최대 그룹이라고 할 수 있음.
  > 또한, 모든 방향성 그래프는 한개 이상의 SSC들로 분리될 수 있음.

* DFS 트리의 개념을 알아야 함.

  > DFS를 사용해서 강결합 컴포넌트를 분리하는 알고리즘.
  >
  > - Kosaraju's Algorithm
  > - Tarjan's Algorithm



##### 2) DFS 트리란?

![사진2](https://user-images.githubusercontent.com/45934494/93757947-8b1a0200-fc42-11ea-9568-43de81b0b8a3.png)



- 어떤한 그래프에서 DFS를 하는 과정을 트리로 나타낸 것.

- discovery time : 그 정점을 방문한 시간.

  > 정점 u의 discovery time을 dt[u]

* finish time : 그 정점의 모든 자식들을 방문하고 그 정점을 빠져나가는 시간.

  >  finish time을 ft[u]

- DFS를 통해 그래프의 간선들을 다음과 같이 분류할 수 있음.

    - Tree edge

      > 그래프의 간선들 중 DFS 트리에 속하는 간선들.
      >
      > 이 경우 dt[u] < dt[v], ft[u] > ft[v] 

    - back edge

      > 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 v가 u의 조상인 간선들.
      >
      > 즉 DFS 트리에서 거꾸로 조상한테 올라가는 간선.
      >
      > 이 경우 dt[u] > dt[v], ft[u] < ft[v]

    - forward edge

        > 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 u가 v의 조상인데 tree edge에 속하지 않는 간선들.
        >
        > 이 경우 dt[u] < dt[v], ft[u] > ft[v]

    - cross edge

        > 위의 3가지 간선에 해당하지 않는 간선들.
        >
        > 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 u가 v의 조상도 아니고, v가 u의 조상도 아닌 경우.
        >
        > 이 경우 dt[u] > ft[v]



- 모든 방향성 그래프의 간선들은 이 4가지 중 하나에 속하게 됨. 

![사진3](https://user-images.githubusercontent.com/45934494/93758332-3460f800-fc43-11ea-8bbc-00ab23d85cc2.jpg)

![사진4](https://user-images.githubusercontent.com/45934494/93758337-35922500-fc43-11ea-9d07-6e146dfbbfc7.jpg)



#### 2) Kosaraju's Algorithm

##### 

![사진1](https://user-images.githubusercontent.com/45934494/93757896-763d6e80-fc42-11ea-8121-eeefaa82eb0f.jpg)



* 위의 그래프를 Kosaraju's Algorithm을 통해 강결합 컴포넌트들로 분리하면
* 그래프에서 DFS를 하면서 각 정점의 finish time을 저장.

![사진5](https://user-images.githubusercontent.com/45934494/93758896-337c9600-fc44-11ea-8bf8-fa5ea39587c9.png)



* 그래프에서 모든 간선의 방향을 반대로 바꾼 역방향 그래프를 만듦.

![사진6](https://user-images.githubusercontent.com/45934494/93758898-34152c80-fc44-11ea-85ae-a35dff514a0e.png)



* finish time이 큰 정점부터, 즉 늦게 끝난 정점부터 역방향 그래프에서 DFS를 함.

  이 때 생기는 DFS 트리들이 각각 하나의 SCC.

![사진7](https://user-images.githubusercontent.com/45934494/93758899-34adc300-fc44-11ea-8b0a-5ef58090e15b.png)



* 진행 순서

  1. 1번 정점의 finish time이 가장 크기 때문에, 1번 정점부터 역방향 그래프에서 DFS를 함.

     4번 정점에서 더 이상 갈 곳이 없이 끝나게 됨.

  2. 아직 방문하지 않은 3, 5, 6번 정점들 중에 5번 정점의 finish time이 가장 크기 때문에,

     5번 정점에서 DFS를 시작하고 6번 정점을 방문하고 끝나게 됨.

  3. 마지막으로 남은 3번 정점에서 DFS를 시작.

  4. 이를 통해 총 3개의 DFS 트리가 생겼고, 각각의 트리가 하나의 SCC가 됨.