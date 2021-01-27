import sys
sys.stdin = open("D6_11389_input.txt", "r")

# Runtime Error 1 / 26
T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    num = list(map(int, input().split()))
    X %= 1000006
    ans = 0
    for i in range(N):
        temp = num[i]
        if temp == X:
            ans += 1
        for j in range(i + 1, N):
            temp *= num[j]
            if temp == X:
                ans += 1

    print("#{} {}".format(test_case + 1, ans))