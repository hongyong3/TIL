import sys
sys.stdin = open("D1_6220_input.txt", "r")

data = input()
if data.islower():
    print(data + " 는 소문자 입니다.")
else:
    print(data + " 는 대문자 입니다.")