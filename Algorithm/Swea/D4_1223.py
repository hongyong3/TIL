import sys
sys.stdin = open("D4_1223_input.txt", "r")

# 이전 풀이
# operators = {"+" : 0, "*" : 1}
#
# def operand():
#     global a, b
#     b = int(stack.pop())
#     a = int(stack.pop())
#
#
# for test_case in range(10):
#     N = int(input())
#     data = input()
#
#     a, b = 0, 0
#     stack = []
#     preorder = []
#     operator = []
#
#     for i in data:
#         if i.isdigit():
#             preorder.append(i)
#         else:
#             if len(operator) == 0:
#                 operator.append(i)
#             else:
#                 if operators[i] > operators[operator[- 1]]:
#                     operator.append(i)
#                 elif operators[i] <= operators[operator[- 1]]:
#                     preorder.append(operator.pop())
#                     operator.append(i)
#
#     while len(operator):
#         preorder.append(operator.pop())
#
#     for i in preorder:
#         if i.isdigit():
#             stack.append(i)
#         elif len(stack) >= 2:
#             if i == "+":
#                 operand()
#                 stack.append(a + b)
#             elif i == "*":
#                 operand()
#                 stack.append(a * b)
#     print("#{} {}".format(test_case + 1, *stack))

operators = {'+': 0, '*': 1}

for test_case in range(10):
    N = int(input())
    data = input()

    preorder = []
    temporary = []
    stack = []

    for i in data:
        if i.isdigit():
            preorder.append(i)
        else:
            if not temporary:
                temporary.append(i)
            else:
                if operators[i] > operators[temporary[- 1]]:
                    temporary.append(i)
                else:
                    preorder.append(temporary.pop())
                    temporary.append(i)

    preorder += temporary[:: - 1]

    for i in preorder:
        if i.isdigit():
            stack.append(int(i))
        if len(stack) >= 2:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
    print("#{} {}".format(test_case + 1, *stack))