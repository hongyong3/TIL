import sys
sys.stdin = open("D2_4864_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     pattern = input()[:: - 1]
#     text = input()
#     i = len(pattern) - 1
#     mat = 0
#
#     while not mat and i < len(text):
#         if pattern[0] != text[i]:
#             if text[i] in pattern:
#                 i += pattern.index(text[i])
#             else:
#                 i += len(pattern)
#         else:
#             for x, y in zip(range(i, i - len(pattern), - 1), pattern):
#                 if text[x] == y:
#                     mat = 1
#                 else:
#                     mat, i = 0, x
#                     break
#     print("#{} {}".format(test_case + 1, mat))

# 더 쉽게..
T = int(input())
for test_case in range(T):
    w = input()
    s = input()
    print("#{} {}".format(test_case + 1, 1 if w in s else 0))