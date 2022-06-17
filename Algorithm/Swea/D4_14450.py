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
        jdx = 0
        flag = True
        while jdx < max(len(i), len(L)):
            a = int(L[: jdx + 1])
            b = int(i[: jdx + 1])
            if a > b:
                flag = False
            jdx += 1
        # for j in range(len(i)):
        #     flag = True
        #     b = int(i[: j + 1])
        #     # l과 b 비교
        #     jdx = 0
        #     while jdx < max(len(i), len(L)):
        #         if int(j)
        #     for k in range(len(L)):
        #         pass
        #     # r과 b 비교
        #     for k in range(len(R)):
        #         pass
        #
        #     a, c = int(L[: j + 1]), int(R[: j + 1])
        #     if not (a <= b <= c):
        #         ans += 'X'
        #         break
        # else:
        #     ans += 'O'
            
    print("#{} {}".format(test_case + 1, ans))