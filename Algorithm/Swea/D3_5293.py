import sys
sys.stdin = open("D3_5293_input.txt", "r")

A, B, C, D = '00', '01', '10', '11'
T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    print(data)