import sys
sys.stdin = open("[PY-TST]1~n까지의 합 (Recursion Version)_input.txt", "r")

N = int(input())
sum = 0
sum = N*(N+1) // 2
print(sum)