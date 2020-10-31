import sys
sys.stdin = open("D3_10032_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    print("#{} {}".format(test_case + 1, 0 if N % K == 0 else 1))