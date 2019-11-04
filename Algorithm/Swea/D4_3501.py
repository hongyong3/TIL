import sys
sys.stdin = open("D4_3501_input.txt", "r")
T = int(input())
for test_case in range(T):
   p, q = map(int, input().split())
   if p / q == p // q:
       print("#{} {}".format(test_case + 1, p // q))
   else:
       print("#{} {}".format(test_case + 1, p / q))