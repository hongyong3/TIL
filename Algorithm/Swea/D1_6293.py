import sys, math
sys.stdin = open("D1_6293_input.txt", "r")

data = list(map(int, input().split(', ')))
print(', '.join(list(str(round(2 * x * math.pi, 2)) for x in data)))
