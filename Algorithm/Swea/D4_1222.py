import sys
sys.stdin = open("D4_1222_input.txt", "r")

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
#             operator.append(i)
#
#     while len(operator):
#         preorder.append(operator.pop())
#
#     for i in preorder:
#         if i.isdigit():
#             stack.append(i)
#         elif len(stack) >= 2:
#             operand()
#             stack.append(a + b)
#     print("#{} {}".format(test_case + 1, *stack))

# 편법..
for test_case in range(10):
    N = input()
    data = input()
    mat = 0
    for i in data:
        if i.isdigit():
            mat += int(i)
    print("#{} {}".format(test_case + 1, mat))