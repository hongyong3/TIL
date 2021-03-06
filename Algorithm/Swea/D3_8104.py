import sys
sys.stdin = open("D3_8104_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     temp = [[0] * K for _ in range(N)]
#     mat = [0] * K
#     k = 0
#
#     while k <= N * K - 1:
#         for i in range(N):
#             for j in range(K):
#                 k += 1
#                 if i % 2 == 0:
#                     temp[i][j] = k
#                 else:
#                     temp[i][K - 1 - j] = k
#
#     for i in range(K):
#         for j in range(N):
#             mat[i] += temp[j][i]
#
#     print("#{}".format(test_case + 1), *mat)


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())

    n = (N // 2) + (N % 2)
    ans = (2 * K * n + 1) * n
    if not N % 2:
        print("#{}".format(test_case + 1), *[ans] * 6)
    else:
        print("#{}".format(test_case + 1), end = "")
        for i in range(1, K + 1):
            print("", ans - ((N + 1) * K - i + 1), end="")
        else:
            print()