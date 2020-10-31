import sys
sys.stdin = open("D3_9940_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = len(set(map(int, input().split())))
    print("#{} {}".format(test_case + 1, "Yes" if N == data else "No"))