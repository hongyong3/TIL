import sys
sys.stdin = open("자릿수 더하기_input.txt", "r")
data = list(map(int, input()))
sums = 0
for i in data:
    sums += i
print(sums)
