import sys
sys.stdin = open("D5_17301_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arrA = list(map(int, input().split()))
    Q = int(input())
    arrX = list(map(int, input().split()))
    print("#{}".format(test_case + 1), *arrA, end=' ')
    total = sum(arrA)
    i, j = 0, 0
    l = Q - N
    e = [total // N]

    while l:
        ai = total // N
        e.append(ai)
        print(ai, end = ' ')
        if i < N:
            total += ai - arrA[i]
            i += 1
        else:
            total += ai - e[j]
            j += 1
        l -= 1
    print()