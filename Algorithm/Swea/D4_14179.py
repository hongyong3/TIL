import sys
sys.stdin = open("D4_14179_input.txt", "r")

# mod = 1000000007
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr2 = arr * 2
#     inversion1, inversion2 = [0] * N, [0] * N
#     ans = 0
#
#     for i in range(N):
#         for j in range(i + 1, N):
#             if arr[i] > arr[j]:
#                 inversion1[i] += 1
#
#     for i in range(N):
#         for j in range(i + 1, i + N):
#             if arr2[i] > arr2[j]:
#                 inversion2[i] += 1
#
#     for i in range(N):
#         ans += (inversion1[i] * K + inversion2[i] * (K * (K - 1) // 2)) % mod
#         ans %= mod
#
#     print("#{} {}".format(test_case + 1, ans % mod))

mod = 1000000007
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = arr * 2
    inversion1, inversion2 = [0] * N, [0] * N
    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                inversion1[i] += 1

        for j in range(i + 1, i + N):
            if arr2[i] > arr2[j]:
                inversion2[i] += 1

    for i in range(N):
        ans += (inversion1[i] * K + inversion2[i] * (K * (K - 1) // 2)) % mod
        ans %= mod

    print("#{} {}".format(test_case + 1, ans % mod))