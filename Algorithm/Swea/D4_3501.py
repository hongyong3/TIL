import sys
sys.stdin = open("D4_3501_input.txt", "r")

T = int(input())
for test_case in range(T):
   p, q = map(int, input().split())
   ans = '0.'
   if p / q == p // q:
       print("#{} {}".format(test_case + 1, p // q))
   else:
       if len(str(float(p) / float(q))) <= 4:
           print("#{} {}".format(test_case + 1, p / q))
       else:
           circulating = str("%.50f" % (p / q))[2:]
           for i in range(len(circulating)):
               j = i + 1
               while j < len(circulating):
                   if circulating[i : j] == circulating[j : 2 * j]:
                       ans += '(' + circulating[i : j] + ')'
                       break
                   else:
                       j += 1
               break
           print("#{} {}".format(test_case + 1, ans))