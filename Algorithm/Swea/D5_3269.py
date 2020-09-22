import sys
sys.stdin = open("D5_3269_input.txt", "r")

'''
강결합 컴포넌트(SCC; Strongly Connected Component)
1. SSC 내의 임의의 두 정점 u, v 사이의 u -> v 경로와 v -> u 경로가 항상 존재.
2. SSC 내의 임의의 정점 u와 외부의 임의의 정점 v 사이에 u -> v 경로와, v -> u 경로가 동시에 존재하는 경우는 X
    즉, SSC는 내부의 모든 정점에서 내부의 다른 모든 정점으로 갈 수 있는 최대 그룹이라고 할 수 있음.
    또한, 모든 방향성 그래프는 한개 이상의 SSC들로 분리될 수 있음.
3. DFS 트리의 개념을 알아야 함.
    DFS를 사용해서 강결합 컴포넌트를 분리하는 알고리즘
        - Kosaraju's Algorithm
        - Tarjan's Algorithm



DFS 트리란?
- 어떤한 그래프에서 DFS를 하는 과정을 트리로 나타낸 것.
- discovery time : 그 정점을 방문한 시간.
  finish time : 그 정점의 모든 자식들을 방문하고 그 정점을 빠져나가는 시간.
    정점 u의 discovery time을 dt[u]
    finish time을 ft[u]
    
- DFS를 통해 그래프의 간선들을 다음과 같이 분류할 수 있음.
    
    1. Tree edge
        - 그래프의 간선들 중 DFS 트리에 속하는 간선ㄷ르.
        - 이 경우 dt[u] < dt[v], ft[u] > ft[v] 
    
    2. back edge
        - 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 v가 u의 조상인 간선들.
        - 즉 DFS 트리에서 거꾸로 조상한테 올라가는 간선.
        - 이 경우 dt[u] > dt[v], ft[u] < ft[v]
    
    3. forward edge
        - 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 u가 v의 조상인데 tree edge에 속하지 않는 간선들.
        - 이 경우 dt[u] < dt[v], ft[u] > ft[v]
    
    4. cross edge
        - 위의 3가지 간선에 해당하지 않는 간선들.
        - 그래프의 간선 (u -> v)들 중에서, DFS 트리에서 u가 v의 조상도 아니고, v가 u의 조상도 아닌 경우.
        - 이 경우 dt[u] > ft[v]

- 모든 방향성 그래프의 간선들은 이 4가지 중 하나에 속하게 됨. 
'''

def GDfs(n):
    global ft
    visited[n] = 1
    for nv in G[n]:
        if not visited[nv]:
            GDfs(nv)
    ft += 1
    ft2vtx[ft] = n

def TDfs(n, scc):
    scc.append(n)
    visited[n] = 1
    for nv in T[n]:
        if not visited[nv]:
            TDfs(nv, scc)

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    ft2vtx = [0] * (V + 1)
    G = [[] for _ in range(V + 1)]  # 정방향 그래프
    T = [[] for _ in range(V + 1)]  # 역방향 그래프
    ft = 0
    visited = [0] * (V + 1)
    scc = []

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        T[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            GDfs(i)
    visited = [0] * (V + 1)
    for i in range(V, 0, - 1):
        if not visited[ft2vtx[i]]:
            TDfs(ft2vtx[i], scc)
            scc = sorted(scc)