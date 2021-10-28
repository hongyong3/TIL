import sys
sys.stdin = open("D6_13043_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, P = map(int, input().split())
    arr = list(map(int, input().split()))
    