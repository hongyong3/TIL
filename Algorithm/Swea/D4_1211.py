import sys
sys.stdin = open("D4_1211_input.txt", "r")

# 이전 풀이
# def check(x, y, visited):
#     if x < 0 or x >= M: return False
#     if y < 0 or y >= M: return False
#     if data[x][y] == 0: return False
#     if visited[x][y] == 1: return False
#     return True
#
# def getCount(x, y):
#     dx = [0, 0, 1]
#     dy = [-1, 1, 0] # 왼쪽, 오른쪽, 아래
#     visited = [[0 for _ in range(M)] for _ in range(M)]
#     count = 0
#     visited[x][y] = 1
#
#     while(True):
#         if x == M - 1: break
#         for j in range(3):
#             new_x = x + dx[j]
#             new_y = y + dy[j]
#             if check(new_x, new_y, visited):
#                 x = new_x
#                 y = new_y
#                 visited[x][y] = 1
#                 count += 1
#                 break
#     return count
#
# def solve():
#     min = 0x7fffffff
#     ret = 0
#     count = 0
#     for i in range(M):
#         if data[0][i]:
#             count = getCount(0, i)
#         if count < min:
#             min = count
#             ret = i
#     return ret
#
# for test_case in range(10):
#     N = int(input())
#     M = 100
#     count = 0
#     data = [list(map(int, input().split())) for _ in range(M)]
#     print("#{} {}".format(test_case+1, solve()))

for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    pillar = [i for i in range(100) if data[99][i]]
    distance = [pillar[i + 1] - pillar[i] for i in range(len(pillar) - 1)]
    count = [0] * len(pillar)

    for i in range(98, 0, - 1):
        for j in range(len(distance)):
            if data[i][pillar[j] + 1]:
                count[j], count[j + 1] = count[j + 1] + distance[j], count[j] + distance[j]

    print("#{} {}".format(test_case + 1, pillar[count.index(min(count))]))