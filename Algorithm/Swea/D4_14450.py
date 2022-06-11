import sys
sys.stdin = open("D4_14450_input.txt", "r")

# 40 / 87
T = int(input())
for test_case in range(1):
    L, R, Q = input().split()
    arr = list(input().split())
    ans = ''
    idx = max(len(L), len(R))
    for i in arr:
        if len(i) > idx or int(i) > int(R):
            ans += 'X'
            continue

        for j in range(len(i)):
            b = int(i[: j + 1])
            for k in range(len(L)):
                pass
            for k in range(len(R)):
                pass


            a, c = int(L[: j + 1]), int(R[: j + 1])
            if not (a <= b <= c):
                ans += 'X'
                break
        else:
            ans += 'O'
    print("#{} {}".format(test_case + 1, ans))