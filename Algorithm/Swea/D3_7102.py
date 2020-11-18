import sys
sys.stdin = open("D3_7102_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     arr, ans, num = [0] * (N + M + 1), [], 0
#
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             arr[i + j] += 1
#
#     num = max(arr)
#
#     for i in range(2, N + M + 1):
#         if num == arr[i]:
#             ans.append(i)
#     print("#{}".format(test_case + 1), *ans)

# 점화식
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    a, b = (M + 1, N + 1) if N > M else (N + 1, M + 1)
    ans = []
    for i in range(a, b + 1):
        ans.append(i)
    print("#{}".format(test_case + 1), *ans)