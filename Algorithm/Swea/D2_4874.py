import sys
sys.stdin = open("D2_4874_input.txt", "r")

# 이전 풀이
# def Forth(data):
#     for i in range(len(data)):
#         if data[i] not in operators and data[i] != '.':
#             stack.append(data[i])
#
#         if data[i] in operators:
#             if len(stack) <= 1:
#                 return 'error'
#
#             elif data[i] == '+':
#                 stack[-2] = int(stack[-2]) + int(stack[-1])
#                 stack.pop()
#
#             elif data[i] == '-':
#                 stack[-2] = int(stack[-2]) - int(stack[-1])
#                 stack.pop()
#
#             elif data[i] == '*':
#                 stack[-2] = int(stack[-2]) * int(stack[-1])
#                 stack.pop()
#
#             elif data[i] == '/':
#                 stack[-2] = int(stack[-2]) // int(stack[-1])
#                 stack.pop()
#
#         if data[i] == '.':
#             if len(stack) > 1:
#                 return "error"
#             else:
#                 return stack[0]
#
# T = int(input())
# for test_case in range(T):
#     data = input().split()
#
#     operators = ['+', '-', '*', '/']
#     stack = []
#     print(f'#{test_case + 1} {Forth(data)}')


def Forth(data):
    for i in data:
        if i.isdigit():
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) < 2:
                return 'error'
            elif i == '+':
                stack.append(stack.pop(- 2) + stack.pop(- 1))
            elif i == '-':
                stack.append(stack.pop(- 2) - stack.pop(- 1))
            elif i == '*':
                stack.append(stack.pop(- 2) * stack.pop(- 1))
            elif i == '/':
                stack.append(stack.pop(- 2) // stack.pop(- 1))
        if i == '.':
            if len(stack) > 1:
                return 'error'
            return stack[- 1]

T = int(input())
for test_case in range(T):
    data = list(map(str, input().split()))
    stack = []
    print("#{} {}".format(test_case + 1, Forth(data)))