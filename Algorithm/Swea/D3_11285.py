import sys
sys.stdin = open("D3_11285_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        distance = (x ** 2 + y ** 2) ** 0.5
        print(distance)