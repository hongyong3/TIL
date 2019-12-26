# 20191119

## Algorithm

### MST - Kruskal's Algorithm



#### 최소신장트리(MST; Minimum Spanning Tree)

##### 1) 최소신장트리란?

* 주어진 그래프에서 최소한의 비용으로 트리를 만드는 것
* 모든 정점을 연결하는 트리를 생성하는데, 이 때 규칙은 최소한의 비용이 되는 그래프를 만드는 것

* MST는 연결된(Connected) 무방향(Undirected)의 가중치(Weight) 그래프(Graph)

* 다시 말하면 MST는 모든 정점을 연결하여 트리를 생성하는데, 

  그 규칙으로써 가중치의 합을 최소화하는 트리를 찾는 것이 목적



##### 2) 방법

* Prim's Algorithm
* Kruskal's Algorithm



---



### Kruskal's Algorithm



##### 1) Kruskal's Algorithm이란?

* 안전간선을 연결할 때, Union - Find 자료구조를 이용
* Union - Find : 찾고, 합치는 과정
* 모든 정점을 독립적인 집합으로 만든다.
* 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
* 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.



##### 2) 방법

* (1) 최초, 모든 간선을 가중치에 따른 오름차순으로 정렬

* (2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가

  > `사이클이 존재한다면` 다음으로 가중치가 낮은 간선 선택

* (3) n - 1개의 간선이 선택될 때까지 (2)를 반복



##### 3) 시간 복잡도

* *O(ElogV)*



##### 4) Algorithm

```pseudocode
MST-KRUSKAL(G, w)
	A <- 0					// 0 : 공집합
	FOR vertex v in G.V		// G.V : 그래프의 정점 집합
		Make_Set(v)			// G.E : 그래프의 간선 집합
	
	G.E에 포함된 간선들을 가중치 w에 의해 정렬
	
	FOR 가중치가 낮은 간선 (u, v) ∈ G.E 선택 (n-1개)
		IF Find_Set(u) != Find_Set(v)
			A <- A ∪ {(u, v)}
			Union(u, v);
	RETURN A
```



##### 5) Python Code

```python
parent = {}
rank = {}

# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = []

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return mst
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]
}
print(kruskal(graph))
sum = 0
for i in range(len(kruskal(graph))):
    sum += kruskal(graph)[i][0]
print(sum)
########################

# 결과
[(5, 'A', 'D'),
 (5, 'C', 'E'),
 (6, 'D', 'F'),
 (7, 'A', 'B'),
 (7, 'B', 'E'),
 (9, 'E', 'G')]
39
```