import sys
sys.stdin = open("D5_4411_input.txt", "r")

# 요세푸스 점화식
T = int(input())
for test_case in range(1):
    N, K = map(int, input().split())
    mat = 0
    for i in range(1, N + 1):
        mat = (mat + K) % i + 1
    print("#{} {}".format(test_case + 1, mat))