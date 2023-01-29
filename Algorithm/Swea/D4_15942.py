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


# 27 / 29 Fail
# 새로 짜야 할듯..
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    total = sum(arr)
    ans = 0

    if K == 0 or K < arr[0] or K + total < arr[- 1] * 2:
        ans = - 1
    else:
        idx = 1
        while idx < len(arr):
            if K < arr[idx]:
                ans += 1
                K += arr[idx - 1]
                total -= arr[idx - 1]
                arr.pop(idx - 1)
                N -= 1
            else:
                idx += 1

        # 여기만 고치면 끝
        jdx = - 2
        while K < arr[- 1]:
            if K >= arr[jdx]:
                K += arr[jdx]
                total -= arr[jdx]
                ans += 1
                arr.pop(jdx)
                break
            else:
                jdx += 1

        while K < total:
            ans += 1
            K += arr[- 1]
            total -= arr[- 1]
            arr.pop(- 1)
            N -= 1

    print("#{} {}".format(test_case + 1, ans))