import sys
sys.stdin = open("D4_1808_input.txt", "r")


T = int(input())
for test_case in range(1):
    data = list(map(int, input().split()))
    N = int(input())
    ans = float('inf')
    num = []
    for i in range(10):
        if data[i] == 1:
            num.append(i)
    print(num)