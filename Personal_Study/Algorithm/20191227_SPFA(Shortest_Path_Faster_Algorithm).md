# 20191227

## Algorithm

### SPFA(Shortest Path Faster Algorithm)



#### 1) SPFA란?

* `벨만포드 알고리즘(Bellman-Ford Algorithm)`의 성능을 향상시킨 알고리즘.
* 음수 간선에도 문제없이 돌아가기 때문에 `MCMF`에서 자주 사용.



#### 2) 벨만포드 알고리즘 VS SPFA

##### 벨만포드 알고리즘

* 그래프 상에 존재하는 **두 노드간의 최단거리를 구할 때** 사용하는 알고리즘.

* Dijkstra 알고리즘과의 차이점은 **음의 가중치**를 포함할 때 사용 가능.

* 간선(Edge)의 개수와 노드(Vertex)의 개수에 따라 **유동적**으로 알고리즘을 사용.

* 매 라운드마다 모든 Edge를 검사하고, |V| - 1의 라운드 동안 전체 Edge |E|개를 검사하므로

  **시간복잡도**는 **O(|V||E|)**, |E|는 최대 V^2^

  **공간복잡도**는 각 노드 마다 최단 거리를 저장하므로 **O(V)**

* 전제조건

  > 최단 경로는 사이클을 포함하지 않음.
  >
  > ​	따라서 **|V| - 1 개**의 간선만 사용할 수 있음.
  >
  > 최단 경로가 업데이트 되는 노드가 없어질 때까지 반복.
  >
  > 만약, **무한히 업데이트 한다면** 이는 조건에 맞지 않으므로 **불가능**.



##### SPFA

* 벨만포드 알고리즘은 *모든 간선에 대해 업데이트*를 진행하지만,

  SPFA는 **바뀐 정점과 연결된 간선에 대해서만 업데이트**를 진행.

* 따라서,  다른 최단경로 알고리즘보다 구현이 간단하면서, 매우 빠른 수행시간을 보여줌.



#### 3) 시간 복잡도

* **O(V * E)**이지만, `실제로는 훨씬 빨리 돌아가는 알고리즘`으로 **O(V + E)** 또는 **O(E)**라고 해도 무방.



#### 4) 방법

##### Pseudo Code

```pseudocode
procedure Shortest-Path-Faster-Algorithm(G, s)
	for each vertex v ≠ s in V(G)
		d(v) := ∞
	d(s) := 0
	offer s into Q
	while Q is not empty
		u := poll Q
		for each edge (u, v) in E(G)
			if d(u) + w(u, v) < d(v) then
				d(v) := d(u) + w(u, v)
				if v is not in Q then
					offer v into Q
```



- 시작 Node(s)에 대하여 큐에 삽입.

- **Queue**에 있는지 없는지는 따로 배열을 만들어서 관리.

  => **O(1)**

- **Queue**의 맨 앞 Node를 가져와서, 모든 Edge를 검사.

  => 만약, **최단거리**를 갱신할 수 있으면 갱신.

- **Queue**에 없는 Node라면, Queue에 삽입.

- *음수 사이클을 확인하려면?*

  > cycle을 확인하는 배열을 만들어서 **Queue**에 Node를 삽입할 때 **+ 1 씩 카운트**.
  >
  > 만약, 똑같은 **Node**에 대해 |V|(정점 개수) 만큼 방문한다면, **음수사이클**.



##### Python code

```python
from collections import deque

T = int(input())
for test_case in range(T):
    N, M, s, e = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    print(graph)

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False for _ in range(N + 1)]
    d = [float('inf') for _ in range(N + 1)]
    d[s] =  0

    q = deque()
    q.append(s)
    visited[s] = True

    while len(q) > 0:
        u = q.popleft()
        visited[u] = False
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                if not visited[v]:
                    q.append(v)
    print("#{} {}".format(test_case + 1, d[e]))
```

