import sys
sys.stdin = open("D2_1970_input.txt", "r")

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(T):
    N = int(input())
    i = 0
    count = [0] * 8
    while i < len(count):
        if N >= money[i]:
            N = N - money[i]
            count[i] += 1
        else:
            i += 1
    print("#{}".format(test_case + 1))
    print(*count)
