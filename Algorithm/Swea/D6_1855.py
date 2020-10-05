import sys
sys.stdin = open("D6_1855_input.txt", "r")

'''
LCA Algorithm(Lowest Common Ancestor)
- 최소 공통 조상을 찾는 알고리즘
- 두 정점 u, v에서 가장 가까운 공통 조상을 찾는 과정
- 세그먼트 트리를 이용하지 않고 DP를 이용하여 해결
- 시간 복잡도
    * LCA 알고리즘 시간 복잡도 O(logN)
    * 쿼리가 함께 존재할 경우 시간 복잡도 O(MlogN)
- 알고리즘 동작 과정
    * 첫 번째로 입력받은 정점과 간선을 이용하여 양방향 그래프를 생성
    * depth와 조상을 가지는 트리를 생성

'''

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(N + 3)]
    chk = [0] * N
    d = [0] * N
    p = [[0] * 23 for _ in range(N + 3)]

    j = 1
    for i in data:
        graph[i - 1].append(j)
        j += 1

    chk[0] = 1
    q = [(0, 0)]

    while q:
        node, depth = q.pop(0)
        d[node] = depth

        for i in graph[node]:
            nnode = i
            if not chk[nnode]:
                chk[nnode] = 1
                p[nnode][0] = node
                q.append((nnode, depth + 1))