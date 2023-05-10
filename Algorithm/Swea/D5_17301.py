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
    i = 0
    l = Q - N
    while l:
        ai = total // N
        print(ai, end = ' ')
        # total -= arrA[i]
        # total += ans[- 1]
        l -= 1
        i += 1
    print()
    # print("#{}".format(test_case + 1), *ans)