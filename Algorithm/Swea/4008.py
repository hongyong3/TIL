import sys
sys.stdin = open("4008_input.txt", "r")

def permutation(opers):
    stack = [(opers[:], [])]
    while stack:
        oper, temp = stack.pop()
        if sum(oper) == 0:
            yield temp
        for i in range(4):
            if oper[i]:
                oper[i] -= 1
                temp.append(i)
                stack.append((oper[:], temp[:]))
                temp.pop()
                oper[i] += 1

T = int(input())
for test_case in range(T):
    N = int(input())
    operators = list(map(int, input().split()))
    data = list(map(int, input().split()))
    minNum, maxNum = float('inf'), - float('inf')

    for perm in permutation(operators):
        subAns = data[0]
        i = 0
        for cal in perm:
            i += 1
            if cal == 0:
                subAns += data[i]
            elif cal == 1:
                subAns -= data[i]
            elif cal == 2:
                subAns *= data[i]
            else:
                if subAns < 0 and subAns % data[i]:
                    subAns //= data[i]
                    subAns += 1
                else:
                    subAns //= data[i]

        if minNum > subAns:
            minNum = subAns
        if maxNum < subAns:
            maxNum = subAns

    print("#{} {}".format(test_case + 1, maxNum - minNum))