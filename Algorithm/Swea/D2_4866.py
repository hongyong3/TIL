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

# def solve(x):
#     if len(x) % 2:
#         return 0
#     if bracket[x[0]] + 2 == bracket[x[- 1]]:
#         for i in range(len(x) - 1):
#             if x[i] == '(' and x[i + 1] == '}' or x[i] == '{' and x[i + 1] == ')':
#                 return 0
#         return 1
#     return 0
#
# bracket= {"(": 0, "{": 1, ")": 2, "}": 3}
# T = int(input())
# for test_case in range(T):
#     data = [x for x in input() if x in bracket]
#     print("#{} {}".format(test_case + 1, solve(data)))

T = int(input())
List_Check = []
def arr_check(str):
    for i in range(len(str)):

        if str[i] == '{' or str[i] == '(':
            List_Check.append(str[i])

        elif str[i] == '}' or str[i] == ')':

            if len(List_Check) == 0:

                return 0

            elif List_Check[-1] == '{':
                List_Check.pop(-1)

            elif List_Check[-1] == '(':

                List_Check.pop(-1)

    if len(List_Check) == 0:
        return 1
    else:
        return 0

for t in range(1,T+1):
    str = input()
    ch = arr_check(str)
    List_Check = []
    print("#{} {}".format(t, ch))