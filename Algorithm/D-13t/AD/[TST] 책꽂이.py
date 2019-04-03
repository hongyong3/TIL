import sys
sys.stdin = open("[TST] 책꽂이_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, B = map(int, input().split())
    H_i = [list(input()) for _ in range(N)]
    print(H_i)