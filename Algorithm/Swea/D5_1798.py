import sys
sys.stdin = open("D5_1798_input.txt", "r")

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    distance = [[0] * (N + 1) for _ in range(N + 1)]
    hotels, points = [], {}

    for i in range(1, N):
        data = list(map(int, input().split()))
        for j, x in enumerate(data, i + 1):
            distance[i][j] = distance[j][i] = x

    for i in range(1, N + 1):
        data = input()
        if data[0] == 'P':
            points[i] = list(map(int, data.split()[1:]))
        elif data[0] == 'H':
            hotels.append(i)
        else:
            airport = i