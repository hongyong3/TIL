import sys
sys.stdin = open("D3_11445_input.txt", "r")

T = int(input())
for test_case in range(T):
    P, Q = input(), input()
    data = sorted([Q, P])
    ans = 'Y'
    if data[0] == Q:
        ans = 'N'
    else:
        if len(P) < len(Q):
            i = len(P)
            if P == Q[: i] and Q[i] == 'a' and len(Q) == i + 1:
                ans = 'N'
    print("#{} {}".format(test_case + 1, ans))

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