import sys
sys.stdin = open("D1_6292_input.txt", "r")

data = list(map(int, input().split(', ')))
print(data)
print(tuple(data))