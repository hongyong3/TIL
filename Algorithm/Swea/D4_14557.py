import sys
sys.stdin = open("D4_14557_input.txt", "r")

# def flip(idx, val):
#     global S
#     if val == '0':
#         S[idx] = '1'
#     elif val == '1':
#         S[idx] = '0'
#
#
# T = int(input())
# for test_case in range(T):
#     S = list(input())
#
#     N = cnt = len(S)
#     i, chk = 0, 0
#
#     while i < N:
#         if cnt == 0:
#             break
#         if S[i] == '1':
#             chk = 1
#             cnt -= 1
#             S[i] = '2'
#             if i == 0:
#                 flip(i + 1, S[i + 1])
#             elif i == N - 1:
#                 flip(i - 1, S[i - 1])
#             else:
#                 flip(i - 1, S[i - 1])
#                 flip(i + 1, S[i + 1])
#         i += 1
#         if i == N:
#             if chk:
#                 i = 0
#                 chk = 0
#     ans = 'no' if cnt else 'yes'
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    S = input()
    print("#{} {}".format(test_case + 1, 'yes' if S.count('1') % 2 else 'no'))