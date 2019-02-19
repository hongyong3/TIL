def Forth(data):
    for i in range(len(data)):
        if data[i] not in operators and data[i] != '.':
            stack.append(data[i])

        if data[i] in operators:
            if len(stack) <= 1:
                return 'error'

            elif data[i] == '+':
                stack[-2] = int(stack[-2]) + int(stack[-1])
                stack.pop()

            elif data[i] == '-':
                stack[-2] = int(stack[-2]) - int(stack[-1])
                stack.pop()

            elif data[i] == '*':
                stack[-2] = int(stack[-2]) * int(stack[-1])
                stack.pop()

            elif data[i] == '/':
                stack[-2] = int(stack[-2]) // int(stack[-1])
                stack.pop()

        if data[i] == '.':
            if len(stack) > 1:
                return "error"
            else:
                return stack[0]

import sys
sys.stdin =open("Forth_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input().split()

    operators = ['+', '-', '*', '/']
    stack = []
    print(f'#{test_case + 1} {Forth(data)}')