import sys
sys.stdin = open("D3_5204_input.txt", "r")

T = int(input())
for _test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    data1, data2 = data[:N // 2], data[N // 2:]
    print(data)
    print(data1, data2)
    print(sorted(data1), sorted(data2))