import sys
sys.stdin = open("D4_1223_input.txt", "r")

operators = {"+" : 0, "*" : 1}

def operand():
    global a, b
    b = int(stack.pop())
    a = int(stack.pop())


for test_case in range(10):
    N = int(input())
    data = input()

    a, b = 0, 0
    stack = []
    preorder = []
    operator = []

    for i in data:
        if i.isdigit():
            preorder.append(i)
        else:
            if len(operator) == 0:
                operator.append(i)
            else:
                if operators[i] > operators[operator[- 1]]:
                    operator.append(i)
                elif operators[i] <= operators[operator[- 1]]:
                    preorder.append(operator.pop())
                    operator.append(i)

    while len(operator):
        preorder.append(operator.pop())

    for i in preorder:
        if i.isdigit():
            stack.append(i)
        elif len(stack) >= 2:
            if i == "+":
                operand()
                stack.append(a + b)
            elif i == "*":
                operand()
                stack.append(a * b)
    print("#{} {}".format(test_case + 1, *stack))