import sys
sys.stdin = open("D2_14510_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = sorted(list(map(int, input().split())))
#     high = arr[- 1]
#     ans, idx = 0, 0
#     while idx < len(arr):
#         k = high - arr[idx]
#         if k % 3 == 0:
#             ans += (k // 3) * 2
#             arr.pop(idx)
#         else:
#             arr[idx] = high - arr[idx]
#             if arr[idx] > 6:
#                 ans += (arr[idx] // 3) * 2
#                 arr[idx] %= 3
#             idx += 1
#     arr = sorted(arr)
#     if len(arr) == 1:
#         ans += (arr[0] // 3) + arr[0] % 3
#         arr.pop()
#     nam1, idx = 0, 0
#     idx = 0
#     while len(arr) > 1 or idx < len(arr):
#         if arr[idx] == 1:
#             nam1 += 1
#             idx += 1
#         elif arr[idx] % 3 == 2:
#             if nam1:
#                 arr[idx - 1] -= 1
#                 if arr[idx - 1] == 0:
#                     arr.pop(idx - 1)
#                 arr[idx - 1] -= 2
#                 if arr[idx - 1] == 0:
#                     arr.pop(idx - 1)
#                 nam1 -= 1
#                 ans += 2
#                 idx -= 1
#             else:
#                 break
#                 idx += 1
#         elif arr[idx] % 3 == 0:
#             ans += (arr[idx] // 3) * 2
#             arr.pop(idx)
#             idx -= 1
#         else:
#             if nam1:
#                 arr[idx - 1] -= 1
#                 if arr[idx - 1] == 0:
#                     arr.pop(idx - 1)
#                 arr[idx - 1] -= 2
#                 if arr[idx - 1] == 0:
#                     arr.pop(idx - 1)
#                 ans += 2
#                 idx -= 1
#     ans += (sum(arr) // 3) * 2 + sum(arr) % 3
#     # if len(arr) == 1:
#     #     if arr[0] % 3 == 1:
#     #         ans += (arr[0] // 3) * 2 + 1
#     #     elif arr[0] % 3 == 2:
#     #         ans += (arr[0] // 3) * 2 + 2
#     #     else:
#     #         ans += 2
#     #     arr.pop()
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    high = max(data)
    ans, h, j = 0, 0, 0
    arr = []
    for i in data:
        k = high - i
        if k % 3:
            if k > 6:
                ans += (k // 3) * 2
                k %= 3
            if k == 1:
                h += 1
            elif k == 2:
                j += 1
            else:
                arr.append(k)
        else:
            ans += (k // 3) * 2
    m = min(h, j)
    ans += 2 * m
    arr = sorted([1] * (h - m) + [2] * (j - m) + arr)

    if arr:
        # 6 : [1, 1, 4], [1, 5], [2, 4] 9 : [4, 5]
        print("#{} {}".format(test_case + 1, arr))
        print(ans)
        print(sum(arr))