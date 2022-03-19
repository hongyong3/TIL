import sys
sys.stdin = open("D4_5608_input.txt", "r")


# def solve(n, idx):
#     global count, num
#     if idx < 0:
#         return
#
#     if n >= arr[idx]:
#         n -= arr[idx]
#         a[arr[idx]] += 1
#         count += 1
#         num += arr[idx]
#         solve(n, idx)
#
#     else:
#         solve(n, idx - 1)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#
#     arr, a, count, num = [], {}, 0, 0
#
#     for i in range(2, N):
#         if pow(i, 3) < N:
#             arr.append(pow(i, 3))
#             a[pow(i, 3)] = 0
#         else:
#             break
#
#     if arr:
#         solve(N, len(arr) - 1)
#         print(count + N - num + 1, num - 1)
#     else:
#         print(N, N)

# def solve(n):
#     memo = [0] * (n + 1)
#     memo[1] = 1
#     idx = 1
#     for i in range(2, n + 1):
#         if i in arr:
#             idx += 1
#         memo[i] = memo[i - arr[idx - 1]] + 1
#     return max(memo), len(memo) - 1 - memo[::-1].index(max(memo))
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = []
#     for i in range(3, N):
#         if pow(i, 3) < N:
#             arr.append(pow(i, 3))
#         else:
#             break
#     print(arr)
#     print("#{}".format(test_case + 1), *solve(N))


# memo = [0, 1]
#
# def cubeRoot(n):
#     arr.clear()
#     for i in range(1, n):
#         if pow(i, 3) <= n:
#             arr.append(pow(i, 3))
#         else:
#             break
#     return arr
#
#
# def solve(n):
#     idx = 1
#     for i in range(2, n + 1):
#         if i in arr:
#             idx += 1
#         else:
#             memo.append(memo[i - arr[idx - 1]] + 1)
#     return max(memo[:n]), len(memo[:n]) - 1 - memo[:n][::-1].index(max(memo[:n]))
#
# T = int(input())
# for test_case in range(1):
#     N = int(input())
#     arr = []
#     cubeRoot(N)
#     print("#{}".format(test_case + 1), *solve(N))
#     print(memo)


# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     num, ans = 0, 0
#
#     numList = []
#     for i in range(1, N):
#         if pow(i, 3) < N:
#             numList = [pow(i, 3)] + numList
#
#         else:
#             break
#     print(numList)
#
#     x = 0
#     while N:
#         mok = N // numList[x]
#         nam = N % numList[x]
#         N = nam
#         x += 1
#         print(mok, nam)

# T = int(input())
# for test_case in range(1):
#     N = int(input())
#
#     idx = 0
#     arr1 = [0]
#     arr2 = [0] * (N + 1)
#     maxCount, maxNum = 0, 0
#
#     for i in range(1, N):
#         if pow(i, 3) < N:
#             arr1.append(pow(i, 3))
#             arr2[pow(i, 3)] = 1
#         else:
#             break
#     arr1.append(0)
#
#     for i in range(N + 1):
#         if i == arr1[idx]:
#             idx += 1
#         else:
#             arr2[i] = arr2[i - arr1[idx - 1]] + 1
#
#     maxCount = max(arr2)
#     maxNum = len(arr2) - 1 - arr2[::-1].index(maxCount)
#     print("#{} {} {}".format(test_case + 1, maxCount, maxNum))

'''
# boj 1699
# 제곱수의 합
import sys
input = sys.stdin.readline
n = int(input())
dp = list(range(n + 1))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        else:
            break
print(dp[n])
'''

# T = int(input())
# dp = list(range(45))
# for i in range(1, 45):
#     for j in range(1, i + 1):
#         if j ** 3 <= i:
#             dp[i] = min(dp[i], dp[i - j * j * j] + 1)
#         else:
#             break
# print(dp)
# for test_case in range(T):
#     M = int(input())