import sys
sys.stdin = open("D5_1798_input.txt", "r")

# dfs를 이용하여 완전 검색이 필요할 듯.
# 더 이상 방문할 관광포인트가 없다면, 호텔이나 공항으로 이동.
# 540분 안에 호텔로

def dfs(day, time, satis, v):
    chk = False
    for i, (m, s) in points.items():
        if visited[i]:
            continue
        if time - m - distance[v][i] >= 10:
            chk = True
            path.append(i)
            visited[i] = 1
            dfs(day, time - m - distance[v][i], satis + s, i)
            path.pop()
            visited[i] = 0
    if not chk:
        if day > 1:
            for i in hotels:
                if distance[v][i] <= time:
                    path.append(i)
                    dfs(day - 1, 540, satis, i)
                    path.pop()
        else:
            if time >= distance[v][airport] and mat[0] < satis:
                mat[0] = satis
                mat[1] = path[1:] + [airport]


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    distance = [[0] * (N + 1) for _ in range(N + 1)]
    hotels = []
    points = {} # 관광포인트는 dict로 해야할 듯.
    visited = [0] * (N + 1)
    mat = [0, []]

    for i in range(1, N):
        data = list(map(int, input().split()))
        for j, x in enumerate(data, i + 1):
            distance[i][j] = distance[j][i] = x # 이동 소요시간은 동일

    for i in range(1, N + 1):
        data = input()
        if data[0] == 'P':  # 관광포인트
            points[i] = list(map(int, data.split()[1:]))
        elif data[0] == 'H':    # 호텔
            hotels.append(i)
        else:   # 공항
            airport = i

    path = [airport]
    dfs(M, 540, 0, airport)
    print('#{} {}'.format(test_case + 1, mat[0]), *mat[1])