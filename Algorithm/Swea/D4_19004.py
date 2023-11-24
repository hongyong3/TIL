import sys
sys.stdin = open("D4_19004_input.txt", "r")

# def solve(k, dis):
#     global ans
#     if k == K:
#         if dis < ans:
#             ans = dis
#         else:
#             return
#
#     while


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    num = set()
    arr = []
    coordinate = [[] for _ in range(K + 1)]

    for x in range(N):
        data = list(map(int, input().split()))
        arr.append(data)
        for y in range(N):
            num.add(data[y])
            coordinate[data[y]].append([x, y])

    if K != len(num):
        ans = - 1
    else:
        ans = float('inf')
        # 탐색 해보자..  가지치기 필수
        # solve(1, 0)   # K, distance
        # for i in range(1, len(coordinate)):
        #     for j in range(len(coordinate[i])):
        #         x, y = coordinate[i][j][0], coordinate[i][j][1]
    print(ans)