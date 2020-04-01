import sys
sys.stdin = open("D4_1224_input.txt", "r")

# 이전 풀이
# # 방법
# # (1) 중위 표기법 -> 후위 표기법 (스택 필요)
# #   1. 피연산자는 출력.
# #   2. 연산자는 스택이 비어있으면 스택에 push.
# #   3. "(" 이면 무조건 push.
# #   4. ")" 이면 stack에서 여는 괄호가 나올 때까지 pop.
# #   5. "(" 가 스택에 push 된 후 ")" 가 나올 때까지 "(" 가 pop이 되면 안되므로, "(" 의 우선 순위는 제일 작음.
# #         우선순위는 '* or /' >> '+ or -' >> '('
# #   6. 괄호는 출력 X(즉, pop 해야함).
# #   7. 연산자는 스택이 비어있지 않으면 스택에 있는 연산자와 현재 연산자의 우선순위를 비교해
# #      스택에 있는 연산자와의 우선순위가 같거나 크면 스택에 있는 연산자를 pop 한 후 현재 연산자를 스택에 push
# #   8. 만약 7번에서 우선순위가 현재 연산자가 더 크면 현재 연산자를 push(스택에서 pop X).
# #   9. 수식이 끝나면 스택이 빌 때까지 pop.
#
# # (2) 후위 표기법 계산 (스택 필요)
# #   1. 피연산자면 스택에 push.
# #   2. 연산자를 만나면 pop을 두 번하고, 각각 값을 저장한 후, 연산자에 맡는 계산.
# #       여기서 주의해야할 점은 스택은 LIFO이므로  A, B 순으로 push 했다면, B, A 순으로 pop이 되므로 주의
# #       b = int(stack.pop())
# #       a = int(stack.pop())
# #   3. 계산을 한 뒤, 결과 값을 다시 스택에 push -> 이 과정을 수식이 끝날 때까지 반복.
# #   4. 수식이 끝났다면 스택에 마지막 남은 값이 결과 값.
#
# operators = {'(' : 0, '+' : 1, '*' : 2}
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
#     a, b = 0, 0
#     stack = []
#     operator = []
#     preorder = []
#
#     for i in data:
#         if i.isdigit():
#             preorder.append(i)
#         else:
#             if len(operator) == 0:
#                 operator.append(i)
#             else:
#                 if i == ')':
#                     while operator[- 1] != '(':
#                         preorder.append(operator.pop())
#                     operator.pop()
#                 elif i == '(':
#                     operator.append(i)
#                 elif operators[i] <= operators[operator[- 1]]:
#                     preorder.append(operator.pop())
#                     operator.append(i)
#                 elif operators[i] > operators[operator[- 1]]:
#                     operator.append(i)
#
#
#     for i in preorder:
#         if i.isdigit():
#             stack.append(i)
#         elif len(stack) >= 2:
#             if i == '+':
#                 operand()
#                 stack.append(a + b)
#             elif i == '*':
#                 operand()
#                 stack.append(a * b)
#     print("#{} {}".format(test_case + 1, stack[0]))

operators = {'(': 0, '+': 1, '*': 2}
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
                if i == '(':
                    temporary.append(i)
                elif i == ')':
                    while temporary[- 1] != '(':
                        preorder.append(temporary.pop())
                    temporary.pop()
                elif operators[i] > operators[temporary[- 1]]:
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