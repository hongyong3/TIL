import sys
sys.stdin = open("D3_11445_input.txt", "r")

# 76 / 100
# T = int(input())
# for test_case in range(3):
#     P = input()
#     Q = input()
#     ans = "Y"
#     chk = True
#     i, j = 0, 0
#
#     while chk and len(P) > i and len(Q) > j:
#         if P[i] > Q[j]:
#             chk = False
#             ans = 'N'
#         elif P[i] == Q[j]:
#             i += 1
#             j += 1
#         else:
#             break
#     if i == len(P):
#         if j < len(Q) and Q[j] == 'a':
#             ans = 'N'
#     print("#{} {}".format(test_case + 1, ans))

# 76 / 100
# T = int(input())
# for test_case in range(T):
#     p, q = input().replace(" ", ""), input().replace(" ", "")
#     ans = 'Y'
#     chk = True
#     i, j = 0, 0
#
#     while chk and i < len(p):
#         if p[i] < q[j]:
#             chk = False
#         else:
#             i += 1
#             j += 1
#     if len(q) - len(p) == 1 and q[- 1] == 'a':
#         ans = 'N'
#     print("#{} {}".format(test_case + 1, ans))

# 76 / 100
# ..? 뭐지..
# T = int(input())
# for test_case in range(T):
#     p, q = input().replace(" ", ""), input().replace(" ", "")
#     if len(q) - len(p) == 1:
#         if q[- 1] == 'a':
#             ans = 'N'
#     else:
#         ans = 'Y'
#     print("#{} {}".format(test_case + 1, ans))

# 93 / 100
T = int(input())
for test_case in range(T):
    p, q = input().strip().replace(" ", ""), input().strip().replace(" ", "")
    if len(q) - len(p) == 1:
        if q[- 1] == 'a':
            ans = 'N'
    else:
        ans = 'Y'
    print("#{} {}".format(test_case + 1, ans))