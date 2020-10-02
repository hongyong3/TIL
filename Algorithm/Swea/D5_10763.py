import sys
sys.stdin = open("D5_10763_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    for i, j in zip(data, sorted(data)):
        if i != j:
            ans += 1
    print("#{} {}".format(test_case + 1, "%.6f" % ans))