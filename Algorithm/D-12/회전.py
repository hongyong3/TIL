import sys
sys.stdin = open("회전_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = list(input().split())
    ans = data[M % N]
    print(f"#{test_case} {ans}")