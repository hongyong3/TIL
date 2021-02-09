import sys
sys.stdin = open("D5_1816_input.txt", "r")

# bit masking...?
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    K = int(input())