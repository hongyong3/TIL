import sys
sys.stdin = open("D3_5204_input.txt", "r")

T = int(input())
for _test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    mid = N // 2
    data1, data2 = data[: mid], data[mid:]