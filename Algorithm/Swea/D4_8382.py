import sys
sys.stdin = open("D4_8382_input.txt", "r")

T = int(input())
for test_case in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    xSum, ySum = abs(x1 - x2), abs(y1 - y2)
    big, small = max(xSum, ySum), min(xSum, ySum)
    diff = big - small
    print("#{} {}".format(test_case + 1, 2 * small + 2 * diff - (diff % 2)))