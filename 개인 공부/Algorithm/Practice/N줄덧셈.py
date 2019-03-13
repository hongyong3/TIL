import sys
sys.stdin = open("N줄덧셈_input.txt", "r")
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)