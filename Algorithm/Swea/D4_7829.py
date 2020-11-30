import sys
sys.stdin = open("D4_7829_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(map(int, input().split())))
    print("#{} {}".format(test_case + 1, data[0] * data[- 1]))