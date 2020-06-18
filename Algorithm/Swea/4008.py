import sys
sys.stdin = open("4008_input.txt", "r")

operators = {1: '+', 2: '-', 3: '*', 4: '/'}

T = int(input())
for test_case in range(1):
    N = int(input())
    a, b, c, d = map(int, input().split())
    data = list(map(int, input().split()))
    op = '+' * a + '-' * b + '*' * c + '/' * d
    # for i in op: