import sys
sys.stdin = open("D1_6313_input.txt", "r")

N = int(input())
print("ASCII {} => {}".format(N, chr(N)))