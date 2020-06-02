import sys
sys.stdin = open("D5_5295_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))