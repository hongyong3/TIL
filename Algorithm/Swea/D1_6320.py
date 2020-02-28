import sys
sys.stdin = open("D1_6320_input.txt", "r")

def RPS(a, b):
    if a == b:
        return "비겼습니다"
    elif a == "가위" and b == "보" or a == "바위" and b == "가위" or a == "보" and b == "바위":
        return a
    else:
        return b
a = input()
b = input()
a1 = input()
b1 = input()

print("{}가 이겼습니다!".format(RPS(a1, b1)))