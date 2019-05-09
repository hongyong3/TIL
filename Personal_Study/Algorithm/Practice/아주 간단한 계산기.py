import sys
sys.stdin = open("아주 간단한 계산기_input.txt", "r")
data = list(map(int, input().split()))
print(data[0]+data[1]), print(data[0]-data[1]), print(data[0]*data[1]), print(data[0]//data[1])