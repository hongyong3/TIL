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
1. 자리수가 같은 경우
    1) 만약 Q가 R보다 크면 바로 X
    2) 자리수별로 비교하면서 확인


2. 자리수가 다를 경우
    1) L과 R의 자리수 차이가 3이상이면
        (1) 만약 Q의 자리수가 R보다 크면 X
        (2) 만약 Q의 자리수가 R과 같으면
            - int(Q) <= int(R) O
            - int(Q) > int(R) X
        (3) 만약 Q의 자리수가 R과 작다면 O
    2) L과 R의 자리수 차이가 2이하면

'''
# 43 / 87
# T = int(input())
# for test_case in range(T):
#     L, R, Q = input().split()
#     arr = list(input().split())
#     ans = ''
#     lr, rr = len(L), len(R)
#     # 자리수가 같을 경우
#     if rr - lr == 0:
#         for i in arr:
#             if len(i) > rr:
#                 ans += 'X'
#                 continue
#
#             temp = 'O'
#             for j in range(len(i)):
#                 num = int(i[:j + 1])
#                 if not (int(L[:j + 1]) <= num <= int(R[:j + 1])):
#                     ans += 'X'
#                     break
#             else:
#                 ans += 'O'
#
#     # 자리수가 다를 경우
#     elif rr - lr < 3:
#         for i in arr:
#             # L의 자리수가 Q보다 크면
#             if lr > len(i):
#                 if
#             elif lr == len(i):
#                 pass
#             else:
#                 pass
#     else:
#         for i in arr:
#             if len(i) > rr:
#                 ans += 'X'
#                 continue
#             elif len(i) == rr:
#                 if int(i) > int(R):
#                     ans += 'X'
#                     continue
#             ans += 'O'
#     print("#{} {}".format(test_case + 1, ans))


# T = int(input())
# for test_case in range(T):
#     L, R, Q = input().split()
#     arr = input().split()
#     l, r = len(L), len(R)
#     ans = ''
#
#     for q in arr:
#         i = len(q)
#         if l != r:
#             if i < l:
#                 if int(q + L[i:]) >= int(L):
#                     ans += 'O'
#                 elif int(q + ('0' * (r - i))) <= int(R):
#                     ans += 'O'
#                 elif l < r - 1:
#                     ans += 'O'
#                 else:
#                     ans += 'X'
#             elif i == l:
#                 if int(q) >= int(L) or int(q + '0') <= int(R):
#                     ans += 'O'
#                 else:
#                     ans += 'X'
#             else:
#                 if i < r:
#                     ans += 'O'
#                 elif i == r and int(q) <= int(R):
#                     ans += 'O'
#                 else:
#                     ans += 'X'
#         else:
#             if int(L[:i]) <= int(q) <= int(R[:i]):
#                 ans += 'O'
#             else:
#                 ans += 'X'
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    L, R, Q = input().split()
    arr = input().split()
    l, r = len(L), len(R)
    ans = ''

    for q in arr:
        i = len(q)
        if l != r:
            if i < l:
                ans += 'O' if int(q + L[i:]) >= int(L) or int(q + ('0' * (r - i))) <= int(R) or l < r - 1 else 'X'
            elif i == l:
                ans += 'O' if int(q) >= int(L) or int(q + '0') <= int(R) else 'X'
            else:
                ans += 'O' if i < r or i == r and int(q) <= int(R) else 'X'
        else:
            ans += 'O' if int(L[:i]) <= int(q) <= int(R[:i]) else 'X'
    print("#{} {}".format(test_case + 1, ans))