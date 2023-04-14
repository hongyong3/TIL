# import sys
# sys.stdin = open("D1_17104_input.txt", "r")

for x in range(0, 81, 20):
    print(*[i for i in range(1 + x, 11 + x)])
    print(*[i for i in range(20 + x, 10 + x, - 1)])