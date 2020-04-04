# 20200404

## Algorithm

### 플로이드 와샬(Floyd Warshall)



#### 플로이드 와샬(Floyd Warshall)

##### 1) 플로이드 와샬이란?

- **모든 최단 경로를 구하는 방법**(All pairs shortest path problem).
- 음의 가중치를 간선에서도 사용 가능.
- 모든 정점에 대한 경롤르 계산하므로 거리를 저장할 자료구조는 2차원 배열이 됨.



##### 2) 방법

- 정보를 저장할 인접행렬 **graph**를 생성.

  graph의 크기는 노드의 개수 `V`에 대해서 V * V의 크기를 가지며,

  `graph[i][j]`는 i 번째 노드부터 j번째 노드까지의 가중치.

- 예를 들어 아래와 같은 그래프가 있으면

![img](https://t1.daumcdn.net/cfile/tistory/2119574E5719C5E824)

* graph는

  ```python
  0		3		8		inf		-4
  inf		0		inf		1		7
  inf		4		0		inf		inf
  2		inf		-5		0		inf
  inf		inf		inf		6		0
  ```

  inf는 이동가능한 경로가 없다는 의미.