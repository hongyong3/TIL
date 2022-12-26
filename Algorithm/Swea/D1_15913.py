import sys
sys.stdin = open("D1_15913_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = list(map(int, input().split()))
    a, b = map(int, input().split())
    print("#{} {}".format(test_case + 1, sum(arr[a - 1 : b]) // (b - a + 1)))