import sys
sys.stdin = open("암호코드 스캔_input.txt", "r")
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(M)]