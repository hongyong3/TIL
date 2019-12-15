import sys
sys.stdin = open("D4_1808_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    N = int(input())
    print(data)
    print(N)
