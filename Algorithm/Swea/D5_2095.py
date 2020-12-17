import sys
sys.stdin = open("D5_2095_input.txt", "r")

# def dp(x, dep):
#     if r[x // 10][dep]:
#         return r[x // 10][dep]
#     r[x // 10][dep] = 1
#     res = d[x // 10][dep]
#     if dep == N:
#         res = 0
#         return res
#     res = float('inf')
#     for i in range(11):
#         if c[dep] + 10 * i < x:
#             cur = dp(c[dep] + 10 * i, dep + 1)
#         else:
#             diff = c[dep] + 10 * i - x
#             cur = dp(c[dep] + 10 * i, dep + 1) + diff
#         if res > cur:
#             res = cur
#         else:
#             break
#     return res


T = int(input())
a = [0] * 999
b = [0] * 999
c = [0] * 999
# d = [[float('inf')] * 652 for _ in range(602)]
# r = [[0] * 602 for _ in range(652)]
for test_case in range(T):
    N = int(input())
    data = input()
    password = input()

    for i in range(N):
        a[i] = int(data[i])
        b[i] = int(password[i])
        c[i] = (b[i] - a[i] + 10) % 10

    # for i in range(N + 1):
    #     for j in range(N + 1):
    #         r[i][j] = 0
    #         d[i][j] = float('inf')
    # ans = dp(0, 0)
    # print("#{}\n{}".format(test_case + 1, ans))