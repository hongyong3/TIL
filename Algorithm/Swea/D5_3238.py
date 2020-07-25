import sys
sys.stdin = open("D5_3238_input.txt", "r")

T = int(input())
for test_case in range(T):
    n, r, p = map(int, input().split())
    pp = p / n *  