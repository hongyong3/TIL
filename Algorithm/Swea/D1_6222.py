import sys
sys.stdin = open("D1_6222_input.txt", "r")

data = input()
print(data + "(ASCII: " + str(ord(data)) + ") =>", str(data.upper()) + "(ASCII: " + str(ord(data.upper())) + ")")