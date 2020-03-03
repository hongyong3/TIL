import sys
sys.stdin = open("D1_6232_input.txt", "r")

data = str(input())
print(data)
if data == data[:: - 1]:
    print("입력하신 단어는 회문(Palindrome)입니다.")