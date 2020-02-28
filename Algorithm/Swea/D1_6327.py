import sys
sys.stdin = open("D1_6327_input.txt", "r")

def square(n, m):
    print("square({}) => {}".format(n, pow(n, 2)))
    print("square({}) => {}".format(m, pow(m, 2)))

N, M = map(int, input().split(','))
square(N, M)