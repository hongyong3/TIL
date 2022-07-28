import sys
sys.stdin = open("D5_14559_input.txt", "r")

# 8 // 27
# T = int(input())
# for test_case in range(T):
#     N, S, E = map(int, input().split())
#     M = int(input())
#     arr = []
#     chk1, chk2 = 0, 0
#     ans = 1
#     for _ in range(M):
#         a, b = 0, 0
#         A, B = map(int, input().split())
#         if S % A == 0:
#             a = 1
#             chk1 = 1
#         if E % B == 0:
#             b = 1
#             chk2 = 1
#         arr.append([a, b])
#     if chk1 == 0 or chk2 == 0:
#         ans = - 1
#     else:
#         if [1, 1] not in arr:
#             ans = 2
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, S, E = map(int, input().split())
    M = int(input())
    arr = []
    chk1, chk2 = 0, 0
    for _ in range(M):
        a, b = 0, 0
        A, B = map(int, input().split())
        if S % A == 0:
            a = 1
            chk1 = 1
        if E % B == 0:
            b = 1
            chk2 = 1
        arr.append([a, b])
    if chk1 == chk2 != 1:
        ans = - 1
    else:
        if [1, 1] in arr:
            ans = 1
        if [1, 1] not in arr:
            ans = 2
            # print("#{} {}".format(test_case + 1, 2))
    print("#{} {}".format(test_case + 1, ans))