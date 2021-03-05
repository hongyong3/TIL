import sys
sys.stdin = open("D1_11419_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = [0] * 10
    for i in range(6):
        num[N % 10] += 1
        N //= 10

    cnt, i, ans = 0, 0, "Lose"
    while i < 10:
        if num[i] >= 3:
            num[i] -= 3
            cn
            t += 1
            continue
        if num[i] >= 1 and num[i + 1] >= 1 and num[i + 2] >= 1:
            num[i] -= 1
            num[i + 1] -= 1
            num[i + 2] -= 1
            cnt += 1
            continue
        i += 1
    if cnt == 2:
        ans = "Baby Gin"
    print('#%d %s' % (test_case, ans))