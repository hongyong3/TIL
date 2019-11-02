import sys
sys.stdin = open("D4_4111_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K, arr = int(input()), int(input()), []
    data = sorted(map(int, input().split()))
    if N <= K:
        print("#{} {}".format(test_case + 1, 0))
        continue
    for i in range(N - 1):
        arr.append(data[i + 1] - data[i])
    arr = sorted(arr)[:len(arr) - (K - 1)]
    print("#{} {}".format(test_case + 1, sum(arr)))