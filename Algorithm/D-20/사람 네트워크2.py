import sys
sys.stdin = open("사람 네트워크2_input.txt", "r")

T = int(input())
for test_case in range(1):
    data = list(map(int, input().split()))
    print(data)