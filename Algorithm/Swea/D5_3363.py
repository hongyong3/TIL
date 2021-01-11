import sys
sys.stdin = open("D5_3363_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [0] * N
    for i in range(N):
        x, y, z = map(int, input().split())
        temp = (x + y) * (y - x + 1) // 2
        arr[i] = temp