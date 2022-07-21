import sys
sys.stdin = open("D2_14577_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print("#{} {}".format(test_case + 1, max(arr) - min(arr)))