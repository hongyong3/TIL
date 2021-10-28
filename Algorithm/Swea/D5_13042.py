import sys
sys.stdin = open("D5_13042_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    math = [list(map(int, input().split())) for _ in range(M)]  # Si, Ei
    science = [list(map(int, input().split())) for _ in range(N - M)]   # Si, Ei
    print(math)
    print(science)
    print()