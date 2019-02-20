import sys
sys.stdin = open("계산기3_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input().split()
    print(data)
    operators = {'+': 0, "*": 1, "(": 2}
    stack = []
