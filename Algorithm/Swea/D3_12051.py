import sys
sys.stdin = open("D3_12051_input.txt", "r")

T = int(input())
for test_case in range(T):
    PD, PG, N = map(int, input().split())
    ans = "Possible"    # "Broken"