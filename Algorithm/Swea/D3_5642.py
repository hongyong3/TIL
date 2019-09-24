import sys
sys.stdin = open("D3_5642_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(1, N):
        if data[i - 1] > 0 and data[i - 1] + data[i] > 0: data[i] += data[i - 1]
    print("#{} {}".format(test_case + 1, max(data)))