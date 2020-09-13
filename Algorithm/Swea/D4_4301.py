import sys, time
start = time.time()
sys.stdin = open("D4_4301_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     ans = N * M
#     visited = [[0] * (N + 2) for _ in range(M + 2)]
#
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j]:
#                 visited[i][j] = 1
#                 if (i + 2) < N and not visited[i + 2][j]:
#                     visited[i + 2][j] = 1
#                     ans -= 1
#                 if (j + 2) < M and not visited[i][j + 2]:
#                     visited[i][j + 2] = 1
#                     ans -= 1
#     print("#{} {}".format(test_case + 1, ans))


# 유클리디안 거리(Euclidean Distance)
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    mat = 0
    a = N // 4 * 2 + min(N % 4, 2)
    b = N // 4 * 2 + max(N - (N // 4) * 4 - 2, 0)
    mat += (M // 4) * 2 * (a + b)
    M = M - (M // 4) * 4
    if M: mat += a
    if M > 1: mat += a
    if M > 2: mat += b
    if M > 3: mat += b
    print("#{} {}".format(test_case + 1, mat))
print("time :", time.time() - start)