import sys
sys.stdin = open("D1_6221_input.txt", "r")

a = str(input())
b = str(input())
if a == b:
    print("Result : Draw")
elif a == "가위" and b == "보" or a == "바위" and b == "가위" or a == "보" and b == "바위":
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")