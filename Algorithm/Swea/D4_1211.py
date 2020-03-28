import sys
sys.stdin = open("D4_1211_input.txt", "r")

# def check(x, y):
#     if not (x <= x < 100 and 0 <= y < 100) or data[x][y] != 1:
#         return False
#     return True
#
# def dfs(x, y):
#     global ans, temp
#     while True:
#         if x == 99:
#             if ans > temp:
#                 ans = temp
#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if check(nx, ny):
#                 data[x][y] = 9
#                 x, y = nx, ny
#                 temp += 1
#
#
# dx = [0, 0, 1]    # 좌 우 하
# dy = [- 1, 1, 0]
# for test_case in range(10):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(100)]
#     ans = float('inf')
#     for i in range(100):
#         if data[0][i] == 1:
#             temp = 0
#             print("#{} {}".format(test_case + 1, dfs(0, i)))

for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    pillar = []  # 기둥 x 좌표
    dist = []  # 기둥 사이 간격
    temp = -1
    for c in range(100):
        if data[99][c]:
            pillar.append(c)
            if temp >= 0:
                dist.append(c - temp)
            temp = c

    # 계산
    cnt = [0] * len(pillar)
    for r in range(98, 0, -1):  # 98~1
        for i in range(len(dist)):
            if data[r][pillar[i] + 1]:
                cnt[i], cnt[i + 1] = cnt[i + 1] + dist[i], cnt[i] + dist[i]

    # 결과
    temp = float('inf')
    for i in range(len(cnt)):
        if cnt[i] <= temp:
            temp = cnt[i]
            result = pillar[i]

    print('#{} {}'.format(test_case + 1, result))