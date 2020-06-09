import sys
sys.stdin = open("D5_1798_input.txt", "r")

# dfs를 이용하여 완전 검색이 필요할 듯.
# 더 이상 방문할 관광포인트가 없다면,
# 호텔이나 공항으로 이동.
# 540분 안에 호텔로

def dfs():
    pass

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    time = [[0] * (N + 1) for _ in range(N + 1)]
    hotels = []
    # points = []
    points = {} # 관광포인트는 dict로 해야할 듯.

    visited = [0] * (N + 1)

    for i in range(1, N):
        data = list(map(int, input().split()))
        for j, x in enumerate(data, i + 1):
            time[i][j] = time[j][i] = x # 이동 소요시간은 동일

    for i in range(1, N + 1):
        data = input()
        if data[0] == 'P':  # 관광포인트
            points[i] = list(map(int, data.split()[1:]))
        elif data[0] == 'H':    # 호텔
            hotels.append(i)
        else:   # 공항
            airport = i