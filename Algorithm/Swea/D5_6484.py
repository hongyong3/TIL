import sys
sys.stdin = open("D5_6484_input.txt", "r")

# arr = [0] * 100001
# arr[0] = 1
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     for i in range(1, N + 1):
#         arr[i] = (arr[i - 1] * i) % 1000000007

# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     num, arr, ans, idx = 1, {}, 1, 2
#     for i in range(N - K + 1, N + 1):
#         num = (num * i) % 100000007
#     for i in range(1, K + 1):
#         num = (num // i) % 100000007
#     num %= 100000007
#
#     while num != 1:
#         if num % idx == 0:
#             num //= idx
#             if idx not in arr:
#                 arr[idx] = 1
#             else:
#                 arr[idx] += 1
#         else:
#             idx +=1
#
#     for i in arr.values():
#         ans *= (i + 1)
#
#     print("#{} {}".format(test_case + 1, ans % 1000000007))

# def findPrimeFactors(n, k):
#     tPrimeFactorsMap = {}
#     tCompositeChecker = [True] * 2 + [False] * n
#     for p in range(n + 1):
#         if tCompositeChecker[p]:
#             continue
#         q, m = p, 1
#         tPrimeCnt = 0
#         tPrimePowers = [0] * (n + 1)
#
#         while True:
#             tPrimePowers[q] = tPrimePowers[m] + 1
#             if q <= k:
#                 tPrimeCnt -= tPrimePowers[q]
#             if q > n - k:
#                 tPrimeCnt += tPrimePowers[q]
#
#             q += p
#             m += 1
#             if q > n:
#                 break
#             tCompositeChecker[q] = True
#         tPrimeFactorsMap[p] = tPrimeCnt
#     return tPrimeFactorsMap
#
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     ans = 1
#     a = findPrimeFactors(N, K)
#     for val in a.values():
#         if val:
#             ans *= (val + 1)
#             ans %= 1000000007
#     print("#{} {}".format(test_case + 1, ans))


maxN = 100001
arr = [0] * maxN
prime = []
for i in range(2, maxN):
    if arr[i]:
        continue
    prime.append(i)
    for j in range(i, maxN, i):
        arr[j] = 1


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    ans = 1

    for i in prime:
        if i > N:
            break

        cnt = 1
        num = N // i
        while num:
            cnt += num
            num //= i

        num = K // i
        while num:
            cnt -= num
            num //= i

        num = (N - K) // i
        while num:
            cnt -= num
            num //= i

        ans *= cnt
        ans %= 1000000007

    print("#{} {}".format(test_case + 1, ans))