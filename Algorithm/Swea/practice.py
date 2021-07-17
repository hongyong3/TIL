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

# a, b, c, d = input().split()
# s1 = a + b
# s2 = c + d
# print(int(s1) + int(s2))

# boj 1965
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# boj 13300

# N, K = map(int, input().split())
# for _ in range(N):
#     S, Y = map(int, input().split())

# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     ans = A * B
#     if A > 9 or B > 9:
#         ans = - 1
#     print("#{} {}".format(test_case + 1, ans))

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# sumList = [0]
# num = 0
# for i in arr:
#     num += i
#     sumList.append(num)
# for _ in range(m):
#     i, j = map(int, input().split())
#     print(sumList[j] - sumList[i - 1])

# import sys
# input = sys.stdin.readline
# t = int(input())
# arr = list(map(int, input().split()))
#
# for i in arr:
#     ans = 0
#     x = i // 3
#     y = i // 7
#     z = i // 21
#     ans += 3 * x * (x + 1) // 2
#     ans += 7 * y * (y + 1) // 2
#     ans -= 21 * z * (z + 1) // 2
#     print(ans)

import sys
input = sys.stdin.readline
n = int(input())
if n < 100:
    print(n // 10 + n % 10)
elif n % 10:
    print(n % 100 + 10)
else:
    print(n // 100 + 10)