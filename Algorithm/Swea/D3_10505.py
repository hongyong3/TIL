import sys
sys.stdin = open("D3_10505_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    avg = sum(data) / N
    ans = 0
    for i in data:
        if i <= avg:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))