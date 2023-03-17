import sys
sys.stdin = open("D2_16811_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    