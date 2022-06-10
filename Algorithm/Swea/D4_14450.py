import sys
sys.stdin = open("D4_14450_input.txt", "r")

# 40 / 87
T = int(input())
for test_case in range(T):
    L, R, Q = input().split()
    arr = list(input().split())
    ans = ''
    idx = max(len(L), len(R))
    for i in arr:
        if len(i) > idx or int(i) > int(R):
            ans += 'X'
            continue
        for k in range(len(i)):
            a, b, c = int(L[: k + 1]), int(i[: k + 1]), int(R[: k + 1])
            if not (a <= b <= c):
                ans += 'X'
                break
        else:
            ans += 'O'
    print("#{} {}".format(test_case + 1, ans))