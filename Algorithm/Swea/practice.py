import sys
sys.stdin = open("practice_input.txt", "r")


# '''
# 1은 익은 토마토
# 0은 안익은 토마토
# - 1은 토마토 X
# '''
# import sys
# from collections import deque
# input = sys.stdin.readline
# def chk(day):
#     for z in range(h):
#         for x in range(n):
#             for y in range(m):
#                 if not arr[z][x][y]:
#                     return - 1
#     return day
#
#
# dx = [0, 0, 0, 0, - 1, 1]   # 위 아래 왼쪽 오른쪽 앞 뒤
# dy = [0, 0, - 1, 1, 0, 0]
# dz = [- 1, 1, 0, 0, 0, 0]
#
# m, n, h = map(int, input().split())
# arr = [[[0] * m for _ in range(n)] for _ in range(h)]
# q = deque() # 익은 토마토
# ans = 0
# for z in range(h):
#     for x in range(n):
#         data = list(map(int, input().split()))
#         for y, i in enumerate(data):
#             arr[z][x][y] = i
#             if i == 1:
#                 q.append((z, x, y, 0))
#
# while q:
#     z, x, y, cnt = q.popleft()
#     for k in range(6):
#         nz = z + dz[k]
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
#             if not arr[nz][nx][ny]:
#                 arr[nz][nx][ny] = 1
#                 q.append((nz, nx, ny, cnt + 1))
#                 ans = cnt + 1
# print(chk(ans))

# print(input() + "??!")

# score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
# arr = list(map(int, input().split()))
# if sum(arr) < 100:
#     print("none")
# else:
#     for i in range(9):
#         if arr[i] > score[i]:
#             print("hacker")
#             break
#     else:
#         print("draw")

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(sum(list(map(int, input().split()))))

# import sys
# input = sys.stdin.readline
# N, K, L = map(int, input().split())
# ans, arr = 0, []
# for _ in range(N):
#     x1, x2, x3 = map(int, input().split())
#     if x1 + x2 + x3 >= K and min(x1, x2, x3) >= L:
#         ans += 1
#         arr.append(x1)
#         arr.append(x2)
#         arr.append(x3)
# print(ans)
# print(*arr)

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     ans = 0
#     for a in range(i - 1, x):
#         for b in range(j - 1, y):
#             ans += arr[a][b]
#     print(ans)

# n, k = map(int, input().split())
# ans = 0
# for i in list(map(int, input().split())):
#     ans += i // 2 + i % 2
# print("YES") if ans >= n else print("NO")

a, b, c, d = input().split()
s1 = a + b
s2 = c + d
print(int(s1) + int(s2))

# boj 1965
# n = int(input())
# ans = 0
# idx = n - 1
# # for i in range(n):