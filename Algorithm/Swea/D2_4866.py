import sys
sys.stdin = open("D2_4866_input.txt", "r")

# 이전 풀이
# def push(x):
#     if len(x) % 2 != 0:
#         return 0
#
#     if x[0] == '(' and x[-1] == ')':
#         for i in range(len(x) - 1):
#             if x[i] == '(' and x[i + 1] == '}':
#                 return 0
#             if x[i] == '{' and x[i + 1] == ')':
#                 return 0
#         else:
#             return 1
#
#     if x[0] == '{' and x[-1] == '}':
#         for i in range(len(x) - 1):
#             if x[i] == '(' and x[i + 1] == '}':
#                 return 0
#             if x[i] == '{' and x[i + 1] == ')':
#                 return 0
#         else:
#             return 1
#     else:
#         return 1
#
# T = int(input())
# for test_case in  range(T):
#     data = list(input())
#     x = []
#     for i in data:
#         if i == '(' or i == '{' or i == ')' or i == '}':
#             x.append(i)
#     print(f'#{test_case + 1} {push(x)}')

def solve(x):
    if len(x) % 2:
        return 0
    if bracket[x[0]] + 2 == bracket[x[- 1]]:
        for i in range(len(x) - 1):
            if x[i] == '(' and x[i + 1] == '}' or x[i] == '{' and x[i + 1] == ')':
                return 0
        return 1

bracket= {"(": 0, "{": 1, ")": 2, "}": 3}
T = int(input())
for test_case in range(T):
    data = [x for x in input() if x in bracket]
    print("#{} {}".format(test_case + 1, solve(data)))