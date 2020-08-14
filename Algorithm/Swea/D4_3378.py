import sys
sys.stdin = open("D4_3378_input.txt", "r")

T = int(input())
for tset_case in range(T):
    p, q = map(int, input().split())
    before = [input() for _ in range(p)]
    after = [input() for _ in range(q)]