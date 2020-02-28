import sys
sys.stdin = open("D1_6326_input.txt", "r")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(int(input())))