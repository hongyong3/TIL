import sys
sys.stdin = open("D2_4881_input.txt", "r")

# 이전 풀이
# def MinSum(k):
#     global min, sum, N
#     if k == N:
#         if min > sum:
#             min = sum
#     for i in range(N):
#         if visit[i] == 0:
#             if sum > min:
#                 continue
#             else:
#                 visit[i] = 1
#                 sum += data[i][k]
#                 MinSum(k+1)
#                 visit[i] = 0
#                 sum -= data[i][k]
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     visit = [0]*N
#     min = 10**10
#     sum = 0
#     MinSum(0)
#
#     print('#{} {}'.format(test_case+1, min))

def solve(n):
    global ans, subAns, visited
    if n == N:
        if ans > subAns:
            ans = subAns

    for i in range(N):
        if not visited[i]:
            if subAns < ans:
                visited[i] = 1
                subAns += data[i][n]
                solve(n + 1)
                visited[i] = 0
                subAns -= data[i][n]

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, subAns = float('inf'), 0
    visited = [0] * N
    solve(0)
    print("#{} {}".format(test_case + 1, ans))