import sys
sys.stdin = open("D5_13243_input.txt", "r")

T = int(input())
for test_case in range(T):
    H, W = map(int, input().split())
    arr = [input() for _ in range(H)]
    print(arr)
