import sys
sys.stdin = open("D3_5162_input.txt")

T = int(input())
for test_case in range(T):
    A, B, C = map(int, input().split())
    count = 0
    if A < B:
        count = C // A
    else:
        count = C // B
    print("#{} {}".format(test_case + 1, count))