import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for test_case in range(T):
   temp = input()  #dummy
   data = list(map(str, input().split()))
   print(data)

   count = [0] * 10
   for i in data:
