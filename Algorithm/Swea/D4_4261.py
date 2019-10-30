import sys
sys.stdin = open("D4_4261_input.txt", "r")

T = int(input())
for test_case in range(T):
    S, N = map(int, input().split())
    data = list(map(str, input().split()))
    print(S, N)
    print(data)
