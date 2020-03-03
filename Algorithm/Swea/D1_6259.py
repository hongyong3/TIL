import sys
sys.stdin = open("D1_6259_input.txt", "r")

data = str(input())
alpha, num = 0, 0
for i in data:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        num += 1

print("LETTERS {}".format(alpha))
print("DIGITS {}".format(num))