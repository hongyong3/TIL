import sys
sys.stdin = open("D4_7208_input.txt", "r")

T = int(input())
for test_case in range(1):
    N = int(input())
    color = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]

    for i in data:
        print(*i)
