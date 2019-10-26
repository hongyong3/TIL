import sys
sys.stdin = open("D4_4530_input.txt", "r")

# 9진수 변환
# 고려해야할 것 1, 2, 3, 5, 6, 7, 8, 9, 0이 아니라 1, 2, 3, 4, 5, 6, 7, 8, 0
def solve(n):
    if n[0] == "-":
        for i in range(1, len(A)):
            if n[i] > '3':
                pass

T = int(input())
for test_case in range(T):
    A, B = map(str, input().split())
    solve(A)