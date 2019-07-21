import sys
sys.stdin = open("D2_1926_input.txt", "r")

N = int(input())
for i in range(1, N + 1):
    a = str(i)
    b = a.count("3") + a.count("6") + a.count("9")
    if (b > 0 ):
        a = "-" * b
    print(a, end=" ")