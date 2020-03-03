import sys
sys.stdin = open("D1_6260_input.txt", "r")

data = str(input())
upper, lower = 0, 0
for i in data:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("UPPER CASE {}".format(upper))
print("LOWER CASE {}".format(lower))