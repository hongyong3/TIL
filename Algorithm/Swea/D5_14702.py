import sys
sys.stdin = open("D5_14702_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    