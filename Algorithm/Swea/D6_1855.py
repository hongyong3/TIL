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
    # graph = [[0] * (N + 1) for _ in range(N + 1)]
    graph = [[] for _ in range(N + 3)]
    n = 0
    for i in range(1, N):
        graph[data[n] - 1].append(i)
        n += 1
    print(graph)
    # 수정...
    for i in range(N):
        sorted(graph[i][0], graph[i][1])
    print(graph)