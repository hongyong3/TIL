import sys
sys.stdin = open("5658_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = input() * 2
    ans = set()

    for i in range(N // 4):
        for j in range(1, 5):
            ans.add(int(data[i + (N // 4) * (j - 1) : i + (N // 4) * j], 16))
    print("#{} {}".format(test_case + 1, sorted(ans)[:: - 1][K - 1]))