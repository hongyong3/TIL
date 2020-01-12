import sys
sys.stdin = open("6206_input.txt", "r")

N = int(input())
print("{}".format(N)  + ".00 kg =>  " "{}".format('%.2f' % (N * 2.2046)) + " lb")