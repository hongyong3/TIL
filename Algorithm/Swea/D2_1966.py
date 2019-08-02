import sys
sys.stdin = open("D2_1966_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(map(int, input().split()))
    print("#{} ".format(test_case + 1), end="")
    print(*data)
