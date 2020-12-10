import sys
sys.stdin = open("D4_11112_input.txt", "r")

T = int(input())
for test_case in range(T):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())