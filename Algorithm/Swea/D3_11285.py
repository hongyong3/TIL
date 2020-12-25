import sys
sys.stdin = open("D3_11285_input.txt", "r")

# RunTime Error...
T = int(input())
for test_case in range(T):
    N = int(input())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        ans += int(220 - pow(x ** 2 + y ** 2, 0.5)) // 20
    print("#{} {}".format(test_case + 1, ans))