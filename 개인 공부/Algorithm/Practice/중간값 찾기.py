import sys
sys.stdin = open("중간값 찾기_input.txt", "r")
T = int(input())
data = list(map(int, input().split()))
new = sorted(set(data))
print(new[len(new)//2+1])