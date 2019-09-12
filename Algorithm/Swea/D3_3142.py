import sys
sys.stdin = open("D3_3142_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    print("#{} {} {}".format(test_case + 1, 2 * M - N, N- M))