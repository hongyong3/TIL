import sys
sys.stdin = open("D4_14450_input.txt", "r")

# 40 / 87
# T = int(input())
# for test_case in range(T):
#     L, R, Q = input().split()
#     arr = list(input().split())
#     ans = ''
#     # idx, jdx = len(L), len(R)
#     for i in arr:
#         if len(i) > len(R):
#             ans += 'X'
#             continue
#         chk = True
#         a = 1
#         while chk and a <= max(len(L), len(i)):
#             l = int(L[:a])
#             x = int(i[:a])
#             if l > x:
#                 if a == len(i):
#                     chk = False
#                     break
#             a += 1
#         if chk == False:
#             ans += 'X'
#             continue
#
#         a = 1
#         while chk and a <= len(R):
#             r = int(R[:a])
#             x = int(i[:a])
#             if x > r:
#                 if a <= len(R):
#                     a += 1
#                     continue
#                 else:
#                     chk = False
#                     break
#             a += 1
#         if chk == False:
#             ans += 'X'
#             continue
#         else:
#             ans += 'O'
#
#     print(ans)


'''
1. 자리수가 같을 경우
    1) 만약 q가 r보다 크면 바로 X
2. 자리수가 다를 경우
'''

T = int(input())
for test_case in range(T):
    L, R, Q = input().split()
    arr = list(input().split())
    ans = ''
    lr, rr = len(L), len(R)
    # 자리수가 같을 경우
    if rr - lr == 0:
        for i in arr:
            if len(i) > rr:
                ans += 'X'
                continue

            temp = 'O'
            for j in range(len(i)):
                num = int(i[:j + 1])
                if not(int(L[:j + 1]) <= num <= int(R[:j + 1])):
                    ans += 'X'
                    break
            else:
                ans += 'O'

    # 자리수가 다를 경우
    elif rr - lr <= 2:
        pass
    else:
        for i in arr:
            if len(i) > rr:
                ans += 'X'
                continue
            ans += 'O'
    print("#{} {}".format(test_case + 1, ans))