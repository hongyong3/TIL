import sys
sys.stdin = open("D5_6697_input.txt", "r")

bracket = {0: ')', 1: '())'}

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = ''
    for i in range(N):
        if a <= arr[i]