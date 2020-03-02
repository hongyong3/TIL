import sys
sys.stdin = open("D1_6297_input.txt", "r")

num = list(map(int, input().split(', ')))
print(', '.join(list(str(x) for x in num if x % 2)))