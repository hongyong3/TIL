import sys
sys.stdin = open("D3_5208_input.txt", "r")

# 이전 풀이
# def dfs(n):
#     global ans, count
#     if n >= N:
#         if ans > count:
#             ans = count
#         return
#
#     if ans < count:
#         return
#
#     start = n
#     fuel = data[start]
#
#     for i in range(start + fuel, start, - 1):
#         count += 1
#         dfs(i)
#         count -= 1
#
#
#
# T = int(input())
# for test_case in range(T):
#     data = list(map(int, input().split()))
#     ans = float('inf')
#     N = data[0]
#     count = 0
#     dfs(1)
#     print("#{} {}".format(test_case + 1, ans - 1))

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    N = data.pop(0)