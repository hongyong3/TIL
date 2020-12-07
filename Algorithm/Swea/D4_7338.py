import sys
sys.stdin = open("D4_7338_input.txt", "r")

T = int(input())
for test_case in range(T):
    Y, M = map(int, input().split())
    diff = (Y - 2016) * 12 + M
    y = 2016 + (diff // 13)
    m = diff % 13
    if m == 0:
        m = 13
        y -= 1

    print("#{} {} {}".format(test_case + 1, y, m))