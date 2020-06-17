import sys
sys.stdin = open("D5_3977_input.txt", "r")

decimal = [0] * 1000001
decimal[0], decimal[1] = 1, 1
for i in range(2, 1000001):
    for j in range(i << 1, 1000001, i):
        decimal[j] = 1

T = int(input())
for test_case in range(T):
    L, R = map(int, input().split())
    ans = 0
    if L <= 2:
        ans += 1

    for i in range(L, R + 1):
        if not decimal[i] and i % 4 == 1:
            ans += 1

    print("#{} {}".format(test_case + 1, ans))