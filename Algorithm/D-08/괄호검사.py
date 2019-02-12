def push(x):
    if len(x) % 2 != 0:
        return 0

    if x[0] == '(' and x[-1] == ')':
        for i in range(len(x) - 1):
            if x[i] == '(' and x[i + 1] == '}':
                return 0
            if x[i] == '{' and x[i + 1] == ')':
                return 0
        else:
            return 1

    if x[0] == '{' and x[-1] == '}':
        for i in range(len(x) - 1):
            if x[i] == '(' and x[i + 1] == '}':
                return 0
            if x[i] == '{' and x[i + 1] == ')':
                return 0
        else:
            return 1
    else:
        return 1


import sys
sys.stdin =open("괄호검사_input.txt", "r")
T = int(input())
for test_case in  range(T):
    data = list(input())
    x = []
    for i in data:
        if i == '(' or i == '{' or i == ')' or i == '}':
            x.append(i)


    print(f'#{test_case + 1} {push(x)}')