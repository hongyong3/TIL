import sys
sys.stdin =open("미로_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    print(table)