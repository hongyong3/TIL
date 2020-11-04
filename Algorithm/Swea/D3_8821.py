import sys
sys.stdin = open("D3_8821_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = list(map(int, input()))
    num = [0] * 10
    ans = 0
    for i in N:
        num[i] += 1

    for i in num:
        if i % 2:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))