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



##### 2) 방법

* (1) 최초, 모든 간선을 가중치에 따른 오름차순으로 정렬

* (2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가

  > `사이클이 존재한다면` 다음으로 가중치가 낮은 간선 선택

* (3) n - 1개의 간선이 선택될 때까지 (2)를 반복



##### 3) Algorithm

```
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

