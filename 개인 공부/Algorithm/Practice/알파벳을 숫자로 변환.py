import sys
sys.stdin = open("알파벳을 숫자로 변환_input.txt", "r")
for i in input():print(ord(i)-64,end=' ')