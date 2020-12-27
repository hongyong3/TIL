import sys
sys.stdin = open("D1_2072_input.txt", "r")

T = int(input())
for test_case in range(T):
    print("#{} {}".format(test_case + 1, sum(i for i in list(map(int, input().split())) if i % 2)))