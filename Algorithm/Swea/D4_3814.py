import sys
sys.stdin = open("D4_3814_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    print(N, K)
    print(data)