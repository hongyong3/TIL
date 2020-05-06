import sys
sys.stdin = open("D5_1245_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    x, m = data[:N], data[N:]
    ans = []

    for i in range(1, N):
        low, high = x[i - 1], x[i]
        while high - low > 10 ** - 12:
            mid = (low + high) / 2
            left, right = 0, 0
            for j in range(N):
                force = m[j] / (mid - x[j]) ** 2
                if x[j] < mid:
                    left += force
                else:
                    right += force
            if left < right:
                high = mid
            else:
                low = mid
        ans.append('%.10f' % mid)
    print("#{}".format(test_case + 1), *ans)

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     ans = []
#
#     for i in range(1, N):
#         s, e = data[i - 1], data[i]
#         while e - s > 10 ** - 12:
#             m, l, r = (s + e) / 2, 0, 0
#             for j in range(N):
#                 f = data[N + j] / (data[j] - m) ** 2
#                 if data[j] < m:
#                     l += f
#                 else:
#                     r += f
#             if l < r:
#                 e = m
#             else:
#                 s = m
#         ans.append('%.10f' % m)
#     print("#{}".format(test_case + 1), *ans)