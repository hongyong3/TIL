import sys
sys.stdin = open("D4_3378_input.txt", "r")
from itertools import product

T = int(input())
for test_case in range(T):
    p, q = map(int, input().split())
    before = [input() for _ in range(p)]
    after = [input() for _ in range(q)]

    a, b, c = 0, 0, 0   # before 소, 중, 대
    beforeDot = []
    beforeBracket = [[0, 0, 0]]

    for i in before:
        beforeDot.append(len(i) - len(i.lstrip('.')))
        for j in i:
            if j == '(':
                a += 1
            if j == ')':
                a -= 1
            if j == '{':
                b += 1
            if j == '}':
                b -= 1
            if j == '[':
                c += 1
            if j == ']':
                c -= 1
        beforeBracket.append([a, b, c])

    candidate = []

    for i in product(range(1, 21), repeat = 3):
        R1, C1, S1 = i
        for j in range(1, p):
            a1, b1, c1 = beforeBracket[j]
            if R1 * a1 + C1 * b1 + S1 * c1 != beforeDot[j]:
                break
        else:
            candidate.append([R1, C1, S1])

    d, e, f = 0, 0, 0   # after 소, 중, 대
    afterDot = [set() for _ in range(q)]
    afterBracket = []

    for i in after:
        for j in i:
            if j == '(':d += 1
            if j == ')':d -= 1
            if j == '{':e += 1
            if j == '}':e -= 1
            if j == '[':f += 1
            if j == ']':f -= 1
        afterBracket.append([d, e, f])

    for i in range(q):
        d1, e1, f1 = afterBracket[i]
        for j in candidate:
            R2, C2, S2 = j
            afterDot[i].add(R2 * d1 + C2 * e1 + S2 * f1)
        if candidate == []:
            afterDot[i] = - 1
        elif len(afterDot[i]) == 1:
            afterDot[i] = afterDot[i].pop()
        else:
            afterDot[i] = - 1

    afterDot = [0] + afterDot[: - 1]
    print("#{} ".format(test_case + 1), *afterDot)