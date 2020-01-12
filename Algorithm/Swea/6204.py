import sys
sys.stdin = open("6204_input.txt", "r")

N = int(input())
print("{}".format(N)  + ".00 inch =>  " "{}".format(N * 2.54) + " cm")