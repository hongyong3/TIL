import sys
sys.stdin = open("D3_1491_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, A, B = map(int, input().split())
    minRC = float('inf')
    for i in range(1, N):
        for j in range(i,  N // i + 1):
            value = A * abs(j - i) + B * (N - j * i)
            if value < minRC: minRC = value
    print("#{} {}".format(test_case + 1, minRC))