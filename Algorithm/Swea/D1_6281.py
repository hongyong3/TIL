import sys
sys.stdin = open("D1_6281_input.txt", "r")

N = int(input())
print(list(filter(lambda x: not N % x, range(1, N + 1))))