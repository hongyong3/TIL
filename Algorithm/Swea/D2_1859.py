import sys
sys.stdin = open("D2_1859_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sum, max = 0, 0
    for i in range(N):
        a = data[- 1 - i]
        if (a > max):
            max = a
        sum += max - a
    print("#{} {}".format(test_case + 1, sum))
