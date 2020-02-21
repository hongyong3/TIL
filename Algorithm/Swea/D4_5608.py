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


T = int(input())
for test_case in range(T):
    N = int(input())

    idx = 0
    arr1 = [0]
    arr2 = [0] * (N + 1)
    maxCount, maxNum = 0, 0

    for i in range(1, N):
        if pow(i, 3) < N:
            arr1.append(pow(i, 3))
            arr2[pow(i, 3)] = 1
        else:
            break
    arr1.append(0)

    for i in range(N + 1):
        if i == arr1[idx]:
            idx += 1
        else:
            arr2[i] = arr2[i - arr1[idx - 1]] + 1

    maxCount = max(arr2)
    maxNum = len(arr2) - 1 - arr2[::-1].index(maxCount)
    print("#{} {} {}".format(test_case + 1, maxCount, maxNum))