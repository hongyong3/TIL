import sys
sys.stdin = open("D3_17937_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    print("#{} {}".format(test_case + 1, A if A == B else 1))