import sys
sys.stdin = open("D3_8338_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    for i in data:
        if i <= 1 or ans <= 1:
            ans += i
        else:
            ans *= i
    print("#{} {}".format(test_case + 1, ans))