import sys
sys.stdin = open("D4_1251_input.txt", "r")

T = int(input())


for test_case in range(2):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    distance = float('inf')