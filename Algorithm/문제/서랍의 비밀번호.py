import sys
sys.stdin = open("서랍의 비밀번호_input.txt", "r")
data = list(map(int, input().split()))
print(data[0]-data[1]+1)