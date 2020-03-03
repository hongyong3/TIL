import sys
sys.stdin = open("D1_6678_input.txt", "r")

data = [str(input()) for _ in range(3)]
for i in data:
    print(">> {}".format(i.upper()))