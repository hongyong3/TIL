import sys
sys.stdin = open("D8_11211_input.txt", "r")

def getMax(x, y):
    if (a - b) & 0x80000000:
        print("c = {}".format(b - a))
        print("b가 a보다 큽니다.")
    else:
        print("c = {}".format(a - b))
        print("a가 b보다 큽니다.")

T = int(input())
for test_case in range(T):
    a = int(input().split()[2])
    b = int(input().split()[2])
    getMax(a, b)
