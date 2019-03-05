import sys
sys.stdin = open("사칙연산_input.txt", "r")

for test_case in range(10):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for i in range(N):
        input_T = input().split()
        # print(input_T)
        tree[int(input_T[0])] = input_T[1:]
    stack = []
    def postorder(n):
        if len(tree[n]) > 1:
            postorder(int(tree[n][1]))
            postorder(int(tree[n][2]))
            stack.append(tree[n][0])
        else:
            stack.append(tree[n][0])
    postorder(1)
    i = 0
    op = ['+', '-', '*', '/']
    while len(stack) != 1:
        if stack[i] in op:
            if stack[i] == '+':
                stack[i] = int(stack[i-2]) + int(stack[i-1])
            elif stack[i] == '-':
                stack[i] = int(stack[i - 2]) - int(stack[i - 1])
            elif stack[i] == '*':
                stack[i] = int(stack[i - 2]) * int(stack[i - 1])
            else:
                stack[i] = int(stack[i - 2]) // int(stack[i - 1])
            stack.pop(i-2)
            stack.pop(i-2)
            i -= 2
        i += 1

    print('#{} {}'.format(test_case+1, stack[0]))