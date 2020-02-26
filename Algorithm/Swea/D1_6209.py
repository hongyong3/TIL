import sys
sys.stdin = open("D1_6209_input.txt", "r")

a = int(input())
print("%0.2f" % a, "℉ => ", round((a - 32) * 5 / 9, 2), "℃")


# 82.00 ℉ =>  27.78 ℃
# 82.00 ℉ =>  27.78 ℃