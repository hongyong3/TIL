def Forth():
    global a, b
    a = int(stack.pop(-2))
    b = int(stack.pop())

import sys
sys.stdin = open("계산기3_input.txt", "r")
for test_case in range(10):
    N = int(input())
    data = input()

    operators = {'(' : 0, '+' : 1, '*' : 2}
    operator = []
    operand = []

    for i in data:
        if i.isdigit():
            operand.append(i)
        else:
            if len(operator) == 0:
                operator.append(i)
            else:
                if i == ")":
                    while operator[-1] != "(":
                       operand.append(operator.pop())
                    operator.pop()
                elif i == "(":
                    operator.append(i)
                elif operators[i] > operators[operator[-1]]:
                    operator.append(i)
                elif operators[i] <= operators[operator[-1]]:
                    operand.append(operator.pop())
                    operator.append(i)

    stack = []
    a, b = 0, 0
    for i in operand:
        if i.isdigit():
            stack.append(i)
        elif len(stack) >= 2:
            if i == "+":
                Forth()
                stack.append(a + b)
            elif i == "*":
                Forth()
                stack.append(a * b)

    print(f'#{test_case+1} {int(stack[0])}')



