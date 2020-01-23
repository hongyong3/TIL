import sys
sys.stdin = open("D4_1218_input.txt", "r")

# for test_case in range(10):
#     N = input()
#     data = input()
#
#     ans = 1
#     stack = []
#
#     for i in data:
#         if i in '[{(<':
#             stack.append(i)
#         else:
#             if not stack:
#                 ans = 0
#                 break
#             else:
#                 if stack[- 1] == '<' and i == '>':
#                     stack.pop()
#                 elif stack[- 1] == '(' and i == ')':
#                     stack.pop()
#                 elif stack[- 1] == '[' and i == ']':
#                     stack.pop()
#                 elif stack[- 1] == '{' and i == '}':
#                     stack.pop()
#                 else:
#                     ans = 0
#     print("#{} {}".format(test_case + 1, ans))


# 아스키코드를 이용한 풀이
# 아스키코드를 보면
#   '(', ')' -> 40번, 41번
#   '<', '>' -> 60번, 62번
#   '[', ']' -> 91번, 93번
#   '{', '}' -> 123번, 125번이다.
# 즉, 현재 ord(stack[- 1]) // 10과 ord(i) // 10이 같다면, 괄호의 짝이 맞다고 할 수 있다.


for test_case in range(10):
    N = input()
    data = input()
    stack = []
    ans = 1

    for i in data:
        if i in '([{<':
            stack.append(i)
        else:
            if not stack:
                ans = 0
                break
            else:
                if ord(stack[- 1]) // 10 == ord(i) // 10:
                    stack.pop()
                else:
                    ans = 0
                    break
    print("#{} {}".format(test_case + 1, ans))