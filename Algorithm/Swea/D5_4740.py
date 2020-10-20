import sys
sys.stdin = open("D5_4740_input.txt", "r")

def down():
    pass

def up():
    pass

def left():
    pass

def right():
    pass

T = int(input())
for test_case in range(T):
    N, M, Q = map(int, input().split())
    data = [input() for _ in range(N)]

    for _ in range(Q):
        q = input()
        if q == 'D':
            pass
        elif q == 'L':
            pass
        elif q == 'R':
            pass
        else:
            pass