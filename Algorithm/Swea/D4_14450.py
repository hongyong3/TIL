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

def same():
    pass

def diff():
    pass

T = int(input())
for test_case in range(T):
    L, R, Q = input().split()
    chklen = 1 if len(str(L)) == len(str(R)) else 0
    print(chklen)
    arr = list(input().split())