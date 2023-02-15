import sys
sys.stdin = open("D4_15942_input.txt", "r")

# 9 / 29 Runtime Error
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     arr = sorted(list(map(int, input().split())))
#     ans = 0
#     total = sum(arr)
#
#     '''
#     - 처음 보유한 함선이 0인 경우
#     - 처음 보유한 함선이 arr[0]보다 작은 경우
#     - (처음 보유한 함선) + (모든 행성의 인구 - A_n) < A_n
#     '''
#
#     if K == 0 or K < arr[0] or K + total < arr[- 1] * 2:
#         ans = - 1
#     else:
#         idx = 0
#         while idx < len(arr):
#             if K < arr[idx]:
#                 ans += 1
#                 K += arr[idx - 1]
#                 total -= arr[idx - 1]
#                 arr.pop(idx - 1)
#                 idx -= 1
#             else:
#                 idx += 1
#
#         if K < sum(arr):
#             ans += 1
#             K += arr[- 1]
#             total -= arr[- 1]
#     print("#{} {}".format(test_case + 1, ans))
#
#
# 27 / 29 Fail
# 새로 짜야 할듯..
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     arr = sorted(list(map(int, input().split())))
#     total = sum(arr)
#     ans = 0
#
#     if K == 0 or K < arr[0] or K + total < arr[- 1] * 2:
#         ans = - 1
#     else:
#         idx = 1
#         while idx < len(arr):
#             if K < arr[idx]:
#                 ans += 1
#                 K += arr[idx - 1]
#                 total -= arr[idx - 1]
#                 arr.pop(idx - 1)
#                 N -= 1
#             else:
#                 idx += 1
#
#         # 여기만 고치면 끝
#         jdx = - 2
#         while K < arr[- 1]:
#             if K >= arr[jdx]:
#                 K += arr[jdx]
#                 total -= arr[jdx]
#                 ans += 1
#                 arr.pop(jdx)
#                 break
#             else:
#                 jdx += 1
#
#         while K < total:
#             ans += 1
#             K += arr[- 1]
#             total -= arr[- 1]
#             arr.pop(- 1)
#             N -= 1
#
#     print("#{} {}".format(test_case + 1, ans))

# 22 / 29 Fail
# def upperBound(k, e):
#     global N, K, s, total, visited
#     while s < e:
#         m = (s + e) // 2
#         if k < arr[m]:
#             e = m
#         else:
#             s = m + 1
#     if not visited[s - 1]:
#         K += arr[s - 1]
#         total -= arr[s - 1]
#         visited[s - 1] = 1
#     else:
#         idx = 1
#         while True:
#             if not visited[s - 1 - idx]:
#                 K += arr[s - 1 - idx]
#                 total -= arr[s - 1 - idx]
#                 visited[s- 1 - idx] = 1
#                 break
#             else:
#                 idx += 1
#     return s
#
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     arr = sorted(list(map(int, input().split())))
#     total = sum(arr)
#     if K < arr[0] or K + total < arr[- 1] * 2:
#         ans = - 1
#     else:
#         ans = 0
#         visited = [0] * N
#         s = 0
#         while K < total:
#             arr[upperBound(K, N - 1)]
#             ans += 1
#
#     print("#{} {}".format(test_case + 1, ans))


def upperBound(k):
    s, e = 0, N - 1
    while s < e:
        m = (s + e) // 2
        if arr[m] <= k:
            s = m + 1
        else:
            e = m
    return e


def find(v):
    if point[v] == v:
        return v
    else:
        point[v] = find(point[v])

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    total = sum(arr)
    visited = [0] * N
    point = [i for i in range(N + 1)]
    ans = 0
    while K < total:
        idx = upperBound(K)
        if idx:
            val = find(idx) - 1
            if visited[val]:
                ans = - 1
                break

            K += arr[val]
            total -= arr[val]
            ans += 1
            visited[val] = 1
            if val:
                point[val] = find(val)
        else:
            ans = - 1
            break
    print("#{} {}".format(test_case + 1, ans))