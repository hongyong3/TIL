import sys
sys.stdin = open("D1_6239_input.txt", "r")

print(*list(map(str, input().split()))[:: - 1])
