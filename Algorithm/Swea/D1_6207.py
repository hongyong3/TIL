import sys
sys.stdin = open("D1_6207_input.txt", "r")

a = int(input())
# print("%0.2f" % a + " ℃ =>  " + "%0.2f" % (a * 1.8 + 32) + " ℉")
print("%0.2f" % a, "℃ => ", "%0.2f" % (a * 1.8 + 32), "℉")