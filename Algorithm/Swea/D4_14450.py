import sys
sys.stdin = open("D4_14450_input.txt", "r")

T = int(input())
for test_case in range(T):
    L, R, Q = input().split()
    # arr = list(map(int, input().split()))
    arr = list(input().split())
    ans = ''

    for i in arr:
        for j in range(len(i)):
            if int(L[j]) <= int(i[0]) <= int(R[j]):
                temp = 1
            else:
                temp = 0
                continue
        if temp == 1:
            ans += 'O'
        else:
            ans += 'X'
    print(ans)