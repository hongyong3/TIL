import sys
sys.stdin = open("Line_test6_input.txt", "r")
N = list(map(str, input().split()))
data = [list(map(int, input().split())) for _ in range(int(N[0]))]
print(data)
