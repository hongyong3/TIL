import sys
sys.stdin = open("D4_6719_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = sorted(list(map(int, input().split())))[N - K :]
    ans = 0
    for i in data:
        ans = (ans + i) / 2
    print("#{} {}".format(test_case + 1, "%0.6f" % ans))