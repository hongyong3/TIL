import sys
sys.stdin = open("D1_6248_input.txt", "r")

data = str(input())
print(''.join(list(data[x] for x in range(len(data)) if not x % 2)))