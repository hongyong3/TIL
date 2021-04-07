import sys
sys.stdin = open("D3_11346_input.txt", "r")


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    a, b = 0, 0
    for i in data:
        if i % 2:
            a += 1
        else:
            b += 1
    print("#{} {}".format(test_case + 1, a + b if a == b else min(a, b) * 2 + 1))
    