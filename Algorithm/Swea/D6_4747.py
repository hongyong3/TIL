import sys
sys.stdin = open("D6_4747_input.txt", "r")

def solve(cnt, total, start):
    if chk:
        return
    if cnt == 3:

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    total = sum(data) // 3
    chk = 0
