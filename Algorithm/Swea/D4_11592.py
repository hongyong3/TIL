import sys
sys.stdin = open("D4_11592_input.txt", "r")

T = int(input())
for test_case in range(T):
    D, N = map(int, input().split())
    time = 0
    for _ in range(N):
        K, S = map(int, input().split())
        if time < (D - K) / S:
            time = (D - K) / S
    print("#{} {}".format(test_case + 1, D / time))