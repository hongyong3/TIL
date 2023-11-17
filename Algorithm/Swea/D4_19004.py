import sys
sys.stdin = open("D4_19004_input.txt", "r")

T = int(input())
for test_case in range(1):
    N, K = map(int, input().split())
    num = set()
    graph = []
    coordinate = [[] for _ in range(K + 1)]

    for x in range(N):
        data = list(map(int, input().split()))
        graph.append(data)
        for y in range(N):
            num.add(data[y])
            coordinate[data[y]].append([x, y])

    if K != len(num):
        ans = - 1
    else:
        ans = float('inf')
        # 탐색 해보자..
        # for i in range()